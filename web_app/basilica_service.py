import basilica
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('BASILICA_API_KEY') 

connection = Connection(API_KEY)

if __name__ == "__main__":
    sentences = ["Hello world!", "How are you?"]
    embeddings = connection.embed_sentences(sentences)
    print(type(embeddings))
    for embedding in embeddings:
        print(len(embedding)) #> 768
        print(list(embedding)) # [[0.8556405305862427, ...], ...]
        print("-------------")

