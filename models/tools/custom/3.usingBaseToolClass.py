from langchain_core.tools import BaseTool
from typing import Type
from pydantic import BaseModel,Field

class MultiplyInput(BaseModel):
    a:int=Field(required=True,description="Integer")
    b:int=Field(required=True,description="Integer")


class MultiplyTool(BaseTool):
    name:str="multiply",
    description:str="Take 2 input integer and multiply both of them"
    args_schema:Type[BaseModel]=MultiplyInput

    def _run(self, a:int,b:int)->int:
        return a*b 
multiply_tool = MultiplyTool()

res = multiply_tool.invoke({"a":9,"b":6})

print(res)