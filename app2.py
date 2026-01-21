import streamlit as st

st.title("Proračun vremena potrebnog čestici podzemne vode da pređe rastojanje između dvije tačke")
st.write("---")

L = st.number_input("Rastojanje između dvije tačke po pravcu toka (m)", min_value=0.0)
dh = st.number_input("Razlika u nivoima podzemnih voda između dvije tačke (m)")
k = st.number_input("Koeficijent filtracije (m/s)", min_value=0.0, format="%f")
ne = st.number_input("Efektivna poroznost (-)", min_value=0.0, max_value=1.0)

if L > 0 and ne > 0:
    i = dh / L                         # hidraulički gradijent
    v_d = k * i                        # Darsijeva brzina
    v_r = v_d / ne                     # realna brzina
    t = L / v_r                        # vrijeme (s)

   
if st.button("Calculate"):
    st.success(f"Vrijeme putovanja čestice: {t/86400:.2f} dana")

