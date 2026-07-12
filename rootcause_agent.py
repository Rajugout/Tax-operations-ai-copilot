from langchain_google_genai import ChatGoogleGenerativeAI


class RootCauseAgent:

    def __init__(self, api_key):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=api_key
        )

    def analyze(self, query, context):

        prompt = f"""
You are a Root Cause Analysis Agent.

Based ONLY on the context, identify the most likely root cause.

Seller Query:
{query}

Context:
{context}

Return ONLY the root cause in 2-3 sentences.
"""

        response = self.llm.invoke(prompt)

        return response.content.strip()