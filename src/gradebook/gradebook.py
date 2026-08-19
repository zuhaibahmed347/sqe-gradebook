class Student:
    def __init__(self, name, roll_no, scores):
        self.name = name
        self.roll_no = roll_no
        self.scores = scores

    def add_score(self, student_score):
        """Add a valid score to the student's scores."""
        if not isinstance(student_score, (int, float)):
            raise ValueError("Score must be numeric")
        if student_score < 0 or student_score > 100:
            raise ValueError("Score must be between 0 and 100") 

            self.scores.append(student_score)