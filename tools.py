from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun

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

TOOLS = [search_tool]

