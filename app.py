import streamlit as st

st.set_page_config(page_title="Gerador de Questões", layout="centered")

st.title("📘 Gerador de Questões para Concursos Públicos")
banca = st.text_input("Banca examinadora", "FGV")
disciplina = st.text_input("Disciplina", "Direito Constitucional")
tema = st.text_input("Tema", "Princípios da Administração Pública")

if st.button("Gerar Questão"):
    st.write(f"🔍 Questão gerada com base na banca {banca}, disciplina {disciplina}, tema {tema}")
    st.write("👉 Qual é o princípio que garante a publicidade dos atos administrativos?")

