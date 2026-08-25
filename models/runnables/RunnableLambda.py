from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt1 = PromptTemplate(
    template="Write a joke on this topic {topic} in sarcastic manner ",
    input_variables=["topic"]
)

parser = StrOutputParser()


parallel = RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "joke_length":RunnableLambda(lambda x:len(x.split()))
    }
)

joke_gen_explain = RunnableSequence(prompt1,model,parser,parallel)


res = joke_gen_explain.invoke({"topic":"standup comedy"})

print(res)