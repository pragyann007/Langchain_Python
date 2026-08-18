import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { z } from "zod";

const responseSchema = z.array(
  z.object({
    language: z.string().describe("Name of language"),
    greeting: z.string().describe("Greeting text including the user's name"),
  })
);

const prompt = ChatPromptTemplate.fromMessages([
  [
    "system",
    "Your name is Jarvis. You are a greeting system that greets the user in at least 4 languages that is portugeese , japanesse , indian , colombian , addressing the user by name.",
  ],
  ["human", "Username: {userName}"],
]);



const model = new ChatGoogleGenerativeAI({
  model: "gemini-2.5-flash",
  apiKey: "AQ.Ab8RN6KsDfP1bfF6feE0Kl-QJMcB7NSDSV7yjQGx95dMyuUqeg",
  temperature: 1.7,
});

const structuredModel = model.withStructuredOutput(responseSchema);
function saveToDb(data){
    console.log("saving data to db",data)
    return data
}

// const response = await structuredModel.invoke(fullPrompt);

let chainModel = prompt.pipe(structuredModel).pipe(saveToDb);

const response = await chainModel.invoke({
    userName:"Pragyan babuwa"
})
console.log(response)