from langchain_google_genai import ChatGoogleGenerativeAI


class ResponseAgent:

    def __init__(self, api_key):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=api_key
        )

    def generate(self, query, context):

        prompt = f"""
You are a Seller Response Agent.

Using ONLY the context below, write a professional response that the analyst can send to the seller.

Seller Query:
{query}

Context:
{context}

Return ONLY the seller response.
"""

        response = self.llm.invoke(prompt)

        return response.content.strip()