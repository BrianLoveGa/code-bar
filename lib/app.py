# Write your code here!


class Member:
    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        print(f"Hi there, my name is {self.full_name}! whazzup?")   
        
      


class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.type = "Student"
        self.reason = reason


class Instructor(Member):
    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio = bio
        self.type = "Instructor"
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)
        return self.skills


jane = Student(
    "Jane Doe", "I am trying to learn programming and need some help.")
jane.introduce()

#      where is this mystery None coming from ?
#      it was from trying to print a function that is a print
#      like the mystery undefined when you console log a console log in JS


print()  # love skipping lines with these empty prints

print(jane.full_name +',', jane.reason)     ### no errors no nuns

lena = Student("Lena Smith", "I am really excited about learning to program!")

print()
lena.introduce()
print()
print(lena.reason)   

vicky = Instructor("Vicky Python", "I want to help people learn coding.")

vicky.add_skill("HTML")

vicky.add_skill("JavaScript")

print()

print(vicky.skills)    

print()
vicky.introduce()
print()
print(vicky.bio)     

nicole = Instructor(
    "Nicole McMillan", """I have been programming for 5 
    years in Python and want to spread the love.""")

nicole.add_skill("Python") 

print()

print(nicole.bio, nicole.skills)

print()

nicole.introduce()       

print()

print("Members, Students and Instructors welcome to the code bar")

print()


class Workshop():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def info(self):
        print(f"Workshop - {self.date} - {self.subject}")

    def add_participant(self, member):
        if member.type == "Student":
            self.students.append(member)
        elif member.type == "Instructor":
            self.instructors.append(member)

    def print_students(self):
        s_index = 1
        print("Students")
        for student in self.students:
            print(f"{s_index}. {student.full_name}, {student.reason}")
            s_index += 1

    def print_instructors(self):
        i_index = 1
        print("Instructors")
        for instructor in self.instructors:
            print(
                f"""{i_index}. {instructor.full_name} - 
                {instructor.skills} \n {instructor.bio}""")
            i_index += 1

    def print_details(self):
        self.info()
        self.print_students()
        self.print_instructors()


print()

print()

workshop = Workshop("12/03/2014", "Shutl")
workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()

print()

wrkshp = Workshop("10/31/2019", "Python-pong-game")
wrkshp.add_participant(jane)
wrkshp.add_participant(lena)
wrkshp.add_participant(nicole)
wrkshp.print_details()
