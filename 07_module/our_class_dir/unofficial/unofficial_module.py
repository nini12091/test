import random
import our_class_dir.official.official_module

def study():
    print(f"{our_class_dir.official.official_module.student_count}명의 학생들이 열심히 공부를 한다!")

def go_lunch(menus):
    return random.choice(menus)

study()
menus = ['한식','중식','양식','일식','디저트']
print(go_lunch(menus))