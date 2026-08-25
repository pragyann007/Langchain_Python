from langchain_community.document_loaders import PyPDFLoader,WebBaseLoader
c

loader = WebBaseLoader("https://portfolio-pragyan.vercel.app/")

doc = loader.load()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt1 = PromptTemplate(
    template="this is the guy that i am looking to hire as a backend developer is he fit ? : {text} ",
    input_variables=["text"]
)
parser = StrOutputParser()

chain = prompt1|model|parser
res = chain.invoke({"text":doc[0].page_content})



print(res)