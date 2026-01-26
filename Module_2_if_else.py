#Sai_K_Kham
#Module_2_if_else
#This app caculate the GPA of students and determine if the student has made Dean's List or Honor List
l_name = input('Enter your last name: ')
if l_name == 'ZZZ':
    quit()
f_name = input('Enter your first name: ')
GPA = float(input('Enter your GPA: '))
if GPA >= 3.5:
    print(f"{f_name} {l_name} has made the Dean's List")
elif GPA >= 3.25:
    print(f"{f_name} {l_name} has made the Honor List")
else:
    print(f"{f_name} {l_name} GPA is {GPA}")
