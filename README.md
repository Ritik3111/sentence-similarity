## Sentence Similarity API

The Sentence Similarity API is a RESTful web service that allows users to compare the similarity between a single sentence and a list of comparison sentences. This API is built using Python and the Flask web framework, and it leverages the SentenceTransformer and scikit-learn libraries to compute the cosine similarity between the sentences.

### How to Use

To use the Sentence Similarity API, you will need to send a POST request to the API endpoint with a JSON payload that contains two parameters:

1. `query_sentence` - the single sentence to compare against the comparison sentences
2. `comparison_sentences` - a list of sentences to compare against the query sentence

The API endpoint will return a JSON response that contains an array of objects, each with two parameters:

1. `sentence` - the sentence from the comparison sentences
2. `similarity_score` - the cosine similarity score between the query sentence and the corresponding comparison sentence

If an error occurs, the API will return a 500 error code and a message explaining the error.

### Core Functionality

The core sentence similarity function used to compute the scores encodes the query sentence and the comparison sentences using the SentenceTransformer library, and then computes the cosine similarity between the query sentence embedding and the comparison sentence embeddings using the scikit-learn library. The similarity score is a value between -1 and 1, where 1 means the sentences are identical, 0 means they are completely dissimilar, and -1 means they are opposite in meaning.

### Limitations

There are a few limitations to consider when using the Sentence Similarity API. Firstly, the model used by the SentenceTransformer library may not be able to capture the nuances of all sentences, and the quality of the similarity scores may depend on the quality and quantity of the data used to train the model. Additionally, the API may not be able to handle large amounts of data due to resource constraints.

### Installation

To install the Sentence Similarity API, follow these steps:

1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Start the server using `python similarity.py`.

The API will then be accessible at `http://localhost:4000/`.

### Conclusion

The Sentence Similarity API provides a simple and easy-to-use way to compare the similarity between sentences. By leveraging state-of-the-art NLP models and libraries, it allows users to quickly and accurately compute similarity scores, making it a valuable tool for a wide range of applications.