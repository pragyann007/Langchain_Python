from langchain_community.tools import DuckDuckGoSearchResults

search_tool = DuckDuckGoSearchResults()
results = search_tool.invoke("ipl 2027 ")
print(results)