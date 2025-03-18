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
		st.markdown('''Minha paixão pela programação começou com um joguinho muito divertido: o RPG Maker. 
  Para quem não conhece, o RPG Maker permite que você crie seus próprios jogos e, de certa forma, é um tipo de programação orientada a eventos. Eu fiquei fascinado pela lógica por trás dos jogos e, depois de alguns anos, quis aprender mais sobre programação. Então, decidi estudar Python.
  
  O que eu mais gosto de ensinar é que, ao mesmo tempo em que ensino, também aprendo muito com cada turma. Como disse Albert Einstein: “Quando você ensina, aprende duas vezes.” E é exatamente isso que acontece em sala de aula. Acredito que o aprendizado é sempre uma troca.''')

with sobre:
	col1, col2 = st.columns(2)
	with col1:
		st.write('boardgame.png', width=150)
	with col2:
		st.markdown('''Além da programação, sou apaixonado por várias outras coisas, como tocar violão, jogar games e jogos de tabuleiro. 
  Amo filmes e séries e sou fã de esportes radicais e artes marciais (mesmo que eu esteja meio fora de forma ultimamente :joy:). 
  Ah, também sou bem viciado em aprender idiomas! Tenho 10 anos de experiência ensinando Inglês e atualmente estudo Norueguês. ''')

with jornada:
	col1, col2 = st.columns(2)
	with col1:
		st.write('python.png', width=150)
	with col2:
		st.markdown('''Eu espero que a gente se divirta muito enquanto exploramos Python. Mais do que aprender comandos e códigos, quero que vocês sintam a magia de resolver problemas de forma criativa, com lógica e com a ajuda dessa linguagem maravilhosa.
Ao final do curso vocês serão capases de desenvolver aplicações em linguagem Python, por meio de técnicas de programação, seguindo boas práticas, procedimentos e normas. ''')

with univ:
	st.markdown('''Acreditem, programação não é só para quem quer ser programador. A lógica de programação que aprendemos com Python é uma ferramenta poderosa que pode ser aplicada em várias áreas, além da tecnologia.
Por exemplo, em Saúde, médicos podem usar análise de dados e modelos preditivos para melhorar diagnósticos, prever surtos de doenças e até otimizar tratamentos personalizados. 
Já no Direito, advogados podem usar Python para automatizar tarefas repetitivas, como revisar contratos, ou analisar grandes volumes de documentos legais. 
Além disso, em áreas como Marketing, Engenharia, Psicologia e Educação, habilidades de lógica e resolução de problemas ajudam a estruturar decisões e melhorar processos.
Ou seja, aprender a programar é como aprender uma nova forma de pensar e de resolver problemas — e isso vale em qualquer profissão que você escolher!''')

