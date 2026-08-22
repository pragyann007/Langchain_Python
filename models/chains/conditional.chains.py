from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from langchain_core.runnables import Runnable,RunnableBranch,RunnableLambda
from pydantic import BaseModel , Field
from typing import Literal

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Response(BaseModel):
    sentiments:Literal["positive","negative"]=Field(description="Either positive or negative")

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Response)

prompt1 = PromptTemplate(
    template="Review this feedback \n {feedback} \n of user and classify it either it is positive or negative in this format: {format} ",
    input_variables=["feedback"],
    partial_variables={
        "format":parser2.get_format_instructions()
    }
)

classifer_chain = prompt1 | model | parser2

# res = classifer_chain.invoke({"feedback":"This product was absoultely wate of timee and its very much bad product i dont recomend this to anyone."})

# print(res)

prompt2 = PromptTemplate(
    template="Generate a positive feedback for this message {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Generate a negative feedback for this message {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiments == "positive",prompt2|model|parser1),
    (lambda x:x.sentiments == "negative",prompt3|model|parser1),
    RunnableLambda(lambda x :"no sentiment detected")
)

chain = classifer_chain | branch_chain 

feedback = """  the product is very amazing it got me my lead that i missed 101 days ago that gave me comission of 900k usd andd this platform just charge 30usd pper onthh wow its very great product for real estaete agent i wonder why cost of this saas is so less i am ready to pay 100s of bucks to this goldmine tool .."""

res = chain.invoke({"feedback":feedback})

print(res)




