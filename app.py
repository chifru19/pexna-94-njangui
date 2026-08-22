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
    st.subheader("Digitize your Njangi experience. Manage cycles, sessions, savings, loans, and group activities all in one secure and user-friendly mobile app.")

    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📊 Group Dashboard & Balance Overview")
        st.write("Easily view your current balance and manage all your Njangi groups in one place.")
        
        st.markdown("### 🔄 Automated Njangi Cycles")
        st.write("Njangi cycles start and manage themselves based on your configured settings.")
        
        st.markdown("### 💬 In-App Group Messaging")
        st.write("Chat with members, send private messages, and share important updates in real-time.")
        
        st.markdown("### 📈 Detailed Transaction History")
        st.write("Track every deposit, withdrawal, and platform fee with full transparency.")
        
        st.markdown("### 💡 Smart Savings & Profit Tracking")
        st.write("See how much you've saved, withdrawn, and the profits earned—automatically calculated.")
        
    with col2:
        st.markdown("### 🏦 Loan Requests & Repayments")
        st.write("Request, approve, and repay group loans with a streamlined, secure workflow.")
        
        st.markdown("### ⏱️ Build Njangi Groups in Seconds")
        st.write("Create and customize your Njangi cycles with just a few taps.")
        
        st.markdown("### 🛠️ Built-in Group Tools")
        st.write("Showcase your group’s finances, chat, and sessions—no extra software needed.")
        
        st.markdown("### ⚡ Smart Interface & Real-Time Communication")
        st.write("Enjoy intuitive design and connect instantly with group members through chats and updates.")
        
        st.markdown("### 🚀 Powerful All-in-One Njangi App")
        st.write("From contributions to cashouts, Njangi simplifies traditional savings with modern tech.")

    st.markdown("---")
    st.subheader("Why Choose Njangi?")
    st.write("- **Instant Setup & Smart Group Management**")
    st.write("- **Enhanced Security with KYC**")
    st.write("- **Built-in Group Communication**")
    st.write("- **Transparent Finances & Personal Savings**")
    st.write("- **Njangi Bank – Personal Savings Made Easy**")
    st.write("- **Njangi Backmarket – Post & Discover Services**")
    st.write("- **Lotto Draws – Win Cash Every Day**")
    st.write("- **Trouble Funds – Community in Times of Need**")
    st.write("- **Njangi Advertisement – Promote Inside Your Groups**")

    st.markdown("---")
    st.subheader("Ready to Transform Your Njangi?")
    st.write("Download Njangi today and unlock a smarter way to save, lend, and grow together.")
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
st.sidebar.text("© 2026 PEXNA 94. All rights reserved. Empowering community savings through digital innovation.")
