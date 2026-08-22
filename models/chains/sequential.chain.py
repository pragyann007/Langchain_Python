from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on this topic : {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Write a most important 5 pointers from this report : {report}",
    input_variables=["report"]
)


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser 

topic = input("Enter a topc to get a report and short summary : ")

res = chain.invoke({"topic":topic})

print(res)