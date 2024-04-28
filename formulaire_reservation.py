import streamlit as st
import datetime
import dateutil.relativedelta
import locale
locale.setlocale(locale.LC_ALL, "fr_FR")
import data_validation as dv
import controler as ctr
from streamlit_js_eval import streamlit_js_eval

# SESSION VARIABLES INITIALISATION
if "is_reservation_name_completed" not in st.session_state:
    st.session_state.is_reservation_name_completed = True
if "is_email_completed" not in st.session_state:
    st.session_state.is_email_completed = True
if "is_phone_number_completed" not in st.session_state:
    st.session_state.is_phone_number_completed = True
if "is_reservation_completed" not in st.session_state:
    st.session_state.is_reservation_completed = False


# FORM
st.title("Restaurant Nuances")
col_title, col_image = st.columns([5,1])
with col_title:
    st.subheader("Réservation")
with col_image:
    st.image("logo_nuances.png",width=100)
st.divider()

if st.session_state.is_reservation_completed==True:
    st.write("Nous avons bien reçu votre réservation!")
    st.write("Merci de choisir le Restaurant Nuances. À très vite!")
else :
    st.write(":red[*]Champs obligatoires")

    st.write('<style>div.row-widget.stRadio > div {flex-direction:row;}</style>', unsafe_allow_html=True)
    lunch_or_dinner = st.radio("Pour quel service souhaitez-vous faire une réservation, midi ou soir?:red[*]", ["Midi", "Soir"])

    head_count = st.number_input("Pour combien de personnes souhaitez-vous réserver?:red[*]", min_value=1, max_value=6)

    date_and_time = datetime.datetime.today()
    if date_and_time.weekday() in range(0,4) and ((date_and_time.hour==13 and date_and_time.minute>30) or date_and_time.hour>13):
        date_days_delta = 1
    elif date_and_time.weekday()==4 and ((date_and_time.hour==21 and date_and_time.minute>30) or date_and_time.hour>21):
        date_days_delta = 3
    elif date_and_time.weekday()==5:
        date_days_delta = 2
    elif date_and_time.weekday()==6:
        date_days_delta = 1
    else:
        date_days_delta = 0

    reservation_date = st.date_input("Date de la réservation:red[*]",
                                    value=datetime.datetime.now()+dateutil.relativedelta.relativedelta(days=date_days_delta),
                                    min_value=datetime.datetime.now()+dateutil.relativedelta.relativedelta(days=date_days_delta), 
                                    max_value=datetime.datetime.now()+dateutil.relativedelta.relativedelta(months=3),
                                    format="DD/MM/YYYY")

    st.write(f":red[{dv.reservation_date_validation(lunch_or_dinner,head_count,reservation_date)[0]}]")

    reservation_hour_col1, reservation_hour_col2 = st.columns(2)
    if lunch_or_dinner == "Midi":
        with reservation_hour_col1:
            hours = st.number_input("Heures:red[*]", min_value=12, max_value=13, step=1)
        with reservation_hour_col2:
            minutes = st.number_input("Minutes:red[*]", min_value=0, max_value=30, step=15, value=15)
            minutes = "00" if minutes==0 else minutes
    else:
        with reservation_hour_col1:
            hours = st.number_input("Heures:red[*]", min_value=20, max_value=21, step=1)
        with reservation_hour_col2:
            minutes = st.number_input("Minutes:red[*]", min_value=0, max_value=30, step=15, value=15)
            minutes = "00" if minutes==0 else minutes

    reservation_name = st.text_input("Nom: :red[*]")
    if st.session_state.is_reservation_name_completed==False:
        st.write(":red[Merci de renseigner le nom de la réservation]")

    email = st.text_input("Adresse email: :red[*] (Un email de confirmation sera envoyé à cette adresse email)")
    if st.session_state.is_email_completed==False:
        st.write(":red[Merci de renseigner une adresse email pour la réservation]")

    phone_number = st.text_input("Téléphone: :red[*]")
    if st.session_state.is_phone_number_completed==False:
        st.write(":red[Merci de renseigner un numéro de téléphone pour la réservation]")

    comments = st.text_input("Commentaires:")

    st.button("Réserver",on_click=ctr.send_user_reservation_to_gsheet,args=(reservation_name,lunch_or_dinner,reservation_date,hours,minutes,head_count,email,phone_number,comments), disabled=phone_number=="")