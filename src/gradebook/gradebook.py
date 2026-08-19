class Student:
    def __init__(self, name, roll_no, scores):
        self.name = name
        self.roll_no = roll_no
        self.scores = scores

    def add_score(self, score):
        """Add a score to the student's scores after validating it."""
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score)