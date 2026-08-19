class Student:
    def __init__(self, name2, id_number ):
        self.name = name2
        self.roll_no = id_number
        self.scores = []

    def average(self):
        if not self.scores:
            return 0.0

        return sum(self.scores) / len(self.scores)

    #  this is the new file where I make changes
