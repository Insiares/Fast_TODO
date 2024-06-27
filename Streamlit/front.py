import streamlit as st
import pandas as pd

# User credentials (for simplicity, we use a dictionary; in a real app, use a database)
USER_CREDENTIALS = [{
    "id": 1,
    "user": "jojo",
    "password": "hello",
},
{
    "id": 2,
    "user": "boris",
    "password": "hello2",
}]


# Function to check if user is logged in
def is_logged_in():
    if "user" in st.session_state:
        return True

# Function to authenticate user
def authenticate(username, password):
    # Check if username and password match
    for USER_CREDENTIAL in USER_CREDENTIALS:
        if username in USER_CREDENTIAL['user'] and USER_CREDENTIAL['password'] == password:
            st.session_state["user"] = USER_CREDENTIAL
            return True

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


if is_logged_in():
    st.title("Gestionnaire de taches")
    # Create DataFrame

    df = pd.DataFrame(
    [
        {"title": "Task 1", "description": "Description 1", "due_date": "2023-05-01", "completed": False},
        {"title": "Task 2", "description": "Description 2", "due_date": "2023-05-02", "completed": False},
        {"title": "Task 3", "description": "Description 3", "due_date": "2023-05-03", "completed": False},
    ])

    # Convert "due_date" column to datetime
    df["due_date"] = pd.to_datetime(df["due_date"]).dt.date

    # Vérifier si le dictionnaire contient des valeurs non vides
    def non_empty_values(dictionary):
        for value in dictionary.values():
            if value:
                return True
        return False

    # Filter with selectbox
    filter = st.selectbox("Filter by title, description, due date or completed", ["all", "title", "description", "due_date", "completed"])
    if filter == "all":
        # Display all tasks
        df = st.data_editor(df, num_rows="dynamic", key="crud", height=200, width=900)
        # Get an updated version of the DataFrame
        df_updated = st.session_state["crud"]
        # Check if any rows were edited
        if non_empty_values(df_updated["edited_rows"]): 
            # Update the DataFrame
            task_id = list(df_updated["edited_rows"].keys())[0]
            user_id = st.session_state["user"]["id"]
            if "title" in df_updated["edited_rows"][task_id]:
                title = df_updated["edited_rows"][task_id]["title"]
            if "description" in df_updated["edited_rows"][task_id]:
                description = df_updated["edited_rows"][task_id]["description"]
            if "due_date" in df_updated["edited_rows"][task_id]:
                due_date = df_updated["edited_rows"][task_id]["due_date"]
            if "completed" in df_updated["edited_rows"][task_id]:
                completed = df_updated["edited_rows"][task_id]["completed"]
            print(user_id)
        
    elif filter == "title":
        # Filter DataFrame by title
        filter_title = st.text_input("Filter by Title")
        if filter_title:
            filtered_df = df[df["title"].str.contains(filter_title)]
            st.dataframe(filtered_df)
    elif filter == "description":
        # Filter DataFrame by description
        filter_description = st.text_input("Filter by Description")
        if filter_description:
            filtered_df = df[df["description"].str.contains(filter_description)]
            st.dataframe(filtered_df)
    elif filter == "due_date":
        # Filter DataFrame by due date
        due_date_filter = st.date_input("Filter by Due Date", None)
        if due_date_filter:
            filtered_df = df[df['due_date'] == due_date_filter]
            st.dataframe(filtered_df)
    elif filter == "completed":
        # Filter DataFrame by completed tasks
        filter_completed = st.radio("Filter by Completed", ["True", "False"], index=None)
        if filter_completed:
            filtered_df = df[df["completed"] == True]
            st.dataframe(filtered_df)
        else:
            filtered_df = df[df["completed"] == False]
            st.dataframe(filtered_df)


      
# Optionally, add a sign-up section (not secure, just for demonstration)
st.write("Don't have an account? Sign up here:")
if st.button("Register", key="register"):
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








