from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt1 = PromptTemplate(
    template="differntiate this {topic} with first prinicple you mst differntiate using 1st prinicple no other method is allowed  with all stepss in detail markdown format response with explaining each step  ",
    input_variables=["topic"]
)

parser = StrOutputParser()
promp2 = PromptTemplate(
   template="diffferntiate this {topic}but never ever use first principl in detail markdown format response with explaining each step e",
    input_variables=["topic"]
)


parallel_chain = RunnableParallel({
    "first_principle":RunnableSequence(prompt1,model,parser),
    "any":RunnableSequence(promp2,model,parser)
})


deriv = input("Enter the derivative expression.... ")
res = parallel_chain.invoke({"topic":deriv})
print(res)