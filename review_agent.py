from langchain_google_genai import ChatGoogleGenerativeAI


class ReviewAgent:

    def __init__(self, api_key):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=api_key
        )

    def review(self, query, context, response):

        prompt = f"""
You are a Review Agent.

Review the generated response.

Check:

1. Is it supported by the context?
2. Is it complete?
3. Give a confidence score out of 100.

Context:
{context}

Seller Query:
{query}

Generated Response:
{response}

Return exactly:

Validation:
Confidence:
Remarks:
"""

        result = self.llm.invoke(prompt)

        return result.content.strip()