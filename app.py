import streamlit as st
import os

# Create a directory to store uploaded files
UPLOAD_DIRECTORY = "uploads"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# Function to handle user authentication
def authenticate_user(username, password):
    # Dummy authentication (replace with actual authentication logic)
    return username == "admin" and password == "admin123"

# Function to handle user signup
def signup_user(name, roll_number, phone_number, email, password):
    # Here you would typically connect to your database and insert the user information
    # For the sake of this example, we'll just print the user details
    st.success("Signup successful!")
    st.write("Name:", name)
    st.write("Roll Number:", roll_number)
    st.write("Phone Number:", phone_number)
    st.write("Email:", email)

# Function to handle file upload along with description
def upload_file_with_description(file, description):
    file_path = os.path.join(UPLOAD_DIRECTORY, file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    description_file_path = os.path.join(UPLOAD_DIRECTORY, f"{file.name}.txt")
    with open(description_file_path, "w") as f:
        f.write(description)
    st.success(f"File uploaded successfully: {file.name}")

import streamlit as st
import os

# Function to display uploaded files with descriptions
def display_uploaded_files_with_description():
    files = os.listdir(UPLOAD_DIRECTORY)
    if files:
        st.subheader("Uploaded Files:")
        for file in files:
            if not file.endswith(".txt"):
                st.write("File Name:", file)
                description_file_path = os.path.join(UPLOAD_DIRECTORY, f"{file}.txt")
                if os.path.exists(description_file_path):
                    with open(description_file_path, "r") as f:
                        description = f.read()
                    st.write("Description:", description)
                    
                    # Check if the file is an image
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        # Display image
                        st.image(os.path.join(UPLOAD_DIRECTORY, file), caption=description, use_column_width=True)
                else:
                    st.write("No description available.")
    else:
        st.write("No files uploaded.")


# Main function
def main():
    st.title("Student Management System")

    page = st.sidebar.radio("Navigation", ["Login", "Signup", "Home"])

    if page == "Login":
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate_user(username, password):
                st.success("Login successful!")
                st.session_state.logged_in = True
            else:
                st.error("Invalid username or password")

    elif page == "Signup":
        st.title("Signup")
        name = st.text_input("Name")
        roll_number = st.text_input("Roll Number")
        phone_number = st.text_input("Phone Number")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Sign Up"):
            signup_user(name, roll_number, phone_number, email, password)

    elif page == "Home":
        if st.session_state.get("logged_in"):
            st.title("Home")
            st.subheader("Upload File")
            file = st.file_uploader("Upload your file", type=["pdf", "png", "jpg", "jpeg"])
            description = st.text_area("Description")
            if file:
                upload_file_with_description(file, description)
            st.subheader("View Uploaded Files")
            if st.button("View"):
                display_uploaded_files_with_description()
        else:
            st.write("Please login to access the system.")

if _name_ == "_main_":
    main()