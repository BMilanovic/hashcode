class Book:
    id = 0
    score = 0

    def __init__(self, id, score):
        self.id = id
        self.score = score
        self.scanned = False

    def mark_as_scanned(self):
        self.scanned = True
