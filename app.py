import streamlit as st
import openai

st.set_page_config(page_title="Gerador de Questões para Concursos", layout="centered")

st.title("📘 Gerador de Questões para Concursos Públicos")

banca = st.text_input("Banca examinadora", "FGV")
disciplina = st.text_input("Disciplina", "Direito Constitucional")
tema = st.text_input("Tema", "Princípios da Administração Pública")

openai.api_key = st.secrets["openai_api_key"]

def gerar_questao(banca, disciplina, tema):
    prompt = f"""
    Gere uma questão de concurso público de múltipla escolha no estilo da banca {banca}, 
    da disciplina {disciplina}, sobre o tema: {tema}.

    A questão deve conter:
    - Enunciado
    - 4 alternativas (A, B, C, D)
    - Gabarito correto com justificativa

    Formato:
    Enunciado: ...
    A) ...
    B) ...
    C) ...
    D) ...
    Gabarito: Letra X
    Comentário: ...
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=700
    )

    return resposta.choices[0].message["content"]

if st.button("🔍 Gerar Questão"):
    with st.spinner("Gerando questão com inteligência artificial..."):
        questao = gerar_questao(banca, disciplina, tema)
        st.markdown("### 📄 Questão Gerada:")
        st.write(questao)
