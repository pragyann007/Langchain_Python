from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
load_dotenv()

embedings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
documents = [
    {
        "text": "The Nebula-9 drone features a hydrogen fuel cell providing 12 hours of continuous flight. It is primarily used for deep-forest search and rescue operations.",
        "metadata": {"category": "tech", "year": 2026, "project": "Nebula"}
    },
    {
        "text": "Quantum computing startups raised a record $4.2 billion in venture capital this year. Experts predict commercial fault-tolerant systems will emerge by 2030.",
        "metadata": {"category": "finance", "year": 2026, "project": "Quantum"}
    },
    {
        "text": "A new species of bioluminescent mushroom, Mycena lux-silva, was discovered in the Amazon. It glows with a soft green light to attract nocturnal spore-dispersing beetles.",
        "metadata": {"category": "science", "year": 2025, "project": "Amazon-Bio"}
    },
    {
        "text": "The Orion-X rover successfully extracted liquid water from beneath the Martian regolith. This marks a massive milestone for future human colonization efforts.",
        "metadata": {"category": "science", "year": 2026, "project": "Orion"}
    },
    {
        "text": "Global supply chains face delays as major shipping lanes experience unprecedented seasonal fog. Logistics companies are turning to AI routing alternatives.",
        "metadata": {"category": "finance", "year": 2025, "project": "Logistics"}
    },
    {
        "text": "Cybersecurity firms warn of a new ransomware strain named 'SilverFox'. It targets legacy industrial control systems using outdated firmware protocols.",
        "metadata": {"category": "tech", "year": 2026, "project": "Security"}
    }
]

# langchain_docs = [

#     Document(page_content=doc["text"],metadata=doc["metadata"])
#     for doc in documents
# ]


vector_store = PineconeVectorStore.from_existing_index(index_name="my-indx",embedding=embedings)

res = vector_store.as_retriever(kwargs={"k":3})
results = res.invoke("cybersecurity firms")


print(results[0].page_content)
