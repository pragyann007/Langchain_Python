from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

loader = TextLoader("abc.txt",encoding="utf-8")

doc = loader.load()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt1 = PromptTemplate(
    template="what is suitable title for this text : {text} ",
    input_variables=["text"]
)
parser = StrOutputParser()

chain = prompt1|model|parser
res = chain.invoke({"text":doc[0].page_content})



print(res)