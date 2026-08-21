from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os 


load_dotenv()

print(os.getenv("GOOGLE_API_KEY"))

template = PromptTemplate(
    template="Say hi {name} in {language} language.. ",
    input_variables=["name","language"],
    validate_template=True
)

name = input("Enter your name")
print("\n")
language = input("Enter your language")

formated_prompt = template.invoke({
    "name":name,
    "language":language
})


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

result = model.invoke(formated_prompt)

print(result.content)