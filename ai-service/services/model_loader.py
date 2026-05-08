from sentence_transformers import SentenceTransformer
import logging
import time

logger = logging.getLogger(__name__)

model = None
startup_time = None


def load_model():
    global model
    global startup_time

    try:
        start = time.time()

        logger.info("Loading sentence transformer model...")

        model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        startup_time = round(time.time() - start, 2)

        logger.info(
            f"Sentence transformer loaded in {startup_time}s"
        )

    except Exception as e:
        logger.error(f"Model loading failed: {str(e)}")


def get_model():
    return model