from langchain_google_genai import ChatGoogleGenerativeAI


class IntentAgent:

    def __init__(self, api_key):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=api_key
        )

    def classify(self, query):

        prompt = f"""
You are an Intent Classification Agent.

Identify ONLY the primary seller issue.

Choose ONLY one of the following:

- VAT Registration
- Belgium JSL
- Tax Verification
- VAT Invoice
- Tax Document Upload
- Entity Change
- General Tax Query

Return ONLY the category name.

Seller Query:
{query}
"""

        response = self.llm.invoke(prompt)

        return response.content.strip()