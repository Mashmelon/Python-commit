  def __init__(self, sid, name, age, grade, subjects):
        self.sid = sid
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects  

    def total_marks(self):
        return sum(self.subjects.values())

    def __str__(self):
        return f"{self.sid} → {self.name} | Total: {self.total_marks()}"

    def __repr__(self):
        return self.__str__()
