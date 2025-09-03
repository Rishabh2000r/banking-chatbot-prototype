from sentence_transformers import SentenceTransformer, util
import json


with open('data/faq_dataset.json', 'r') as f:
    faq_data = json.load(f)

model = SentenceTransformer('all-MiniLM-L6-v2')

faq_embeddings = model.encode([item['question'] for item in faq_data])

def get_answer(query):

    query_embedding = model.encode(query)

    # Calculate cosine similarity
    cos_scores = util.cos_sim(query_embedding, faq_embeddings)[0]

    top_result = cos_scores.argmax()

    return faq_data[top_result]['answer']
