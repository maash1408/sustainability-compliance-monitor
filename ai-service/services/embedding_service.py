from sentence_transformers import SentenceTransformer

model = None


def load_model():
    global model

    if model is None:
        print("Loading sentence transformer model...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        print("Sentence transformer loaded successfully")

    return model


def generate_embedding(text):
    global model

    if model is None:
        load_model()

    return model.encode(text).tolist()