from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel,Field
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


class Person(BaseModel):
    name:str=Field(description="name ")
    age:int=Field(description="age ")
    country:str=Field(description="country name  ")
class Response(BaseModel):
    persons:list[Person]=Field(description="List of userss ")

parser = PydanticOutputParser(pydantic_object=Response)
template = PromptTemplate(
    template="create a list of 5 fake peoples of this country {country} in this {format}",
    input_variables=["country"],
    partial_variables={"format":parser.get_format_instructions()}
)


chain = template | model | parser 

finalRes = chain.invoke({"country":"colombian"})

print(finalRes)
