
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda
from enum import Enum
from langchain_core.documents import Document

load_dotenv()

nam = input("Enter your name...")
cont = input("Enter your large content ....")


def intelegince(content:str,name:str):
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    class Difficulty(str, Enum):
        EASY = "easy"
        HARD = "hard"
        INTERMEDIATE = "intermediate"

   


    
    class Response(BaseModel):
        title:str
        summary:str
        category:str
        difficulty:Difficulty
        keywords:list[str]
        sentiment:str
    
    document = Document(
        page_content=content,
        metadata={"owner":name}
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system","You are a helful assistant that will return the content guiadance add the suitable title summarise it and create some additional information like its category diffciulty keywords and its seniments  and meta information to user from the content you receive in dict format.. "),
        ("user","This is users detailed content : \n\n\n {content}")]
    )
    struct_model = model.with_structured_output(Response)


    chain = RunnableSequence(
        prompt,
        struct_model,
        RunnableParallel(
            contents=RunnablePassthrough(),
            count=RunnableLambda(lambda x:len(x.summary))
        )
        

    )


    res = chain.invoke({
        "content":document.page_content,
       
    })

    return res 


output = intelegince(content=cont,name=nam)

print(output)
    