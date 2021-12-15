student_list = []
lecturer_list = []


def comparison_stud(name_course, student_list=student_list):
    sum_grade = 0
    len_grade = 0
    for i in student_list:
        for j in i.grades[name_course]:
            sum_grade += j
            len_grade += 1
    return sum_grade / len_grade


def comparison_lecturer(name_course, lecturer_list=lecturer_list):
    sum_grade = 0
    len_grade = 0
    for i in lecturer_list:
        for j in i.grades[name_course]:
            sum_grade += j
            len_grade += 1
    return sum_grade / len_grade


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('нельзя сравнивать студентов с преподавателями')
        return self.grade_average_stu() > other.grade_average_stu()

    def grade_average_stu(self):
        sum_grades = 0
        len_grades = 0
        for i in self.grades:
            sum_grades += sum(self.grades[i])
            len_grades += len(self.grades[i])
        return round(sum_grades / len_grades, 1)

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lectur(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.grade_average_stu()} \nКурсы в процессе изучения:{str(', '.join(self.courses_in_progress))} \nЗавершенные курсы: {str(''.join(self.finished_courses))}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        # self.grade_average = grade_average()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('нельзя сравнивать студентов с преподавателями')
        return self.grade_average_lect() > other.grade_average_lect()

    def grade_average_lect(self):
        sum_grades = 0
        len_grades = 0
        for i in self.grades:
            sum_grades += sum(self.grades[i])
            len_grades += len(self.grades[i])
        return round(sum_grades / len_grades, 1)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grade_average_lect()}'
        return res


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


# def comparison (person1, person2):
# else person1.grade_average() > person2.grade_average():
# return ""


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
student_list.append(best_student)
student_2 = Student('Сидр', 'Сидоров', 'denger_3')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses = ['Введение в программирование']
student_list.append(student_2)

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

reviewer_1 = Reviewer('Иван', 'Иванов')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Василий', 'Васильев')
reviewer_2.courses_attached += ['Python']

lecturer_1 = Lecturer('Пётр', 'Петров')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Семен', 'Семенов')
lecturer_2.courses_attached += ['Python']
lecturer_list.append(lecturer_1)
lecturer_list.append(lecturer_2)

reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(best_student, 'Python', 8)
reviewer_1.rate_hw(best_student, 'Python', 9)
reviewer_1.rate_hw(best_student, 'Python', 8)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(best_student, 'Python', 10)
reviewer_2.rate_hw(best_student, 'Python', 10)
reviewer_2.rate_hw(best_student, 'Python', 10)

best_student.rate_lectur(lecturer_1, 'Python', 9)
best_student.rate_lectur(lecturer_1, 'Python', 10)
best_student.rate_lectur(lecturer_1, 'Python', 10)
student_2.rate_lectur(lecturer_1, 'Python', 10)
student_2.rate_lectur(lecturer_1, 'Python', 10)
student_2.rate_lectur(lecturer_1, 'Python', 10)
best_student.rate_lectur(lecturer_2, 'Python', 9)
best_student.rate_lectur(lecturer_2, 'Python', 10)
best_student.rate_lectur(lecturer_2, 'Python', 10)
student_2.rate_lectur(lecturer_2, 'Python', 9)
student_2.rate_lectur(lecturer_2, 'Python', 10)
student_2.rate_lectur(lecturer_2, 'Python', 10)

# print(lecturer_1.grades)
# print(best_student.grades)
# print(reviewer_1)
# print(lecturer_2)
# print(best_student)
# print(best_student < student_2)
# print(lecturer_1 < lecturer_2)
# print(lecturer_list)
# print(comparison_stud('Python'))
print(comparison_lecturer('Python'))
