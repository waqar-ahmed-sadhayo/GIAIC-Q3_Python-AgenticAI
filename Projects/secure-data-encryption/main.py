import streamlit as st
from cryptography.fernet import Fernet # For symmetric encryption/decryption
import hashlib  # For hashing passkeys securely
import json  # For reading/writing JSON files
import os   # For file path checking
import time


# File paths for persistent data storage
DATA_FILE = 'secure_data.json'   # File paths for persistent data storage
ATTEMPTS_FILE = 'attempts.json'  # Stores failed login attempts per user


# Load stored encrypted data from JSON file or return empty dict
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save encrypted data to JSON file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Load login attempt counts from JSON file
def load_attempts():
    if os.path.exists(ATTEMPTS_FILE):
        with open(ATTEMPTS_FILE, "r") as f:
           return json.load(f)
    return {}

# Save failed login attempts to JSON file
def save_attempts(attempts):
    with open(ATTEMPTS_FILE, "w") as f:
        json.dump(attempts, f)



# Initialize session state on first run
if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()  # Generate new encryption key

if "authorized" not in st.session_state:
    st.session_state.authorized = True  # User is initially authorized

# Create Fernet object with session key
fernet = Fernet(st.session_state.fernet_key)

# Load data and attempts from JSON
stored_data = load_data()
failed_attempts = load_attempts()


# Hash passkey using SHA256 (used for verification)
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()


# Encrypt and store user data with hashed passkey
def insert_data(user_id, text, passkey):
    encrypted_text = fernet.encrypt(text.encode()).decode()  # Encrypt the data
    hashed_passkey = hash_passkey(passkey)  # Hash the passkey for secure storage
    stored_data[user_id] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
    save_data(stored_data)   # Save to JSON
    st.success(f"Data stored securely for user: {user_id}")


# Decrypt user data if correct passkey is provided
def retrieve_data(user_id, passkey):
    if user_id not in stored_data:
        st.error("No data found for this user.")
        return


    # Check if user has exceeded allowed attempts
    if failed_attempts.get(user_id, 0) >= 3:
        st.session_state.authorized = False
        st.warning("Too many failed attempts. Redirecting to login.")
        time.sleep(1)
        st.rerun()  # Redirect to login page
        return

    hashed_input = hash_passkey(passkey)

    # Check if hashed passkey matches stored hash
    if hashed_input == stored_data[user_id]["passkey"]:
        try:
            decrypted = fernet.decrypt(stored_data[user_id]["encrypted_text"].encode()).decode()
            st.success(f"Decrypted Data: {decrypted}")
            failed_attempts[user_id] = 0   # Reset attempt counter on success
            save_attempts(failed_attempts)
        except Exception as e:
            st.error("Error while decrypting. Possibly incorrect key.")
    else:
        # Increment failed attempt counter
        failed_attempts[user_id] = failed_attempts.get(user_id, 0) + 1
        save_attempts(failed_attempts)
        attempts_left = 3 - failed_attempts[user_id]
        st.error(f"Incorrect passkey. Attempts left: {attempts_left}")


# Set page configuration for Streamlit
st.set_page_config(page_title="🔐 CryptoVaul", layout="wide")


# Admin Login page
def login_page():
    st.title("🔐 Reauthorization Required")
    username = st.text_input("Enter Admin Username")
    password = st.text_input("Enter Admin Password", type="password")

    if st.button("Login"):
        # Check if credentials are correct
        if username == "admin" and password == "admin123":
            st.session_state.authorized = True
            failed_attempts.clear()   # Clear all failed attempts after admin login
            save_attempts(failed_attempts)
            st.success("Login successful! Redirecting...")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Invalid credentials.")

# Main App Logic
def main():
    # Redirect unauthorized users to login page
    if not st.session_state.get("authorized", True):
        login_page()
        return

    # Sidebar navigation
    st.sidebar.title("🔐 Secured Data Storage")
    menu = st.sidebar.radio("Navigate", ["Home", "Insert Data", "Retrieve Data", "Login"])

    # Home screen
    if menu == "Home":
        st.title("Welcome to Secure Data Encryption System 🔐")
        st.write("Use the sidebar to insert or retrieve encrypted data 🛠️📁.")


    # Insert Data Page
    elif menu == "Insert Data":
        st.title("📥 Store Your Secure Data")
        user_id = st.text_input("Enter User ID")
        data = st.text_input("Enter Data to Encrypt")
        passkey = st.text_input("Set a Passkey", type="password")

        if st.button("Store Data"):
            if user_id and data and passkey:
                insert_data(user_id, data, passkey)
            else:
                st.warning("All fields are required.")


    # Retrieve Data Page
    elif menu == "Retrieve Data":
        st.title("🔓 Retrieve Your Encrypted Data")
        user_id = st.text_input("Enter User ID")
        passkey = st.text_input("Enter Passkey", type="password")

        if st.button("Decrypt Data"):
            if user_id and passkey:
                retrieve_data(user_id, passkey)
            else:
                st.warning("Both Username and Passkey are required.")

    # Admin Login Page
    elif menu == "Login":
        login_page()


    # Footer
    st.markdown("""
        ---
        Developed with 💖 by **Waqar Ahmed Sadhayo**
        """)

# Run the main app when script is executed
if __name__ == "__main__":
    main()