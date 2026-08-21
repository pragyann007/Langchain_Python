from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Summarise tese report in 100 words {report}",
    input_variables=["report"]
)

chain = template1 | model | parser | template2 | model | parser

finalRes = chain.invoke({"topic":"blokchcian web3 solana rust evm solidity"})

print(finalRes)
