import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

import json
import pandas as pd
from datetime import datetime
import streamlit as st

# If modifying these scopes, delete the file token.json.
# SCOPES = st.secrets.gsheet_connection.scopes
# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = st.secrets.gsheet_connection.spreadsheet_id
SERVICE_ACCOUNT_JSON = json.loads(st.secrets.gsheet_connection.gsheet_k)

def spreadsheet_connection():
  # creds = service_account.Credentials.from_service_account_info(SERVICE_ACCOUNT_JSON, scopes=SCOPES)
  creds = service_account.Credentials.from_service_account_info(SERVICE_ACCOUNT_JSON)
  try:
    service = build("sheets", "v4", credentials=creds)
    return service
  except HttpError as err:
    print(err)


def get_disponibilities():
    service = spreadsheet_connection()

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SPREADSHEET_ID, range="'Disponibilités'!A1:G")
        .execute()
    )
    values = result.get("values", [])

    return pd.DataFrame(values[1:],columns=["Jour","Date","Midi","Soir","Is_booking_blocked_midi","Is_booking_blocked_soir","Nb_of_booking_through_form"])
    
def update_disponibilities(reservation_date,lunch_or_dinner,head_count,add_reservation):

  try:
    service = spreadsheet_connection()
    disponibilities = get_disponibilities()
    reservation_date_format_gsheet=reservation_date.strftime('%d/%m/%Y')
    row_to_update = disponibilities.loc[disponibilities["Date"]==reservation_date_format_gsheet]
    row_nb_to_update = row_to_update.index[0]+2
    restaurant_capacity = int(list(row_to_update[lunch_or_dinner])[0])

    update_restaurant_capacity_range = f"'Disponibilités'!C{row_nb_to_update}:C{row_nb_to_update}" if lunch_or_dinner=="Midi" else f"'Disponibilités'!D{row_nb_to_update}:D{row_nb_to_update}"
    if add_reservation:
      values = [[restaurant_capacity-head_count]]
    else:
      values = [[restaurant_capacity+head_count]]
    body = {"values": values}
    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=SPREADSHEET_ID,
            range=update_restaurant_capacity_range,
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )

    nb_booking_through_form = int(list(row_to_update["Nb_of_booking_through_form"])[0])
    update_nb_booking_through_form_range = f"'Disponibilités'!G{row_nb_to_update}:G{row_nb_to_update}"
    if add_reservation:
      values = [[nb_booking_through_form+1]]
    else:
      values = [[nb_booking_through_form-1]]
    body = {"values": values}
    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=SPREADSHEET_ID,
            range=update_nb_booking_through_form_range,
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error

def get_reservations():
    service = spreadsheet_connection()

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SPREADSHEET_ID, range="'Réservations'!A1:K")
        .execute()
    )
    values = result.get("values", [])

    return pd.DataFrame(values[1:],columns=values[0])

def get_reservation_by_id(id):
    reservations = get_reservations()
    return reservations[reservations["Id"]==id]

def get_last_reservation_row():
    return len(get_reservations());

def set_reservation(reservation_id,reservation_name,lunch_or_dinner,reservation_date,reversation_time,head_count,email,phone_number,comments):
    try:
        service = spreadsheet_connection()
        values = [[reservation_id,json.dumps(datetime.now().isoformat())[1:-1],0,reservation_name,lunch_or_dinner,str(reservation_date),reversation_time,head_count,email,str(phone_number),comments]]
        body = {"values": values}
        last_reservation_row = get_last_reservation_row()
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=SPREADSHEET_ID,
                range=f"'Réservations'!A{last_reservation_row+2}:K{last_reservation_row+2}",
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
        update_disponibilities(reservation_date,lunch_or_dinner,head_count,True)
        return True
    except HttpError as error:
        return False
    
def delete_reservation(reservation_id,reservation_date,lunch_or_dinner,head_count):
    reservations = get_reservations()
    reservation_to_update = reservations[reservations["Id"]==reservation_id]

    try:
      service = spreadsheet_connection()
      row_nb_to_update = reservation_to_update.index[0]+2
      update_restaurant_capacity_range = f"'Réservations'!C{row_nb_to_update}:C{row_nb_to_update}"

      body = {"values": [[1]]}
      result = (
          service.spreadsheets()
          .values()
          .update(
              spreadsheetId=SPREADSHEET_ID,
              range=update_restaurant_capacity_range,
              valueInputOption="USER_ENTERED",
              body=body,
          )
          .execute()
      )
      update_disponibilities(reservation_date,lunch_or_dinner,head_count,False)
    except HttpError as error:
        return error
  