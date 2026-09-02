from langchain_core.tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

# create tool :
@tool
def multiply(a:int,b:int)->int:
    """take 2 no as input and multiply and return int"""
    return a*b 

# llminitialise
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# tool binidng
llm_withTools = llm.bind_tools([multiply])

# prompt creation 
query = HumanMessage("Muliply 2 and 3")

# messages memory 
messages = [query]

# tool calling
tool_call = llm_withTools.invoke("Multiply 2 and 3 ")

resultfromToolCall = tool_call.tool_calls[0]

print("toolcall",tool_call.tool_calls)

# tool execution
toolMessage = multiply.invoke(resultfromToolCall)
print("toolmsg",toolMessage)
messages.append(toolMessage)


print(messages)
# final tool message embeded and execution
finalResult = llm.invoke(messages)
print(finalResult.content)


