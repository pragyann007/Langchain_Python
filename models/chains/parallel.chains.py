from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_mistralai.chat_models import ChatMistralAI
load_dotenv()
parser = StrOutputParser()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model2 = ChatMistralAI(model="mistral-small-latest")
prompt1 = PromptTemplate(
    template="Generate a short and swwt 5 pointer notes from this large text document : \n {document}",
    input_variables=["document"]
)

prompt2 = PromptTemplate(
    template="Generate a short and sweet 5 mcq quizes from this document text : \n {document}",
    input_variables=["document"]
)


prompt3 = PromptTemplate(
    template="merge these two notes and quizes in one section: \n Notes:{notes} \n quizes:{quizes}",
    input_variables=["notes","quizes"]
)


parallel_chain = RunnableParallel({
    "notes":prompt1 | model1 | parser ,
    "quizes":prompt2 | model2 | parser

})

merge_chain = prompt3 | model1 | parser 

chain = parallel_chain | merge_chain 

document = """
    NestJS developers and backend engineers possess a unique competitive advantage in the booming Agentic AI (Agent AI) landscape. Building autonomous AI agents requires far more than just prompting a Large Language Model (LM). It demands robust infrastructure, structured data flow, and reliable orchestrations—areas where backend specialists excel.Production-Ready ArchitectureAI agents must execute complex workflows, chain multiple tasks, and handle errors gracefully. NestJS, with its TypeScript foundation and modular architecture, provides the ideal framework for this. Its built-in support for Dependency Injection simplifies the integration of various AI SDKs, vector databases, and memory layers. Backend developers can easily wrap agent logics into scalable, maintainable microservices.Efficient Tool IntegrationAgents become powerful when they can interact with the external world through tools. Backend engineers are experts at building and consuming APIs, managing database queries, and handling authentication. By leveraging tools like LangChain or LlamaIndex within a NestJS environment, developers can securely grant agents the ability to read databases, send emails, or trigger webhooks, transforming static LLMs into active problem-solvers.State Management and StreamingAutonomous agents often require long-running processes and persistent state memory to track user interactions. Backend developers leverage Redis, PostgreSQL, and event-driven architectures (like MQTT or Kafka) to maintain this context. Furthermore, NestJS excels at handling Server-Sent Events (SSE) and WebSockets. This allows developers to stream real-time agent thoughts and responses directly to the frontend, optimizing the user experience.Career and Financial GrowthBy stepping into Agent AI, backend developers future-proof their careers. They transition from building standard CRUD APIs to architecting intelligent systems. This shift opens high-paying roles in AI engineering and enterprise automation, allowing developers to capture massive market value.
"""




res = chain.invoke({"document":document})

print("######################## RESPONSE #############################################")

print("\n")
print(res)

print("\nGraphs ::::: ")
print(chain.get_graph().draw_ascii())
