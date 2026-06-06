from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from examples import examples

client = PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="sql_examples"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Populating only once 

if collection.count() == 0:

    questions = [
        e["question"]
        for e in examples
    ]

    embeddings = model.encode(
        questions
    ).tolist()

    collection.add(
        ids=[str(i) for i in range(len(examples))],
        documents=questions,
        embeddings=embeddings
    )

print("Vector Store Ready")