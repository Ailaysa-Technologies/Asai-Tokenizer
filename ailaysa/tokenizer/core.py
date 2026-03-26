class TokenOutput:
    def __init__(self, encoding):
        self.ids = encoding.ids
        self.tokens = encoding.tokens
        self.length = len(encoding.ids)