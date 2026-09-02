from langchain_community.tools import DuckDuckGoSearchResults,ShellTool

search_tool = DuckDuckGoSearchResults()
# results = search_tool.invoke("ipl 2027 ")

shell = ShellTool()

result = shell.invoke("ls")
print(result)