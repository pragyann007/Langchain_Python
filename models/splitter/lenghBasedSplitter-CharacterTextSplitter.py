from langchain_text_splitters import CharacterTextSplitter

text = """
    The blue lantern flickered against the cold stone wall, casting long, dancing shadows across the quiet hallway. Outside, a gentle breeze rustled the autumn leaves as they drifted past the frosted windowpane. A solitary clock chimed softly in the corner, marking the slow and steady passage of time in an otherwise silent room.        
"""

splitter = CharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=0,
    separator=""
)

res = splitter.split_text(text)
print(res)