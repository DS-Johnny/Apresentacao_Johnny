import streamlit as st

# ------------------------ Sidebar ------------------------------------------
st.sidebar.image("senai_logo.jpg")
st.sidebar.title('Fábrica de Programadores')






# ------------------------ Body ----------------------------------------------

col1, col2 = st.columns(2)

with col1:
	st.image('johnny.jpeg', width=200)

with col2:
	st.title('Johnny')
	st.markdown('## Oi, pessoal! Eu sou o professor Johnny e serei o professor de Python de vocês.')

st.markdown('---')

hist, jornada, sobre = st.tabs(['Minha história com a programação', 'A jornada de vocês', 'Curiosidades sobre mim'])

