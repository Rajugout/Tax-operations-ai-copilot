from langchain_google_genai import ChatGoogleGenerativeAI


class ResolutionAgent:

    def __init__(self, api_key):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=api_key
        )

    def resolve(self, query, context):

        prompt = f"""
You are a Resolution Agent.

Using ONLY the context below, provide the best resolution for the analyst.

Seller Query:
{query}

Context:
{context}

Return ONLY the recommended resolution in bullet points.
"""

        response = self.llm.invoke(prompt)

        return response.content.strip()