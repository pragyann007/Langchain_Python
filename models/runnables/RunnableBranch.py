from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableParallel,RunnablePassthrough,RunnableBranch
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt1 = PromptTemplate(
    template="Write a report on this topic {topic} ",
    input_variables=["topic"]
)


prompt2 = PromptTemplate(
    template="Summarise this report in short {report} ",
    input_variables=["report"]
)

parser = StrOutputParser()

joke_gen = RunnableSequence(prompt1,model,parser)

chain = RunnableSequence(joke_gen,RunnableBranch(
    (lambda x:len(x.split())>300,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()

))






res = chain.invoke({"topic":"standup comedy"})

print(res)