# Prof. Meta — Assistente Virtual de Pesquisa e Metodologia Científica

**Prof. Meta** é um assistente virtual desenvolvido para auxiliar estudantes de cursos da área da saúde em dúvidas relacionadas à **metodologia científica, revisão de literatura, escrita acadêmica e normas de citação**.

O assistente utiliza inteligência artificial (IA) com modelo GPT-4o, integrado a ferramentas de busca na web e exportação de respostas em PDF. Foi projetado para oferecer respostas claras, didáticas e organizadas, mesmo para usuários com pouca familiaridade com tecnologia.

---

## 🔗 Acesse o assistente online

O projeto está disponível gratuitamente em:

**[https://embaixadoresisa.streamlit.app/](https://embaixadoresisa.streamlit.app/)**

---

## 🚀 Funcionalidades

- Responde perguntas sobre metodologia científica, revisão sistemática, revisão integrativa, PICO, normas de citação e outros temas acadêmicos.
- Busca informações atualizadas na internet utilizando DuckDuckGo.
- Permite salvar as respostas em arquivos PDF.
- Respostas estruturadas, claras e voltadas para estudantes da área da saúde.
- Histórico de conversa exibido na interface.

---

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4o](https://platform.openai.com/)
- [DuckDuckGo Search API](https://duckduckgo.com/)
- [Pydantic](https://docs.pydantic.dev/)

---

## 📦 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/isamamede/embaixadores_tarefa1.git
cd new directory
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as credenciais

Crie o arquivo **`.streamlit/secrets.toml`** com o seguinte conteúdo:

```toml
OPENAI_API_KEY = "sua-chave-da-openai"
```

Se desejar, adicione outras chaves conforme necessário.

### 4. Execute a aplicação

```bash
streamlit run main.py
```

---

## 📁 Estrutura do projeto

```
embaixadores_tarefa1/
├── .streamlit/
│   └── secrets.toml
├── tools.py
├── main.py
├── requirements.txt
├── README.md
```

---

## 📜 Licença

Este projeto é de uso educacional e acadêmico, sem fins comerciais. Consulte os termos de uso das APIs utilizadas (OpenAI, DuckDuckGo) para mais informações.
