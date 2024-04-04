import streamlit as st
import controler as ctr
from datetime import datetime
import gsheet_connection as gsc
from pathlib import Path

st.set_page_config(page_title="remove_reservation")

# SESSION VARIABLES INITIALISATION
if "user_want_to_delete_reservation" not in st.session_state:
    st.session_state.user_want_to_delete_reservation = False

def change_deletion_state(usr_want_to_delete_reservation):
    st.session_state.user_want_to_delete_reservation = usr_want_to_delete_reservation

st.title("Restaurant Nuances")
col_title, col_image = st.columns([5,1])
with col_title:
    st.subheader("Détail de la réservation")
with col_image:
    path = str(Path(__file__).parent.parent) + "/logo_nuances.png"
    st.image(path,width=100)
st.divider()

reservation_id=st.query_params.id
reservation_detail = gsc.get_reservation_by_id(reservation_id)

reservation_date = str(reservation_detail["Date de la réservation"].values[0])+" "+str(reservation_detail["Heure de la réservation"].values[0])
reservation_date = datetime.strptime(reservation_date, "%d/%m/%Y %H:%M")

if reservation_detail["Réservation annulée?"].values[0]=="1":
    st.write("La réservation a été annulée")
elif datetime.now() > reservation_date:
    st.write("Le lien n'est plus valide")
else:
    st.markdown(f"""
                | Nom | {reservation_detail["Nom"].values[0]} |
                | ----------- | ----------- |
                | Service | {reservation_detail["Service"].values[0]} |
                | Date de la réservation | {reservation_detail["Date de la réservation"].values[0]} |
                | Heure de la réservation | {reservation_detail["Heure de la réservation"].values[0]} |
                | Nombre de personnes | {reservation_detail["Nombre de personnes"].values[0]} |
                | Email | {reservation_detail["Email"].values[0]} |
                | Téléphone | {reservation_detail["Téléphone"].values[0]} |
            """)
    
    if reservation_detail["Commentaires"].values[0] != "None":
        st.write(" ")
        st.write(" ")
        st.write("Commentaires : "+reservation_detail["Commentaires"].values[0])

    st.divider()
    if st.session_state.user_want_to_delete_reservation == False:
        st.button("Annuler la réservation",on_click=change_deletion_state,args=(True,))
    else:
        st.write("Confirmez-vous l'annulation de la réservation:")
        col_yes, col_no = st.columns([.5,1])
        with col_yes:
            st.button("Oui",on_click=gsc.delete_reservation,args=(reservation_id,reservation_detail["Nom"].values[0],reservation_detail["Email"].values[0],reservation_detail["Téléphone"].values[0],reservation_date,reservation_detail["Service"].values[0],int(reservation_detail["Nombre de personnes"].values[0])))
        with col_no:
            st.button("Non",on_click=change_deletion_state,args=(False,))
