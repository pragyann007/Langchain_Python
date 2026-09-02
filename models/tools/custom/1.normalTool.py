from langchain_core.tools import tool

@tool
def multiply(a:int,b:int)->int:
    """ it will take a and b as a input integer and multiply both,, """
    return a*b 

result = multiply.invoke({"a":2,"b":990003})

print(result)