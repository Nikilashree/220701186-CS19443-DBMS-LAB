import streamlit as st
from database_hospital import *
from database_patient import *


def update_hospital():
    col1, col2 = st.columns(2)
    with col1:
        H_ID  = st.number_input("Enter the ID of hospital you want to update:")
        new_H_Name = st.text_input("Name:")
        
    with col2:
        new_H_Address=st.text_input("Address")
        new_Ph_Number=st.text_input("Number:")

    if st.button("Update"):
        update_hospital_row(H_ID, new_H_Name, new_H_Address, new_Ph_Number)
        st.success("Successfully UPDATED : {}".format(new_H_Name))
        
def update_patient():
    col1, col2, col3, col4= st.columns(4)
    with col1:
        p_id  = st.number_input("Enter the ID of Patient you want to update:")
        new_p_date = st.date_input("Date:")
        
    with col2:
        p_name=st.text_input("Name")
        p_r_request=st.text_input("Reason:")
    with col3:
        p_organid = st.number_input("OrganID")
        p_doctorid = st.text_input("Doctor ID")
    with col4:
        p_procurement = st.date_input("Enter Procurement Date   ")
    if st.button("Update"):
        update_patient_row(p_id, new_p_date, p_name, p_r_request,p_organid,p_doctorid,p_procurement)
        st.success("Successfully UPDATED : {}".format(p_name))
        
