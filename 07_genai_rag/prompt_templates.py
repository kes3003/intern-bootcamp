"""
prompt_templates.py
Day 3 - LangChain Prompt Templates & Automation (2025 compatible)
"""

import os
from dotenv import load_dotenv

# New LangChain imports (2024–2025)
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence


# ---------------------------------------------------------
# Load API key
# ---------------------------------------------------------

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini",
    temperature=0.3
)


# ---------------------------------------------------------
# Template 1 — Markdown Summary
# ---------------------------------------------------------

summary_template = PromptTemplate(
    input_variables=["markdown_text"],
    template="""
You are an assistant that summarizes bakery business notes.

Summarize the following markdown content in 5 bullet points:

Markdown:
{markdown_text}
"""
)

summary_chain = (
    summary_template
    | llm
)


def summarize_markdown(text: str):
    """Summarizes markdown text using LangChain PromptTemplate."""
    return summary_chain.invoke({"markdown_text": text}).content


# ---------------------------------------------------------
# Template 2 — Keyword Extraction
# ---------------------------------------------------------

keyword_template = PromptTemplate(
    input_variables=["product_text"],
    template="""
Extract 5–8 keywords from the following bakery product description.
Return them as a comma-separated list.

Product description:
{product_text}
"""
)

keyword_chain = (
    keyword_template
    | llm
)


def extract_keywords(text: str):
    """Extracts keywords from product descriptions."""
    return keyword_chain.invoke({"product_text": text}).content


# ---------------------------------------------------------
# Optional Test Block
# ---------------------------------------------------------

if __name__ == "__main__":
    sample_md = """
    ## Baking Notes
    - Introduced a new blueberry cheesecake
    - Customer complaints about dry sponge cake continue
    - Need to improve delivery speed
    - Chocolate tart sales increased this week
    """

    sample_desc = "Fresh blueberry cheesecake with butter crust and vanilla whipped cream."

    print("SUMMARY OUTPUT:\n", summarize_markdown(sample_md))
    print("\nKEYWORDS OUTPUT:\n", extract_keywords(sample_desc))
