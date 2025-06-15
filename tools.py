from datetime import datetime

from fpdf import FPDF
from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun

# ---------------------------
# Save Text to PDF Utility
# ---------------------------

def save_to_pdf(data: str, filename: str = "research_output.pdf") -> str:
    """
    Saves given text data into a PDF file with a timestamp header.

    Args:
        data (str): Text to save.
        filename (str): PDF filename.

    Returns:
        str: Success message with filename.
    """
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"--- Research Output ---\nTimestamp: {timestamp}\n\n"

        pdf.multi_cell(0, 10, header + data)

        pdf.output(filename)

        return f"Salvo com sucesso em {filename}"
    except Exception as e:
        return f"Falha em salvar PDF: {str(e)}"


save_tool = Tool(
    name="save_text_to_pdf",
    func=save_to_pdf,
    description="Salva resultados em um arquivo PDF."
)


# ---------------------------
# Search Tool (DuckDuckGo)
# ---------------------------

search_tool = Tool(
    name="web_search",
    func=DuckDuckGoSearchRun().run,
    description="Procura na internet por informações."
)


# ---------------------------
# List of Tools
# ---------------------------

TOOLS = [search_tool, save_tool]

