from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant.

            Answer the user's query using the available tools when required.

            Tool usage rules:
            - Use Wikipedia for background information when relevant.
            - Use web search when current or additional information is needed.
            - For a research query, call Wikipedia once and web search once at most.
            - Do not repeat the same search query.
            - Do not search for Wikipedia links after using the Wikipedia tool.
            - If web search fails, continue using the information already retrieved.
            - Never repeat a tool call with a slightly different query.
            - Once you have enough information, stop calling tools and prepare the final answer.

            - For broad research queries, use the available information from the first successful Wikipedia and web search calls.
            - Do not search for Wikipedia pages using the web search tool.
            - After collecting information, immediately generate the final JSON response.

            Return valid JSON with exactly these fields:
            - topic: string
            - summary: string
            - sources: list of strings containing URLs only
            - tools_used: list of strings containing tool names

            Only include URLs actually returned by the tools.
            Never invent sources or URLs.
            Do not call any tool named JSON.
            """
        ),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)
tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=5,
    max_execution_time=60,
    handle_parsing_errors=True
)

query = input("What can i help you research? ")
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)


