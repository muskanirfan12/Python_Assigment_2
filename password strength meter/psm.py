import re
import streamlit as st

#page styling:
st.set_page_config(page_title="Password Strength Meter", page_icon="🌘", layout="centered")

#custom css
st.markdown(
    """
    <style>
    .main{text-align: center;}
    .stTextInput{ width: 60% !important, margin: auto;}
    .stButton button{ width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
    .stButton button:hover { background-color: #45a049;}
    </style>
    """,
    unsafe_allow_html=True
)

#page title and Description
st.title("🔐Password Strength Generator")
st.write("Enter your password to check its strength and get suggestions for improvement. 🔍 ")

#function to check password strength
def check_password_strength(password):
    score = 0,
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌Password should be **at least 8 character long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should include  **both uppercase (A-Z) and one lowercase (a-z) letter**.")

    if re.search(r"\d", password):
        score += 1
    else:
         feedback.append("❌Password should include  **at least one number (0-9)**.")

    #special characters
    if re.search(r"[!@#$%^&*]", password):
         score += 1
    else:
        feedback.append("❌Password should include  **at least one special character (!@#$%^&*)**.")
       
    #display password strength result
    if score == 4:
        st.success("🔥 **Strong Pasword** . Your Password is secure.")
        
    elif score == 3:
        st.warning("⚠️ **Moderate Password** . Consider security improving by adding more features.")

    else:
        st.error("🚨 **Weak Password** . Follow the suggestion below to strength it.")

#feedback
    if feedback:
        with st.expander("🔍 **Improve your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your Password:", type="password", help="Enter your Password is strong🔐")

#Button working
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning(" ⚠️ Please enter your password first!.") #show warning if password empty
