import streamlit as st
import pandas as pd

# User credentials (for simplicity, we use a dictionary; in a real app, use a database)
USER_CREDENTIALS = {
    "user1": "password123",
    "user2": "pass456",
}

# Function to authenticate user
def authenticate(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        return True
    else:
        return False

# Streamlit app
st.title("Streamlit Auth Interface")

# Create input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Create a button for logging in
if st.button("Login"):
    if authenticate(username, password):
        st.success(f"Welcome {username}!")
        # Here you can add more functionality after a successful login
        st.write("You are now logged in!")
    else:
        st.error("Invalid username or password")

# Optionally, add a sign-up section (not secure, just for demonstration)
st.write("Don't have an account? Sign up here:")
new_username = st.text_input("New Username")
new_password = st.text_input("New Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Sign Up", key="sign_up"):
    if new_password == confirm_password:
        if new_username in USER_CREDENTIALS:
            st.warning("Username already exists. Please choose a different username.")
        else:
            USER_CREDENTIALS[new_username] = new_password
            st.success("Account created successfully! You can now log in.")
    else:
        st.error("Passwords do not match. Please try again.")

st.title("Gestionnaire de taches")

# Create DataFrame

df = pd.DataFrame(
[
    {"title": "Task 1", "description": "Description 1", "due_date": "2023-05-01", "completed": False},
    {"title": "Task 2", "description": "Description 2", "due_date": "2023-05-02", "completed": False},
    {"title": "Task 3", "description": "Description 3", "due_date": "2023-05-03", "completed": False},
])

edited_df = st.data_editor(df, num_rows="dynamic", height=200, width=900)

# Filter DataFrame by completed tasks
filter_completed = st.radio("Filter by Completed", ["All", "True", "False"])
if filter_completed == "True":
    filtered_df = edited_df[edited_df["completed"] == True]
    st.write(filtered_df)
elif filter_completed == "False":
    filtered_df = edited_df[edited_df["completed"] == False]
    st.write(filtered_df)
else:
    st.write(edited_df)

# Filter DataFrame by title
filter_title = st.text_input("Filter by Title")
if filter_title:
    filtered_df = edited_df[edited_df["title"].str.contains(filter_title)]
    st.write(filtered_df)

# Filter DataFrame by description
filter_description = st.text_input("Filter by Description")
if filter_description:
    filtered_df = edited_df[edited_df["description"].str.contains(filter_description)]
    st.write(filtered_df)

# Filter DataFrame by due date
due_date_filter = st.date_input("Filter by Due Date", None)
if due_date_filter:
    due_date_filter = due_date_filter.strftime("%Y-%m-%d")
    filtered_df = edited_df[edited_df['due_date'] == due_date_filter]
    st.write(filtered_df)

# Sort DataFrame by due date
sort_by_due_date = st.checkbox("Sort by Due Date descending")
if sort_by_due_date:
    sorted_df = edited_df.sort_values(by="due_date", ascending=False)
    st.write(sorted_df)



