import gsheet_connection as gsc
import streamlit as st
import datetime
import re

def reservation_date_validation(lunch_or_dinner,head_count,reservation_date):
    dt = datetime.datetime.today()

    if reservation_date==datetime.date.today() and lunch_or_dinner=="Midi" and ((dt.hour==13 and dt.minute>30) or dt.hour>13):
        return [f"Il n'est plus possible de réserver pour le service de ce midi",False]
    elif reservation_date==datetime.date.today() and lunch_or_dinner=="Soir" and ((dt.hour==21 and dt.minute>30) or dt.hour>21):
        return [f"Il n'est plus possible de réserver pour le service de ce soir",False]
    else:
        try:
            reservation_date_format_gsheet=reservation_date.strftime('%d/%m/%Y')
            disponibilities = gsc.get_disponibilities()
            restaurant_capacity = int(list(disponibilities.loc[disponibilities["Date"]==reservation_date_format_gsheet,lunch_or_dinner])[0])
            is_booking_blocked_lunch = list(disponibilities.loc[disponibilities["Date"]==reservation_date_format_gsheet,"Is_booking_blocked_midi"])[0]
            is_booking_blocked_lunch = False if is_booking_blocked_lunch=="FALSE" else True
            is_booking_blocked_dinner = list(disponibilities.loc[disponibilities["Date"]==reservation_date_format_gsheet,"Is_booking_blocked_soir"])[0]
            is_booking_blocked_dinner = False if is_booking_blocked_dinner=="FALSE" else True

            if reservation_date.weekday() == 5:
                    return [f"Le restaurant Nuances est fermé le samedi",False]
            elif reservation_date.weekday() == 6:
                    return [f"Le restaurant Nuances est fermé le dimanche",False]
            else:
                if head_count > restaurant_capacity or (lunch_or_dinner=="Midi" and is_booking_blocked_lunch) or (lunch_or_dinner=="Soir" and is_booking_blocked_dinner):
                    if lunch_or_dinner == "Midi":
                        return [f"Le restaurant Nuances est complet le midi du {reservation_date.strftime('%d %B %Y')}",False]
                    else:
                        if reservation_date.weekday() == 4:
                            return [f"Le restaurant Nuances est complet le soir du {reservation_date.strftime('%d %B %Y')}",False]
                        else:
                            return [f"Le restaurant Nuances n'ouvre que le vendredi soir",False]
                else:
                    return ["",True];
        except IndexError:
            pass

def is_reservation_name_completed(reservation_name):
    if reservation_name == "":
        st.session_state.is_reservation_name_completed = False
        return False
    else:
        st.session_state.is_reservation_name_completed = True
        return True

def is_phone_number_completed(phone_number):
    if phone_number == "":
        st.session_state.is_phone_number_completed = False
        return False
    else:
        st.session_state.is_phone_number_completed = True
        return True
    
def is_email_completed(email):
    if re.match("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])",email) is None:
        st.session_state.is_email_completed = False
        return False
    else:
        st.session_state.is_email_completed = True
        return True