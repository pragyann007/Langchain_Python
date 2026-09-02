from langchain_core.tools import tool

@tool
def add(a:int,b:int)->int:
    """takes 2 integer as input and add them"""
    return a+b

@tool
def subtract(a:int,b:int)->int:
    """takes 2 integer as input and subtract them"""
    return a-b 

class MathToolKit:
    def get_tools(self):
        return [add,subtract]

toolKit = MathToolKit()
tools = toolKit.get_tools()


for tool in tools:
    res = tool.invoke({"a":90,"b":20})
    print(res)
