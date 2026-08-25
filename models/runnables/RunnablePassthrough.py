from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
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
promp2 = PromptTemplate(
    template="Explain this joke in simple manner : joke : \n {joke}",
    input_variables=["joke"]
)


joke_with_explanation = RunnableParallel({
     "joke":RunnablePassthrough(),
     "explaination":RunnableSequence(promp2,model,parser)

}
   
)

joke= RunnableSequence(
    prompt1,model,parser,
    joke_with_explanation
)


res = joke.invoke({"topic":"actress"})
print(res)