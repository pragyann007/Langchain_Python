from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field

class MultiplyInput(BaseModel):
    a:int=Field(required=True,description="Integer")
    b:int=Field(required=True,description="Integer")

def multiply(a:int,b:int)->int:
    return a*b ; 

multiply_tool = StructuredTool(
    name="Multiply",
    func=multiply,
    description="takes 2 input and multiply them ",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({"a":3,"b":90})

print(result)