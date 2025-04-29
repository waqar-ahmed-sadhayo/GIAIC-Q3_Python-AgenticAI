import streamlit as st
import re

# Title of the App
st.title("🔐 Ultimate Password Strength Checker")

# 📃 Descriptions
st.markdown("""
Welcome to **Ultimate Password Strength Checker!**
Ensure your password is secured by checking:
- ✅ Length
- ✅ Upper and Lower case
- ✅ Special characters
- ✅ Numbers

> ⚡ *Improve your online security by creating 💪 strong password!*
""")

# 🏷️ Input field
password = st.text_input("🔑 Enter your password: ", type = "password")

# 🔍 Password Strength Check
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    # Special Characters Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (!@#$%^&*)**.")

    # Uppercase and Lowercase Letters Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both **uppercase and lowercase** letters.")

    # Digits Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least **one number (0-9)**.")

    return score, feedback

# ✅ Button to Check Password
if st.button("🔍 Check Password Strength"):
    score, feedback = check_password_strength(password)

    if password:
        st.subheader("🔒 Password strength result:")

        if score == 4:
            st.success("✅ Strong Password! Your password is secure.")
        elif score == 3:
            st.warning("⚠ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using suggestion below.")

        if feedback:
            st.info("Suggestions to improve your password")
            for tip in feedback:
                st.write(tip)
    else:
        st.write("🚨 Please enter a password to check")

# Footer
st.markdown("""
    ---
    Developed with 💖 by **Waqar Ahmed Sadhayo**
    """)
