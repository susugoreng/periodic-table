import streamlit as st
import random

# Data unsur
elements = [
    {"symbol": "H", "name": "hidrogen"},
    {"symbol": "He", "name": "helium"},
    {"symbol": "Li", "name": "litium"},
    {"symbol": "C", "name": "karbon"},
    {"symbol": "N", "name": "nitrogen"},
    {"symbol": "O", "name": "oksigen"},
    {"symbol": "F", "name": "fluorin"},
    {"symbol": "Na", "name": "natrium"},
    {"symbol": "Cl", "name": "klorin"},
    {"symbol": "K", "name": "kalium"}
]

# Inisialisasi session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'round' not in st.session_state:
    st.session_state.round = 0
if 'used' not in st.session_state:
    st.session_state.used = []
if 'current' not in st.session_state:
    st.session_state.current = random.choice(elements)

st.title("🔬 Game Tebak Unsur Kimia")
st.write("Tebak nama unsur berdasarkan **simbol kimia**!")

# Pilih simbol yang belum pernah dit
