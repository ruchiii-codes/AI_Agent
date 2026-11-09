import wikipediaapi
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description=(
    "Save the research result to research_output.txt only when "
    "the user explicitly asks to save the result."
    ),
)

search = DuckDuckGoSearchRun()

def search_web(query: str):
    try:
        return search.run(query)
    except Exception as e:
        return f"Web search is temporarily unavailable: {str(e)}"

search_tool = Tool(
    name="search",
    func=search_web,
    description=(
        "Search the web for relevant information about a topic. "
        "Use only when additional web information is needed. "
        "Avoid repeating searches for the same topic."
    ),
)

wiki_client = wikipediaapi.Wikipedia(
    user_agent="RuchiResearchAgent/1.0 (learning project)",
    language="en"
)

def search_wikipedia(query: str):
    page = wiki_client.page(query)

    if not page.exists():
        return f"No Wikipedia page found for {query}"

    return page.summary[:2000]

wiki_tool = Tool(
    name="wikipedia",
    func=search_wikipedia,
    description=(
        "Get background information about a topic from Wikipedia. "
        "Use this tool once when relevant. Do not search for the same "
        "Wikipedia information again using the web search tool."
    )
)