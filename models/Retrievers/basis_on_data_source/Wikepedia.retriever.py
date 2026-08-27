from langchain_community.retrievers import WikipediaRetriever

# 1. Use short keywords instead of a full conversational prompt
# 2. Set doc_content_chars_max if you want to limit text length
retriever = WikipediaRetriever(
    top_k_results=3,
    lang="en",
    doc_content_chars_max=1000
)

# Set a custom user-agent on the underlying wrapper to avoid Wikipedia API 403 blocks
retriever.wiki_client.USER_AGENT = "MyLangChainApp/1.0 (contact@example.com)"

# Pass concise search terms instead of a conversational sentence
docs = retriever.invoke("Blockchain future trends")

for doc in docs:
    print(f"Title: {doc.metadata['title']}\n")
    print(doc.page_content[:200] + "...\n" + "-"*40)