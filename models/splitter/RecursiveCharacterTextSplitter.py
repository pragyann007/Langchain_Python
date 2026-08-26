from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
    The blue lantern flickered against the cold stone wall casting long, dancing shadows  
    across the quiet hallway Outside, a gentle breeze rustled the autumn leaves as they  drifted past the frosted windowpane
    \n\n
      A solitary clock chimed softly in the corner marking the slow and steady passage of time in an otherwise silent room      
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
    separators=["\n\n","\n","-",""]
)

print(splitter.split_text(text))