
import {ChatGoogleGenerativeAI} from "@langchain/google-genai"
import {Annotation, StateGraph} from "@langchain/langgraph"

const model = new ChatGoogleGenerativeAI({
    model:"gemini-2.5-flash",
})

const state = Annotation.Root({
    prompt:Annotation,
    aiMsg:Annotation
})

const callLlm = async(state)=>{
    const response =await model.invoke([
        {
            role:"system",
            content:"You are useful jarvis assistant that greets user in 4 langauges , japaness , korean , chineese ,russian with users name saying how are you and extra cultural note "
        },
        {
            role:"human",
            content:`User name : ${state.prompt}`
        }
    ])

    return {aiMsg:response.content};
}

const graph = new StateGraph(state)
.addNode("agent",callLlm)
.addEdge("__start__","agent")
.addEdge("agent","__end__")
.compile();

const response =await graph.invoke({prompt:"desi kalakar pragyan chaprii"})
console.log(response);

