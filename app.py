import streamlit as st

# Dummy Login-Daten
USER = "admin"
PASSWORD = "1234"

# Alle Länder der Welt (ISO-Liste)
COUNTRIES = [
    "Afghanistan", "Ägypten", "Albanien", "Algerien", "Andorra", "Angola", "Antigua und Barbuda", "Argentinien",
    "Armenien", "Australien", "Österreich", "Aserbaidschan", "Bahamas", "Bahrain", "Bangladesch", "Barbados",
    "Weißrussland", "Belgien", "Belize", "Benin", "Bhutan", "Bolivien", "Bosnien und Herzegowina", "Botswana",
    "Brasilien", "Brunei", "Bulgarien", "Burkina Faso", "Burundi", "Kambodscha", "Kamerun", "Kanada", "Kap Verde",
    "Zentralafrikanische Republik", "Tschad", "Chile", "China", "Kolumbien", "Komoren", "Kongo", "Costa Rica",
    "Kroatien", "Kuba", "Zypern", "Tschechien", "Dänemark", "Dschibuti", "Dominica", "Dominikanische Republik",
    "Ecuador", "El Salvador", "Äquatorialguinea", "Eritrea", "Estland", "Eswatini", "Äthiopien", "Fidschi",
    "Finnland", "Frankreich", "Gabun", "Gambia", "Georgien", "Deutschland", "Ghana", "Griechenland", "Grenada",
    "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Ungarn", "Island", "Indien", "Indonesien",
    "Iran", "Irak", "Irland", "Israel", "Italien", "Jamaika", "Japan", "Jordanien", "Kasachstan", "Kenia", "Kiribati",
    "Nordkorea", "Südkorea", "Kuwait", "Kirgisistan", "Laos", "Lettland", "Libanon", "Lesotho", "Liberia", "Libyen",
    "Liechtenstein", "Litauen", "Luxemburg", "Madagaskar", "Malawi", "Malaysia", "Malediven", "Mali", "Malta",
    "Marshallinseln", "Mauretanien", "Mauritius", "Mexiko", "Mikronesien", "Moldawien", "Monaco", "Mongolei",
    "Montenegro", "Marokko", "Mosambik", "Myanmar", "Namibia", "Nauru", "Nepal", "Niederlande", "Neuseeland",
    "Nicaragua", "Niger", "Nigeria", "Nordmazedonien", "Norwegen", "Oman", "Pakistan", "Palau", "Panama",
    "Papua-Neuguinea", "Paraguay", "Peru", "Philippinen", "Polen", "Portugal", "Katar", "Rumänien", "Russland",
    "Ruanda", "St. Kitts und Nevis", "St. Lucia", "St. Vincent und die Grenadinen", "Samoa", "San Marino",
    "Sao Tomé und Príncipe", "Saudi-Arabien", "Senegal", "Serbien", "Seychellen", "Sierra Leone", "Singapur",
    "Slowakei", "Slowenien", "Salomonen", "Somalia", "Südafrika", "Südsudan", "Spanien", "Sri Lanka", "Sudan",
    "Suriname", "Schweden", "Schweiz", "Syrien", "Taiwan", "Tadschikistan", "Tansania", "Thailand", "Timor-Leste",
    "Togo", "Tonga", "Trinidad und Tobago", "Tunesien", "Türkei", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
    "Vereinigte Arabische Emirate", "Großbritannien", "USA", "Uruguay", "Usbekistan", "Vanuatu", "Vatikanstadt",
    "Venezuela", "Vietnam", "Jemen", "Sambia", "Simbabwe"
]

# Session-Status prüfen
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "dashboard"
if "kunden" not in st.session_state:
    st.session_state.kunden = []

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

def dashboard():
    st.image("https://notebook-repair-corner.at/wp-content/uploads/2022/03/nrc-logo-1.png", width=200)
    st.title("📊 NRC-CRM Dashboard")
    st.write("Willkommen bei deinem NRC Notebook Repair Corner CRM!")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Neuer Servicefall"):
            st.session_state.page = "neuer_servicefall"
        if st.button("🔧 Alle Reparaturen"):
            st.session_state.page = "alle_reparaturen"
        if st.button("✅ Beendete Reparaturen"):
            st.session_state.page = "beendete_reparaturen"
    with col2:
        if st.button("📊 Übersicht"):
            st.session_state.page = "uebersicht"
        if st.button("🕒 Offene Reparaturen"):
            st.session_state.page = "offene_reparaturen"
        if st.button("💰 Heutiger Umsatz"):
            st.session_state.page = "umsatz"

def neuer_servicefall():
    st.title("➕ Neuer Servicefall")
    st.write("Erfasse hier die Kundendaten für einen neuen Servicefall:")

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
        st.success(f"Servicefall für '{name}' gespeichert ✅")

    if st.button("🔙 Zurück zum Dashboard"):
        st.session_state.page = "dashboard"

def alle_reparaturen():
    st.title("🔧 Alle Reparaturen")
    st.write("Hier werden später alle Reparaturfälle angezeigt.")
    if st.button("🔙 Zurück zum Dashboard"):
        st.session_state.page = "dashboard"

# App starten
if not st.session_state.logged_in:
    login()
else:
    if st.session_state.page == "dashboard":
        dashboard()
    elif st.session_state.page == "neuer_servicefall":
        neuer_servicefall()
    elif st.session_state.page == "alle_reparaturen":
        alle_reparaturen()
    else:
        dashboard()
