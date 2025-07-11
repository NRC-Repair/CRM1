import streamlit as st

# NRC-Farben
PRIMARY = "#1B3556"   # NRC Blau
ACCENT = "#F7C843"    # NRC Gold
BG_OVERLAY = "rgba(27,53,86,0.82)"  # halbtransparentes Blau

# NRC Logo und Hintergrund
NRC_LOGO_URL = "https://notebook-repair-corner.at/wp-content/uploads/2022/03/nrc-logo-1.png"
NRC_BG_URL = "https://notebook-repair-corner.at/wp-content/uploads/2022/03/nrc-background-dark-blur2.png"

# Dummy Login-Daten
USER = "admin"
PASSWORD = "1234"

# Alle Länder der Welt
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

# === NRC DESIGN: Global CSS ===
st.markdown(
    f"""
    <style>
        body, .stApp {{
            background: url({NRC_BG_URL}) no-repeat center center fixed;
            background-size: cover;
        }}
        .nrc-overlay {{
            background: {BG_OVERLAY};
            border-radius: 24px;
            padding: 2.5rem 2rem 2rem 2rem;
            margin-top: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 6px 32px 0 rgba(20,40,80,0.25);
            max-width: 560px;
            margin-left: auto;
            margin-right: auto;
        }}
        .nrc-btn button {{
            background: linear-gradient(90deg, {ACCENT} 50%, {PRIMARY} 100%) !important;
            color: #142238 !important;
            border-radius: 1.5rem !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            margin-bottom: 0.5rem !important;
        }}
        .stTextInput > div > input, .stTextArea > div > textarea, .stSelectbox > div > div {{
            background: #eef4fa77;
            color: #222;
            border-radius: 0.8rem;
        }}
        .stTable, .stDataFrame {{
            background: #fff8;
            border-radius: 1.2rem;
        }}
        .stAlert {{
            border-radius: 1rem !important;
        }}
        .stSuccess, .stError, .stInfo {{
            font-size: 1.09rem;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Session-Status prüfen
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "dashboard"
if "kunden" not in st.session_state:
    st.session_state.kunden = []

def login():
    st.image(NRC_LOGO_URL, width=180)
    st.markdown(f'<div class="nrc-overlay">', unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:{ACCENT}; margin-bottom:1.5rem; text-align:center;'>🔐 NRC-CRM Login</h2>", unsafe_allow_html=True)
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    if st.button("Login", key="login", help="Mit deinen Zugangsdaten anmelden"):
        if username == USER and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login erfolgreich ✅")
        else:
            st.error("❌ Falsche Login-Daten")
    st.markdown("</div>", unsafe_allow_html=True)

def dashboard():
    st.image(NRC_LOGO_URL, width=180)
    st.markdown(f'<div class="nrc-overlay">', unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:{ACCENT};text-align:center'>📊 NRC-CRM Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.write("Willkommen bei deinem **NRC Notebook Repair Corner CRM!** Wähle eine Aktion aus:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Neuer Servicefall", key="btn-neu"):
            st.session_state.page = "neuer_servicefall"
        if st.button("🔧 Alle Reparaturen", key="btn-alle"):
            st.session_state.page = "alle_reparaturen"
        if st.button("✅ Beendete Reparaturen", key="btn-beendet"):
            st.session_state.page = "beendete_reparaturen"
    with col2:
        if st.button("📊 Übersicht", key="btn-ueber"):
            st.session_state.page = "uebersicht"
        if st.button("🕒 Offene Reparaturen", key="btn-offen"):
            st.session_state.page = "offene_reparaturen"
        if st.button("💰 Heutiger Umsatz", key="btn-umsatz"):
            st.session_state.page = "umsatz"
    st.markdown("</div>", unsafe_allow_html=True)

def neuer_servicefall():
    st.image(NRC_LOGO_URL, width=180)
    st.markdown(f'<div class="nrc-overlay">', unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:{ACCENT};text-align:center'>➕ Neuer Servicefall</h2>", unsafe_allow_html=True)
    st.write("Erfasse hier die Kundendaten für einen neuen Servicefall:")

    name = st.text_input("Name")
    email = st.text_input("E-Mail")
    phone = st.text_input("Telefon")
    company = st.text_input("Firma (optional)")
    street = st.text_input("Straße & Hausnummer")
    postal_code = st.text_input("PLZ")
    city = st.text_input("Ort")
    country = st.selectbox("Land", COUNTRIES)

    if st.button("Speichern", key="btn-save"):
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

    if st.button("🔙 Zurück zum Dashboard", key="btn-back"):
        st.session_state.page = "dashboard"
    st.markdown("</div>", unsafe_allow_html=True)

def alle_reparaturen():
    st.image(NRC_LOGO_URL, width=180)
    st.markdown(f'<div class="nrc-overlay">', unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:{ACCENT};text-align:center'>🔧 Alle Reparaturen</h2>", unsafe_allow_html=True)
    if st.session_state.kunden:
        st.write("**Gespeicherte Servicefälle:**")
        st.table(st.session_state.kunden)
    else:
        st.info("Noch keine Servicefälle erfasst.")
    if st.button("🔙 Zurück zum Dashboard", key="btn-back2"):
        st.session_state.page = "dashboard"
    st.markdown("</div>", unsafe_allow_html=True)

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
