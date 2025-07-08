import streamlit as st

# Dummy Login-Daten
USER = "admin"
PASSWORD = "1234"

# Länder-Liste (abgekürzt, aber du bekommst gleich ALLE)
COUNTRIES = [
    "Österreich", "Deutschland", "Schweiz", "Türkei", "Bosnien und Herzegowina",
    "Frankreich", "Italien", "USA", "Kanada", "China", "Japan", "Alle Länder der Welt …"
]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 NRC-CRM Login")
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    if st.button("Login"):
        if username == USER and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login erfolgreich ✅")
        else:
            st.error("❌ Falsche Login-Daten")

def kundenverwaltung():
    st.title("📋 NRC Kundenverwaltung")
    if "kunden" not in st.session_state:
        st.session_state.kunden = []

    st.header("➕ Neuen Kunden anlegen")
    name = st.text_input("Name")
    email = st.text_input("E-Mail")
    phone = st.text_input("Telefon")
    company = st.text_input("Firma (optional)")
    street = st.text_input("Straße & Hausnummer")
    postal_code = st.text_input("PLZ")
    city = st.text_input("Ort")
    country = st.selectbox("Land", COUNTRIES)
    
    if st.button("Speichern"):
        st.session_state.kunden.append({
            "Name": name,
            "E-Mail": email,
            "Telefon": phone,
            "Firma": company,
            "Straße": street,
            "PLZ": postal_code,
            "Ort": city,
            "Land": country
        })
        st.success(f"Kunde '{name}' gespeichert ✅")

    st.header("📑 Alle Kunden")
    for kunde in st.session_state.kunden:
        st.write(f"👤 **{kunde['Name']}**")
        st.write(f"📧 {kunde['E-Mail']} | 📞 {kunde['Telefon']} | 🏢 {kunde['Firma']}")
        st.write(f"🏠 {kunde['Straße']}, {kunde['PLZ']} {kunde['Ort']}, {kunde['Land']}")

if not st.session_state.logged_in:
    login()
else:
    kundenverwaltung()
