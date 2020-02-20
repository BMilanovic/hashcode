class LSS:

    def __init__(self, reg):
        self.reg = reg
        return self

    def buildResult(self):
        signup_queue = self.build_signup_queue()
        result = self.build_final_result(signup_queue)
        return result

    def build_signup_queue(self):
        signup_queue = []
        max_score = reg.max_score
        for score in sorted(reg.scores.keys()):
            for lib in reg.scores[score]:
                signup_queue.append(lib)

        return signup_queue

    def build_final_result(self):
        final_restult = []
        for lib in signup_queue:
            final_restult.append([lib, lib.unscanned_books])
        return
