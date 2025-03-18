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

hist, sobre, jornada, univ = st.tabs(['Minha história com a programação', 'Curiosidades sobre mim', 'A jornada de vocês', 'O universo além de T.I.'])

with hist:
	col1, col2 = st.columns(2)
	with col1:
		st.image('rpgmaker.png', width=150)
	with col2:
		st.markdown('Minha paixão pela programação começou com um joguinho muito divertido: o RPG Maker. Para quem não conhece, o RPG Maker permite que você crie seus próprios jogos e, de certa forma, é um tipo de programação orientada a eventos (sim, você estava certo!). Eu fiquei fascinado pela lógica por trás dos jogos e, ao longo dos anos, quis aprender mais sobre programação. Então, decidi estudar Python.Apesar de já ter tocado em outras linguagens de programação, o Python foi a que mais me conquistou, principalmente porque decidi focar na área de dados. Mas, acreditem, eu também adoro o desenvolvimento de software e as infinitas possibilidades que ele oferece.')

with sobre:
	col1, col2 = st.columns(2)
	with col1:
		pass
	with col2:
		pass

with jornada:
	pass

with univ:
	pass

