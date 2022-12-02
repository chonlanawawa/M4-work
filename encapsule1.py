class Student:
    def __init__(self, number, score):
        self.number = number
        self.__score = score

stu = Student('No.2', 10)

print('Student Number:', stu.number)
print('Score:', stu._Student__score)