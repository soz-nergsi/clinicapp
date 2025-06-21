import streamlit as st
import pandas as pd
from datetime import datetime

# Initial sample data (built-in, no CSV file needed)
data = {
    'Name': ['John Doe', 'Jane Smith', 'Emily Davis', 'Michael Brown'],
    'Age': [34, 29, 42, 36],
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'Last Visit': ['2024-10-15', '2024-10-10', '2024-11-01', '2024-10-20'],
    'Next Appointment': ['2024-11-20', '2024-11-25', '2024-11-30', '2024-11-22'],
    'Notes': [
        'Needs follow-up on test results',
        'Routine check-up',
        'Dietary consultation',
        'Blood pressure monitoring'
    ]
}
df = pd.DataFrame(data)

# Streamlit app config
st.set_page_config(page_title="Clinic Data Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Dashboard Navigation")
menu = ["Overview", "Add Client", "Contact"]
choice = st.sidebar.radio("Go to", menu)

# Main Pages
if choice == "Overview":
    st.title("Clinic Data Dashboard")
    st.subheader("Client Overview")
    st.dataframe(df)

    st.subheader("Filter Clients")
    search = st.text_input("Search by Name")
    if search:
        filtered_df = df[df['Name'].str.contains(search, case=False)]
        st.dataframe(filtered_df)

elif choice == "Add Client":
    st.title("Add New Client")

    with st.form("add_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        gender = st.selectbox("Gender", ["Male", "Female"])
        last_visit = st.date_input("Last Visit")
        next_appointment = st.date_input("Next Appointment")
        notes = st.text_area("Notes")

        submitted = st.form_submit_button("Add Client")
        if submitted:
            new_entry = {
                'Name': name,
                'Age': age,
                'Gender': gender,
                'Last Visit': last_visit.strftime('%Y-%m-%d'),
                'Next Appointment': next_appointment.strftime('%Y-%m-%d'),
                'Notes': notes
            }
            # Append new entry to dataframe (temporary, not saved to file)
            df.loc[len(df)] = new_entry
            st.success("Client added successfully!")
            st.dataframe(df)

elif choice == "Contact":
    st.title("Contact Information")
    st.write("Clinic Address: 123 Health Street, Wellness City")
    st.write("Phone: +1 234 567 890")
    st.write("Email: clinic@example.com")
