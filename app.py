import streamlit as st

# Design/Branding
PRIMARY = "#1B3556"
ACCENT = "#F7C843"
BG_OVERLAY = "rgba(255,255,255,0.83)"
NRC_LOGO_URL = "https://notebook-repair-corner.at/wp-content/uploads/2022/03/nrc-logo-1.png"
NRC_BG_URL = "https://notebook-repair-corner.at/wp-content/uploads/2022/03/nrc-background-light.jpg"

USER, PASSWORD = "admin", "1234"
COUNTRIES = [
    "Österreich", "Deutschland", "Schweiz", "Türkei", "USA", "Frankreich", "Italien", "Spanien", "England",
    "Polen", "Ungarn", "Kroatien", "Griechenland", "Niederlande", "Rumänien", "Serbien", "Bulgarien", "Dänemark",
    "Tschechien", "Slowakei", "Slowenien", "Belgien", "Luxemburg", "Norwegen", "Finnland", "Schweden", "Portugal"
    # ... gerne beliebig erweitern!
]

# ---------- Apple-Style CSS ----------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600;700&display=swap');
body, .stApp {{
  font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
  background: url('{NRC_BG_URL}') center/cover no-repeat fixed;
}}
.nrc-overlay {{
  background: {BG_OVERLAY};
  border-radius: 22px;
  padding: 2.3rem 2.3rem 1.7rem 2.3rem;
  max-width: 540px;
  margin: 2rem auto 2rem auto;
  box-shadow: 0 8px 36px 0 rgba(20,30,40,0.13);
}}
input, select, textarea {{
  border: 1.2px solid #dee2e6;
  border-radius: 13px;
  padding: 0.7rem;
  font-size: 1.07rem;
  background: #fafdff;
  margin-bottom: 0.15rem;
  transition: border 0.18s, box-shadow 0.18s;
}}
input:focus, select:focus, textarea:focus {{
  outline: none;
  border-color: {PRIMARY};
  box-shadow: 0 0 0 3px rgba(27,53,86,0.18);
  background: #f0f6fc;
}}
.stButton>button, .stDownloadButton>button {{
  background-color: {PRIMARY};
  color: white;
  border-radius: 12px;
  padding: 0.7rem 1.15rem;
  font-size: 1.07rem;
  font-weight: 600;
  box-shadow: 0 2px 6px rgba(25,45,65,0.09);
  border: none;
  margin-top: 0.2rem;
}}
.stButton>button:hover {{
  background-color: {ACCENT};
  color: #222;
}}
.error-field {{
  border-color: #e53935 !important;
  box-shadow: 0 0 0 2px rgba(229,57,53,0.16);
  background: #fff1f1 !important;
}}
.stAlert {{
  border-radius: 13px;
}}
</style>
""", unsafe_allow_html=True)
# -------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "dashboard"
if "kunden" not in st.session_state:
    st.session_state.kunden = []

def login():
    st.image(NRC_LOGO_URL, width=142)
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
    st.image(NRC_LOGO_URL, width=142)
    st.markdown('<div class="nrc-overlay">', unsafe_allow_html=True)
    st.header("📊 Dashboard")
    st.write("Willkommen im stilvollen NRC-CRM. Wähle eine Aktion:")
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
    st.image(NRC_LOGO_URL, width=142)
    st.markdown('<div class="nrc-overlay">', unsafe_allow_html=True)
    st.header("➕ Neuer Servicefall")
    st.write("**Pflichtfelder sind mit * markiert.**")
    # State zur Fehleranzeige
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
        # Pflichtfeldprüfung
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
            # Felder leeren:
            for k in ["name", "email", "phone", "company"]:
                st.session_state[k] = ""
            st.session_state["submitted"] = False
    if st.button("🔙 Zurück"):
        st.session_state.page = "dashboard"
        st.session_state["submitted"] = False
    st.markdown("</div>", unsafe_allow_html=True)

def alle_reparaturen():
    st.image(NRC_LOGO_URL, width=142)
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
