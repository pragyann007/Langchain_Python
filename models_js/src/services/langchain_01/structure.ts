import {ChatGoogleGenerativeAI} from "@langchain/google-genai"
import {z} from "zod"
import "dotenv/config"

let response = z.object({
    name:z.string(),
    age:z.number(),
    skills:z.array(z.string()),
    summary:z.string()
})
const model = new ChatGoogleGenerativeAI({
    model:"gemini-2.5-flash",
})


const struct_model = model.withStructuredOutput(response);
const ress = await struct_model.invoke("My name is pragyan thapaliya i am 18 yo old mern stack nest js backend focused ull stack developer")

console.log(ress)