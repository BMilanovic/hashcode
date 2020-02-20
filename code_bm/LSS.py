class LSS:

    def __init__(self, reg):
        self.reg = reg

    def buildResult(self):
        signup_queue = self.build_signup_queue()
        result = self.build_final_result(signup_queue)
        return result

    def build_signup_queue(self):
        signup_queue = []
        # max_score = self.reg.min_score
        for scored in sorted(self.reg.score.keys()):
            for lib in self.reg.score[scored]:
                signup_queue.append(lib)

        return signup_queue

    def build_final_result(self):
        final_restult = []
        for lib in self.build_signup_queue():
            final_restult.append([lib, lib.unscanned_books()])
            for book in lib.unscanned_books():
                book.mark_as_scanned()
        return final_restult
