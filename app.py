import streamlit as st
import pandas as pd
from datetime import datetime

# Load existing data or create a new one
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("clients.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Age", "Gender", "Last Visit", "Next Appointment", "Notes"])
    return df

def save_data(df):
    df.to_csv("clients.csv", index=False)

# Initialize data
df = load_data()

# Page config
st.set_page_config(page_title="Clinic Data Dashboard", layout="wide")

st.title("Clinic Data Dashboard")

# Sidebar navigation
menu = ["Overview", "Add Client", "Contact"]
choice = st.sidebar.radio("Go to", menu)

if choice == "Overview":
    st.subheader("Client Overview")
    st.dataframe(df)

    st.subheader("Filter Clients")
    search_name = st.text_input("Search by Name")
    if search_name:
        filtered_df = df[df['Name'].str.contains(search_name, case=False, na=False)]
        st.dataframe(filtered_df)

elif choice == "Add Client":
    st.subheader("Add New Client")

    with st.form("client_form", clear_on_submit=True):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        last_visit = st.date_input("Last Visit")
        next_appointment = st.date_input("Next Appointment")
        notes = st.text_area("Notes")

        submitted = st.form_submit_button("Add Client")
        if submitted:
            new_data = pd.DataFrame({
                "Name": [name],
                "Age": [age],
                "Gender": [gender],
                "Last Visit": [last_visit],
                "Next Appointment": [next_appointment],
                "Notes": [notes]
            })
            df = pd.concat([df, new_data], ignore_index=True)
            save_data(df)
            st.success(f"Client '{name}' added successfully!")

elif choice == "Contact":
    st.subheader("Contact Info")
    st.write("📞 Phone: +123 456 789")
    st.write("📧 Email: clinic@example.com")
    st.write("🏥 Address: 123 Clinic Street, Health City")
