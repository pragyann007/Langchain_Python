from typing import List
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from pydantic import BaseModel, Field

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


class MovieRecommendation(BaseModel):
    title: str = Field(description="Name of movie")
    year: int = Field(description="Release year")
    reason: str = Field(description="Reason for selecting this movie")


class MovieResponse(BaseModel):
    recommendations: List[MovieRecommendation] = Field(
        description="List of recommended movies"
    )

chat = ChatPromptTemplate([{rol}])

template = PromptTemplate(
    template="Suggest the best movies of this genre: {genre}",
    input_variables=["genre"]
)


genre = input("Enter movie genre: ")

prompt = template.invoke({
    "genre": genre
})


structured_model = model.with_structured_output(MovieResponse)

res = structured_model.invoke(prompt)

sRes = res.model_dump()

print(sRes)