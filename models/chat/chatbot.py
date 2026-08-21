from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

message_history = []

while 2==2:
    user_prompt = input("You : ")
    if(user_prompt=="exit"):
        break 
    message_history.append({
        "role":"user",
        "content":user_prompt
    })


    result = model.invoke(message_history)
    print("AI: ",result.content)
    message_history.append({
        "role":"assistant",
        "content":result.content
    })
