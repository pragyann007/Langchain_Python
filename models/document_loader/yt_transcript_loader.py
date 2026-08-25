from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


parser = StrOutputParser()

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
doc = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=wGBQTpGqc5c&t=57s")
prompt = PromptTemplate(
    template="See the transcript of video and say what is this video about and what i sthe core concept used n this video , {transcript}",
    input_variables=["transcript"]
)

docs = doc.load()

tsct = docs[0].page_content
print(tsct)

chain = prompt|model|parser

res = chain.invoke({"transcript":tsct})
print(res)
