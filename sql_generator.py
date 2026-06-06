from groq import Groq
from examples import examples
from vector_store import collection, model
import os
from dotenv import load_dotenv


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


SCHEMA = """
PRODUCTS(
 PRODUCT_ID NUMBER,
 PRODUCT_NAME VARCHAR2,
 CATEGORY VARCHAR2,
 PRICE NUMBER,
 STOCK NUMBER
)

CUSTOMERS(
 CUSTOMER_ID NUMBER,
 CUSTOMER_NAME VARCHAR2,
 CITY VARCHAR2
)

ORDERS(
 ORDER_ID NUMBER,
 CUSTOMER_ID NUMBER,
 ORDER_DATE DATE
)

ORDER_ITEMS(
 ORDER_ITEM_ID NUMBER,
 ORDER_ID NUMBER,
 PRODUCT_ID NUMBER,
 QUANTITY NUMBER
)
"""


def get_similar_examples(question):

    embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    retrieved = []

    for doc in results["documents"][0]:

        for e in examples:

            if e["question"] == doc:
                retrieved.append(e)

    return retrieved


def generate_sql(question):

    similar_examples = get_similar_examples(question)

    few_shot = "\n\n".join(
        [
            f"Question: {e['question']}\nSQL: {e['sql']}"
            for e in similar_examples
        ]
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"""
                                  You are an Oracle SQL expert.

                                  Database Schema:

                                  {SCHEMA}

                                  Examples:

                                  {few_shot}

                                  Return ONLY SQL.
                                  Do not explain.
                                  Do not use markdown.
                                  """
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()