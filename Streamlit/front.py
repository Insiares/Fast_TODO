import streamlit as st

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

if st.button("Sign Up"):
    if new_password == confirm_password:
        if new_username in USER_CREDENTIALS:
            st.warning("Username already exists. Please choose a different username.")
        else:
            USER_CREDENTIALS[new_username] = new_password
            st.success("Account created successfully! You can now log in.")
    else:
        st.error("Passwords do not match. Please try again.")
