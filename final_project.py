import statistics as s

admin = {"Peter": "Python1",
         "Paul": "Python2"
         }

studentList = {
    'Alex' : [92, 76, 88],
    'Jeff' : [78, 88, 93],
    'Sam' : [89, 92, 93]
    }


def main ():
        print(
        '''
            Welcome to grade central

            [1] - Enter Grades
            [2] - Remove Student
            [3] - Student Average Grades
            [4] - Exit
        '''
            )
        action = input('What would you like to do, please enter a number: ')

        if action == '1':
            addGrade = input('please enter student name: ')
            if addGrade in studentList:
                gradeValue = input('please enter grade: ')
                studentList[addGrade].append(float(gradeValue))
            else:
                print('invalid student name')
        elif action == '2':
            removeStudent = input('Please enter student name to delete: ')
            del studentList[removeStudent]
            print(studentList)
        elif action == '3':
            print(s.mean(studentList))
        elif action == '4':
            print('exit')
        else:
            print('invalid selection')
                  


userName = input('Please enter your user name: ')

if userName in admin:
    passW = input('Please enter your password: ')
    if admin[userName]== passW:
        main()
    else:
        print('Invalid password')
else:
    print('Invalid user name')

   







