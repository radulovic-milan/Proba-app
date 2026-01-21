import streamlit as st

st.title("Proračun vremena potrebnog čestici podzemne vode da pređe rastojanje između dvije tačke")
st.write("---")

L = st.number_input("Rastojanje između dvije tačke po pravcu toka (m)")
dh = st.number_input("Razlika u nivoima podzemnih voda između dvije tačke (m)")
k = st.number_input("Koeficijent filtracije (m/s)", format="%f")
ne = st.number_input("Efektivna poroznost (-)", max_value=1.0)

   
if st.button("Izračunaj"):
    i = dh / L                         # hidraulički gradijent
    v_d = k * i                        # Darsijeva brzina
    v_r = v_d / ne                     # realna brzina
    t = L / v_r                        # vrijeme (s)
    t_d = (L / v_r)/86400               # vrijeme (dan)
    st.success(f"Vrijeme putovanja čestice: {t_d:.2f} dana")

