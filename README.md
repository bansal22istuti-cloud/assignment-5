## Assignment-5
this repository contains two task each for the assignment 5 of tutedude python program

## Task 1
this task aims to create a dictionary where student names are keys and their marks are values.it should ask the user to input a student's name and retrieve and display the corresponding marks. if the student’s name is not found, display an appropriate message.

## Program of task 1

[ass5task1.py](https://github.com/user-attachments/files/24347770/ass5task1.py)


students={'alice':95,'john':63,'sanjay':98}
name=input("enter the student name: ")

if name in students:
        print(f"marks of {name} are: {students[name]}")
else:
        print("student not found")

input("press enter to exit")



## Explanation of task 1 program

here first a dictionary was created and then user input gives the key which is needed to be found in the dictinary and by if else condition staement it is determined whether the value of the dictionary is printed or error statement is issued

## Task 2
this task aims to create a list of numbers from 1 to 10 and extract the first five elements from the list and then reverses these extracted elements. it should print both the extracted list and the reversed list


## Program of task 2

[ass5task2.py](https://github.com/user-attachments/files/24347774/ass5task2.py)


num=[]
for i in range(1,11):
    num.append(i)
print(f'original list:{num}')
forward=num[0:5]
print(f'extracted first five elements:{forward}')
forward.reverse()
print(f'extracted last five elements:{forward}')
input("press enter to exit")

## Explanation of task 2 program
here with the help of for loop in the empty list num and then with the help of slicing first five elements are printed and then by reverse function the extracted list is reversed and printed.

## Status
it has been verified before submission that the program runs successfully.
