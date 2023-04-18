from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load pre-trained sentence transformer model
model = SentenceTransformer('bert-base-nli-mean-tokens')

@app.route('/sentence-similarity', methods=['POST'])
def sentence_similarity():
    """
    Returns similarity of sentence with other sentences

    Returns:
        response(json): sentence with similarity score
    """
    try:
        # Parse request payload
        payload = request.json
        query_sentence = payload['query_sentence']
        comparison_sentences = payload['comparison_sentences']

        # Encode query sentence and comparison sentences
        query_embedding = model.encode([query_sentence], convert_to_tensor=False)[0]
        comparison_embeddings = model.encode(comparison_sentences, convert_to_tensor=False)

        # Compute similarity scores for comparison sentences
        sim = cosine_similarity(query_embedding.reshape(1,-1), comparison_embeddings)
        # Create response payload
        response = []

        for index,item in enumerate(comparison_sentences):
            result = {
                "sentence": item,
                "similarity_score": sim[0][index].item()
            }
            response.append(result)

        return jsonify(response)

    except Exception as err:
        # Handle exceptions and return error response
        return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=4000)
