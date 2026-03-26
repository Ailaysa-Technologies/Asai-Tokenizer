import os
import sentencepiece as spm

MODEL_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "models")
)

class TokenOutput:
    def __init__(self, ids, tokens):
        self.ids = ids
        self.tokens = tokens
        self.length = len(ids)

class TokenizerWrapper:
    def __init__(self, model_path):
        self.sp = spm.SentencePieceProcessor()
        self.sp.load(model_path)

    def encode(self, text):
        ids = self.sp.encode(text, out_type=int)
        tokens = self.sp.encode(text, out_type=str)
        return TokenOutput(ids, tokens)

def load(name: str):
    if name == "asai-v1":
        model_path = os.path.join(MODEL_DIR, "asai-v1.model")

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}")

        return TokenizerWrapper(model_path)

    else:
        raise ValueError(f"Model '{name}' not found")