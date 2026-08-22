import streamlit as st
import pandas as pd
from data import AUGUST_PAYMENTS, RULES

st.set_page_config(page_title="PEXNA 94 - Secure Njangui Platform", page_icon="🎓", layout="wide")

# Simple Password Gate for GDPR Compliance
password = st.sidebar.text_input("Enter Batch Password to Access", type="password")
if password != "pexna94_secure":
    st.warning("🔒 This directory is password-protected for GDPR compliance. Please enter the authorized batch password.")
    st.stop()

# --- Navigation ---
st.sidebar.title("Menu")
page = st.sidebar.radio("Navigate", ["Home", "August Njangui Ledger", "Contact Us", "Privacy Policy", "French"])

df_payments = pd.DataFrame(AUGUST_PAYMENTS)
total_collected = df_payments["amount_xaf"].sum()

if page == "Home":
    st.title("African Tradition Meets Modern Finance")
    st.subheader("Digitize your PEXNA 94 Njangui experience. Manage cycles, sessions, savings, loans, and group activities securely.")

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📊 Group Dashboard")
        st.write("Easily view balances and manage all Njangi groups in one place.")
    with col2:
        st.markdown("### 🔄 Automated Cycles")
        st.write("Njangi cycles start and manage themselves based on configured schedules.")
    with col3:
        st.markdown("### 💬 In-App Messaging")
        st.write("Chat with members, send private messages, and get 48-hour automated reminders.")

    st.markdown("---")
    st.subheader("PEXNA 94 Guidelines & Penalty Framework Highlights")
    st.write(f"- **Slot Contribution:** Fixed at {RULES['slot_amount']:,} XAF per hand (Maximum {RULES['max_hands']} hands per member).")
    st.write(f"- **Contribution Schedule:** {RULES['schedule']}.")
    st.write(f"- **Late Fee Penalty:** {int(RULES['late_fee_percentage']*100)}% of the missed outstanding contribution.")
    st.write(f"- **Suspension Rule:** After {RULES['suspension_limit']} missed payments, suspension from payouts applies.")

    st.markdown("---")
    st.subheader("Behind The App")
    st.markdown("**Dr. ATEH Thomson Pepeah** — *Founder | Lawyer*")
    st.write("Husband, lawyer, and university lecturer specializing in Economics, Corporate, Labour, Business Law, and IP.")
    
    st.markdown("**Kamga Simo Junior** — *Senior Full Stack Engineer | Systems Analyst | Design Enthusiast*")
    st.write("Senior Full Stack Engineer blending code with creativity to build smart, scalable digital solutions.")
    
    st.markdown("---")
    st.markdown("🌐 **Website:** [frankfru.com](https://frankfru.com)")
    st.markdown("🔗 **LinkedIn:** [Frank Fru on LinkedIn](https://www.linkedin.com/in/frank-fru/)")

elif page == "August Njangui Ledger":
    st.title("August 2006 Njangui Payment Ledger")
    st.write("Confirmed contributions for the August Njangui cycle.")
    
    st.metric(label="Total August Collections (XAF)", value=f"{total_collected:,} XAF")
    
    st.markdown("---")
    st.dataframe(df_payments, use_container_width=True)

elif page == "Contact Us":
    st.title("Contact Us")
    st.write("Get in touch with the PEXNA 94 administration team.")
    st.text_input("Your Name")
    st.text_input("Your Email / WhatsApp")
    st.text_area("Your Message")
    st.button("Send Message")

elif page == "Privacy Policy":
    st.title("Privacy Policy")
    st.write("Your data, KYC details, and transaction histories are protected under strict transparency and member consent guidelines.")

elif page == "French":
    st.title("Bienvenue sur PEXNA 94")
    st.write("Numérisez votre expérience Njangi. Gérez les cycles, les sessions, l'épargne et les prêts en toute sécurité.")

st.sidebar.markdown("---")
st.sidebar.text("© 2026 PEXNA 94. All rights reserved.")
