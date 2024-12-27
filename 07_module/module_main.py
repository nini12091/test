# import our_class

# print(our_class.teacher_name, our_class.student_count)
# our_class.study()
# our_class.lecture()

# menus = ['한식','중식','양식','일식','디저트']
# print(our_class.go_lunch(menus))

from our_class import teacher_name, student_count, study, lecture, go_lunch

print(teacher_name, student_count)
study()
lecture()

menus = ['한식','중식','양식','일식','디저트']
print(go_lunch(menus))