class RetrieverAgent:

    def __init__(self, retriever):
        self.retriever = retriever

    def retrieve(self, query):

        docs = self.retriever.invoke(query)

        pages = []

        for doc in docs:

            page = doc.metadata.get("page", 0) + 1

            if page not in pages:
                pages.append(page)

        return docs, pages