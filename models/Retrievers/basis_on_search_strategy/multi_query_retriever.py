from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from pinecone import Pinecone
from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore

load_dotenv()

embedings = GoogleGenerativeAIEmbeddings(
   model="gemini-embedding-001")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

vector_store = PineconeVectorStore.from_existing_index(index_name="my-indx",embedding=embedings)



mqr = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(
         search_kwargs={"k": 2, "fetch_k": 2, "lambda_mult": 0.5},
),
llm=llm

)

res = mqr.invoke("hacking ransom")

print(res)