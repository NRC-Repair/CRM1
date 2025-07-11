import streamlit as st

# Farben & Branding
PRIMARY = "#F7C843"     # NRC Gold
BG_COLOR = "#111111"    # Tiefschwarz
TEXT_COLOR = "#ffffff"  # Weiß
NRC_LOGO_URL = "https://notebook-repair-corner.at/wp-content/uploads/2022/03/nrc-logo-1.png"

USER, PASSWORD = "admin", "1234"
COUNTRIES = [
    "Österreich", "Deutschland", "Schweiz", "Türkei", "USA", "Frankreich", "Italien", "Spanien", "England",
    "Polen", "Ungarn", "Kroatien", "Griechenland", "Niederlande", "Rumänien", "Serbien", "Bulgarien", "Dänemark",
    "Tschechien", "Slowakei", "Slowenien", "Belgien", "Luxemburg", "Norwegen", "Finnland", "Schweden", "Portugal"
    # beliebig erweiterbar!
]

# ------------- Modern Dark Apple-Style CSS -------------
st.markdown(f"""
<style>
body, .stApp {{
    background: {BG_COLOR} !important;
    color: {TEXT_COLOR} !important;
    font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
}}
.nrc-overlay {{
    background: rgba(20,20,22,0.93);
    border-radius: 22px;
    padding: 2.3rem 2.3rem 1.7rem 2.3rem;
    max-width: 540px;
    margin: 2rem auto 2rem auto;
    box-shadow: 0 8px 36px 0 rgba(0,0,0,0.32);
    color: {TEXT_COLOR};
}}
h1, h2, h3, h4, h5, h6, .stHeader, .stTitle, .stMarkdown, label, p, span, .stAlert, .stTable, .stDataFrame {{
    color: {TEXT_COLOR} !important;
}}
input, select, textarea {{
    background: #222 !important;
    color: {TEXT_COLOR} !important;
    border: 1.3px solid #444;
    border-radius: 13px;
    padding: 0.7rem;
    font-size: 1.07rem;
    margin-bottom: 0.15rem;
}}
input:focus, select:focus, textarea:focus {{
    outline: none;
    border-color: {PRIMARY};
    box-shadow: 0 0 0 3px rgba(247,200,67,0.13);
    background: #222 !important;
}}
.stButton>button, .stDownloadButton>button {{
    background-color: {PRIMARY};
    color: #222 !important;
    border-radius: 12px;
    padding: 0.7rem 1.15rem;
    font-size: 1.07rem;
    font-weight: 700;
    box-shadow: 0 2px 6px rgba(30,25,5,0.19);
    border: none;
    margin-top: 0.3rem;
}}
.stButton>button:hover {{
    background-color: #fffbe2;
    color: #111 !important;
}}
.error-field {{
    border-color: #e53935 !important;
    box-shadow: 0 0 0 2px rgba(229,57,53,0.15);
    background: #402020 !important;
}}
.stAlert {{
    border-radius: 13px;
}}
/* Logo oben mittig */
.nrc-logo {{
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 0.5rem;
    margin-bottom: 1.0rem;
    width: 128px;
}}
.yurt-header {{
    color: {TEXT_COLOR} !important;
    text-align: center;
    font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
    font-size: 2.3rem;
    letter-spacing: 0.05em;
    font-weight: 700;
    margin-top: 1.1rem;
    margin-bottom: 0.7rem;
}}
</style>
""", unsafe_allow_html=True)
# -------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "dashboard"
if "kunden" not in st.session_state:
    st.session_state.kunden = []

def header_area():
    st.markdown(f'<div class="yurt-header">Yurt/BDMC</div>', unsafe_allow_html=True)
    st.markdown(f'<img src="{NRC_LOGO_URL}" class="nrc-logo"/>', unsafe_allow_html=True)

def login():
    header_area()
    st.markdown('<div class="nrc-overlay">', unsafe_allow_html=True)
    st.header("🔐 NRC-CRM Login")
    user = st.text_input("Benutzername")
    pwd = st.text_input("Passwort", type="password")
    if st.button("Login"):
        if user == USER and pwd == PASSWORD:
            st.session_state.logged_in = True
            st.session_state.page = "dashboard"
        else:
            st.error("Falsche Login-Daten")
    st.markdown("</div>", unsafe_allow_html=True)

def dashboard():
    header_area()
    st.markdown('<div class="nrc-overlay">', unsafe_allow_html=True)
    st.header("📊 Dashboard")
    st.write("Willkommen im NRC-CRM. Wähle eine Aktion:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Neuer Servicefall"):
            st.session_state.page = "neuer_servicefall"
        if st.button("🔧 Alle Reparaturen"):
            st.session_state.page = "alle_reparaturen"
    with col2:
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "dashboard"
    st.markdown("</div>", unsafe_allow_html=True)

def neuer_servicefall():
    header_area()
    st.markdown('<div class="nrc-overlay">', unsafe_allow_html=True)
    st.header("➕ Neuer Servicefall")
    st.write("**Pflichtfelder sind mit * markiert.**")
    if "submitted" not in st.session_state:
        st.session_state["submitted"] = False
    error_fields = []
    name = st.text_input("Name *", key="name")
    email = st.text_input("E-Mail *", key="email")
    phone = st.text_input("Telefon *", key="phone")
    company = st.text_input("Firma", key="company")
    country = st.selectbox("Land", COUNTRIES, key="country")
    if st.button("Speichern"):
        st.session_state["submitted"] = True
        for fld, val in [("Name", name), ("E-Mail", email), ("Telefon", phone)]:
            if not val.strip():
                error_fields.append(fld)
        if error_fields:
            st.error("Bitte ausfüllen: " + ", ".join(error_fields))
            # JS zur Markierung der leeren Felder
            st.markdown(f"""
            <script>
            for (const label of document.querySelectorAll('label')) {{
                if ({'"Name *"' in error_fields}) {{
                    if (label.textContent.includes("Name *")) {{
                        let input = label.parentElement.querySelector('input');
                        if (input && input.value === "") input.classList.add('error-field');
                    }}
                }}
                if ({'"E-Mail *"' in error_fields}) {{
                    if (label.textContent.includes("E-Mail *")) {{
                        let input = label.parentElement.querySelector('input');
                        if (input && input.value === "") input.classList.add('error-field');
                    }}
                }}
                if ({'"Telefon *"' in error_fields}) {{
                    if (label.textContent.includes("Telefon *")) {{
                        let input = label.parentElement.querySelector('input');
                        if (input && input.value === "") input.classList.add('error-field');
                    }}
                }}
            }}
            </script>
            """, unsafe_allow_html=True)
        else:
            st.success(f"Kunde '{name}' gespeichert ✅")
            st.session_state.kunden.append({
                "Name": name,
                "E-Mail": email,
                "Telefon": phone,
                "Firma": company,
                "Land": country
            })
            for k in ["name", "email", "phone", "company"]:
                st.session_state[k] = ""
            st.session_state["submitted"] = False
    if st.button("🔙 Zurück"):
        st.session_state.page = "dashboard"
        st.session_state["submitted"] = False
    st.markdown("</div>", unsafe_allow_html=True)

def alle_reparaturen():
    header_area()
    st.markdown('<div class="nrc-overlay">', unsafe_allow_html=True)
    st.header("🔧 Alle Reparaturen")
    if st.session_state.kunden:
        st.table(st.session_state.kunden)
    else:
        st.info("Keine Einträge vorhanden.")
    if st.button("🔙 Zurück"):
        st.session_state.page = "dashboard"
    st.markdown("</div>", unsafe_allow_html=True)

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
