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
        return

    def calculate_dynamic_score(self):
        return

    def calculate_total_score(self):
        return