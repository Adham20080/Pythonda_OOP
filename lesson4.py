class Shaxs:
    def __init__(self, ism, famlily, age, passport, gender):
        self.ism = ism
        self.famlily = famlily
        self.age = age
        self.passport = passport
        self.gender = gender

    def get_passport(self):
        return self.passport


obj = Shaxs("Akbar", "Akbarov", 27, "AB123434", "Male")


class Student(Shaxs):
    def __init__(self, student_id, student_username, ism, famlily, age, passport, gender):
        super().__init__(ism, famlily, age, passport, gender)
        self.student_id = student_id
        self.student_username = student_username

