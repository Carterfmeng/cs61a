class Instructor:
    degree = "PhD (Magic)"  # this is a class attribute

    def __init__(self, name):
        self.name = name  # this is an instance attribute

    def lecture(self, topic):
        print("Today we're learning about " + topic)


dumbledore = Instructor("Dumbledore")


class Student:
    instructor = dumbledore

    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        ta.add_student(self)

    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        if Student.instructor == dumbledore:
            print(Student.instructor.name + " is awesome!")
        else:
            print("I miss Dumbledore.")
        self.understanding += 1

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)


class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True  # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def __init__(self, name, owner):
        Pet.__init__(self, name, owner)

    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives
        if self.lives > 0:
            self.is_alive = True
        else:
            self.is_alive = False

    def talk(self):
        """A cat says meow! when asked to talk."""
        print(self.name + ' says meow!')

    def lose_life(self):
        """A cat can only lose a life if they have atleast one life.
        When lives reaches zero, 'is_alive'becomes False."""
        if self.lives > 0:
            self.lives -= 1
        if self.lives == 0:
            self.is_alive = False


class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    # def __init__(self, name, owner, lives=9):
    # Is this method necessary? Why or why not? Not necessary
    # Cat.__init__(self, name, owner, lives)

    def talk(self):
        """Repeat what a Cat says twice."""
        for _ in range(2):
            Cat.talk(self)


class A:
    def f(self):
        return 2

    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)


class B(A):
    def f(self):
        return 4
