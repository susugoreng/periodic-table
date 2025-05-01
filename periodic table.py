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

# Pilih simbol yang belum pernah ditanya
while st.session_state.current in st.session_state.used:
    st.session_state.current = random.choice(elements)

symbol = st.session_state.current["symbol"]
correct_answer = st.session_state.current["name"]

# Input user
user_answer = st.text_input(f"Apa nama unsur dengan simbol **{symbol}**?", key=st.session_state.round)

if st.button("Kirim Jawaban"):
    st.session_state.used.append(st.session_state.current)
    st.session_state.round += 1

    if user_answer.lower().strip() == correct_answer:
        st.success("✅ Benar!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Salah. Jawaban benar: **{correct_answer.capitalize()}**")

    if st.session_state.round < 5:
        st.session_state.current = random.choice(elements)
    else:
        st.markdown("---")
        st.subheader(f"🎯 Skor Akhir Kamu: {st.session_state.score}/5")

        if st.session_state.score == 5:
            st.success("🎉 Luar biasa! Kamu menguasai semua simbol!")
        elif st.session_state.score >= 3:
            st.info("👍 Bagus! Tapi masih bisa lebih baik.")
        else:
            st.warning("📚 Yuk belajar lagi tentang unsur kimia!")

        st.button("Main Lagi", on_click=lambda: [st.session_state.clear(), st.experimental_rerun()])

# Pilih simbol yang belum pernah dit
