from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

class Person(TypedDict):
    name:str
    age:int
    summary:str
    skills:list[str]
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

struct_model = model.with_structured_output(Person)

results = struct_model.invoke("My name is pragyan i kno mern nest js gen ai  i am 18 yo")

print(results["name"])