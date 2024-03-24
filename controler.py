from data_validation import is_reservation_name_completed
from data_validation import is_phone_number_completed
from data_validation import is_email_completed
from data_validation import reservation_date_validation
import gsheet_connection as gsc
from format_email import format_email_html

import time
import uuid
from smtplib import SMTP
from email.message import EmailMessage
import streamlit as st

def send_user_reservation_to_gsheet(reservation_name,lunch_or_dinner,reservation_date,hours,minutes,head_count,email,phone_number,comments):
    is_reservation_name_completed_ = is_reservation_name_completed(reservation_name)
    is_phone_number_completed_ = is_phone_number_completed(phone_number)
    is_email_completed_ = is_email_completed(email)
    is_date_validated = reservation_date_validation(lunch_or_dinner,head_count,reservation_date)[1]

    if is_reservation_name_completed_ and is_phone_number_completed_ and is_email_completed_ and is_date_validated:
        reservation_id = str(time.time())+str(uuid.uuid4())
        reversation_time = str(hours)+":"+str(minutes)
        comments = "None" if comments=="" else comments

        send_email_confirmation(reservation_id,reservation_name,reservation_date,reversation_time,head_count,email,phone_number)
        set_reservation_state = gsc.set_reservation(reservation_id,reservation_name,lunch_or_dinner,reservation_date,reversation_time,head_count,email,phone_number,comments)
        st.session_state.is_reservation_completed = set_reservation_state


def send_email_confirmation(reservation_id,reservation_name,reservation_date,reservation_time,head_count,email,phone_number):
    
    subject="Restaurant Nuances: Confirmation de votre réservation"
    
    sender= st.secrets.email_credentials.email_username
    USERNAME = st.secrets.email_credentials.email_username
    PASSWORD = st.secrets.email_credentials.email_password

    msg = EmailMessage()
    msg.set_type('text/html')
    msg['Subject']= subject
    msg['From']   = sender
    msg['To']   = email

    booking_app_url=st.secrets.booking_app.url
    booking_app_remove_reservation_url=st.secrets.booking_app.url_reservation_id+reservation_id
    
    msg.add_alternative(format_email_html(booking_app_url,booking_app_remove_reservation_url,reservation_name,reservation_date,reservation_time,head_count,phone_number), subtype="html")
        
    server = SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(sender, email, msg.as_string())
    server.sendmail(sender, st.secrets.restaurantnuances.email, msg.as_string())
    server.close()

