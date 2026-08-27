from pinecone import Pinecone
from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

embedings = GoogleGenerativeAIEmbeddings(
   model="gemini-embedding-001")

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

vector_store = PineconeVectorStore.from_existing_index(index_name="my-indx",embedding=embedings)


retriver = vector_store.as_retriever(
    
     search_type="mmr",
     search_kwargs={"k": 2, "fetch_k": 2, "lambda_mult": 0.5},
)

res = retriver.invoke("cyberscurity ")
print(res)