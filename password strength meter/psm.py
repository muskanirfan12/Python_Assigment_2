import re
import random
import string
import streamlit as st

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    score = 0
    common_passwords = ["password", "123456", "qwerty", "password123", "admin", "letmein"]
    
    if password in common_passwords:
        st.error("❌ **This password is too common. Choose a more secure one.**")
        return "Weak"
    
    if len(password) >= 8:
        score += 1
    else:
        st.warning("❌ **Password should be at least 8 characters long.**")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.warning("❌ **Include both uppercase and lowercase letters.**")
    
    if re.search(r"\d", password):
        score += 1
    else:
        st.warning("❌ **Add at least one number (0-9).**")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.warning("❌ **Include at least one special character (!@#$%^&*).**")
    
    st.markdown("---")
    
    if score == 4:
        st.success("✅ **Strong Password! 🎉 Great job securing your account!**")
        return "Strong"
    elif score == 3:
        st.info("⚠️ **Moderate Password - Consider adding more security features.**")
        return "Moderate"
    else:
        st.error("❌ **Weak Password - Improve it using the suggestions above.**")
        st.info(f"💡 **Suggested Strong Password:** ✨ `{generate_strong_password()}` ✨")
        return "Weak"

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter By Muskan Irfan Ahmed✨ ")

st.markdown("""
### 🔎 Check Your Password Strength!
- ✅ **Strong passwords** are safe to use.
- ⚠️ **Moderate passwords** need extra security.
- ❌ **Weak passwords** get improvement suggestions.
---
""", unsafe_allow_html=True)

password = st.text_input("💡 **Enter your password:**", type="password")
if password:
    check_password_strength(password)
