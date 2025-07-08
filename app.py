def dashboard():
    st.image("https://notebook-repair-corner.at/assets/logo.png", width=200)  # Dein Logo-URL
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
