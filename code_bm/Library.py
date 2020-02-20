class Library:
    id = 0
    signup_days = 0
    books_per_day = 0
    number_of_books = 0
    books = []

    popularity_first_25 = 0
    popularity_last_75 = 0
    popularity_mean = 0

    def __init__(self, id, signup_days, books_per_day, number_of_books, books):
        self.id = id
        self.signup_days = signup_days
        self.books_per_day = books_per_day
        self.number_of_books = number_of_books
        self.books = sorted(books, key=lambda x: x.score, reverse=True)

    def unscanned_books(self):
        return [book for book in self.books if book.scanned == False]

    def evaluate_books(self):
        z = 0
        sum_25 = 0
        sum_75 = 0
        sum_all = 0
        first_sector_size = self.number_of_books * 0.25
        for book in self.books:
            if z < first_sector_size:
                sum_25 += book.score
            else:
                sum_75 += book.score
            sum_all += book.score

        self.popularity_first_25 = sum_25/first_sector_size
        self.popularity_last_75 = sum_75/(self.number_of_books - first_sector_size)
        self.popularity_mean = sum_all/self.number_of_books
