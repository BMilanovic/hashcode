class Registry:

    libs = []
    total_score = {}
    score = {}
    min_score = 0
    static_score = {}
    dynamic_score = {}

    ALPHA = 0.33
    BETA = 0.33
    GAMMA = 0.33

    TOTAL_A = 0.5
    TOTAL_B = 0.5

    def __init__(self, libs):
        self.libs = libs

    def calculate(self):
        for lib in self.libs:
            self.calculate_static_score(lib)
            self.calculate_dynamic_score(lib)
            self.calculate_total_score(lib)

    def calculate_static_score(self, lib):
        days_to_complete = lib.number_of_books / lib.books_per_day
        total_days = lib.signup_days + days_to_complete

        score_a = 1.0 / total_days
        print(score_a)
        score_b = 1.0 / lib.popularity_first_25 if lib.popularity_first_25 else 1.0
        score_c = 1.0 / lib.popularity_mean if lib.popularity_mean else 1.0

        self.static_score[lib.id] = self.ALPHA * score_a + self.BETA * score_b + self.GAMMA * score_c

    def calculate_dynamic_score(self, lib):
        days_to_complete = lib.number_of_books / lib.books_per_day
        total_days = lib.signup_days + days_to_complete

        self.dynamic_score[lib.id] = 1. / (lib.popularity_mean*lib.number_of_books / total_days) if lib.popularity_mean else 1.0

    def calculate_total_score(self, lib):
        score = self.TOTAL_A * self.static_score[lib.id] + self.TOTAL_B * self.dynamic_score[lib.id]
        if score < self.min_score:
            self.min_score = score

        self.total_score[lib.id] = score
        if score in self.score:
            self.score[score].append(lib)
        else:
            self.score[score] = [lib]
