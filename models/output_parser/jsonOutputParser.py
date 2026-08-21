from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = JsonOutputParser()

template = PromptTemplate(
    template="create a list of 5 fake peoples of this country {country} in this {format}",
    input_variables=["country"],
    partial_variables={"format":parser.get_format_instructions()}
)


chain = template | model | parser 

finalRes = chain.invoke({"country":"colombian"})

print(finalRes)
