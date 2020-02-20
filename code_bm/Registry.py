class Registry:

    libs = []
    total_score = {}
    static_score = {}
    dynamic_score = {}

    def __init__(self, libs):
        self.libs = libs
        return self

    def calculate(self):
        self.calculate_static_score()
        self.calculate_dynamic_score()
        self.calculate_total_score()
        return self

    def calculate_static_score(self):
        for lib in self.libs:
            lib.signup_days
            lib.books_per_day
            lib.number_of_books

            days_to_complete = lib.number_of_books / lib.books_per_day
            total_days = lib.signup_days + days_to_complete

            # score needs the score of books in each lib
            # [most popular] [popular] [not popular]

            score = 0

    def calculate_dynamic_score(self):
        return

    def calculate_total_score(self):
        return