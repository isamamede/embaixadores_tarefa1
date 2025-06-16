from typing import List, Optional

import streamlit as st
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

from tools import search_tool

# ---------------------------
# API Key Input
# ---------------------------
# Load env
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY não encontrada! Verifique seu arquivo .env")

# ---------------------------
# Tools
# ---------------------------
tools = [search_tool]


# ---------------------------
# LLM
# ---------------------------
llm = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.2,
)


# ---------------------------
# Data Model for Parsing
# ---------------------------
class ResearchResponse(BaseModel):
    topic: str
    answer: str
    sources: Optional[List[str]] = []
    tools_used: Optional[List[str]] = []


# ---------------------------
# Prompt Template with Parsing
# ---------------------------
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Você é **Prof. Meta**, um especialista em metodologia científica, pesquisa acadêmica, meta-análises e escrita científica.

Responda às perguntas utilizando as ferramentas necessárias. Seja didático, claro, objetivo e use exemplos sempre que possível.

Seu público são estudantes da área da saúde, com pouca familiaridade com pesquisa.

Formate sua resposta estritamente neste formato JSON e não adicione nenhum texto extra:

{format_instructions}
""",
        ),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())


# ---------------------------
# Agent Setup
# ---------------------------
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)


# ---------------------------
# Session State (Only for Display)
# ---------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------------------
# Streamlit UI
# ---------------------------
st.title("🤖 Prof. Meta — AI Assistente de Pesquisa")
st.markdown(
    """
    Pergunte sobre metodologia científica, revisões, escrita acadêmica, citações, bancos de dados e muito mais.
    """
)


# Input de Pergunta
user_query = st.text_input("Digite sua pergunta:")

if user_query:
    with st.spinner("Prof. Meta está pensando..."):
        try:
            inputs = {"query": user_query}

            raw_response = agent_executor.invoke(inputs)

            # Parse structured output
            structured_response = parser.parse(raw_response.get("output"))

            # Display structured response
            st.subheader("Resposta do Prof. Meta:")
            st.markdown(f"**Tema:** {structured_response.topic}")
            st.markdown(f"**Resposta:** {structured_response.answer}")

            if structured_response.sources:
                st.markdown("**🔗 Fontes:**")
                for src in structured_response.sources:
                    st.markdown(f"- {src}")

            if structured_response.tools_used:
                st.markdown("**🛠️ Ferramentas usadas:**")
                for tool in structured_response.tools_used:
                    st.markdown(f"- {tool}")

            # 💾 Update chat history (for display only)
            st.session_state.chat_history.append(("Você", user_query))
            st.session_state.chat_history.append(("Prof. Meta", structured_response.answer))

        except Exception as e:
            st.error(f"❌ Erro na resposta: {e}")
            st.json(raw_response)


# ---------------------------
# Display Chat History (Only for UI)
# ---------------------------
if st.session_state.chat_history:
    with st.expander("🕑 Histórico da Conversa"):
        for role, msg in st.session_state.chat_history:
            if role == "Você":
                st.markdown(f"**🧑‍💻 {role}:** {msg}")
            else:
                st.markdown(f"**🤖 {role}:** {msg}")
