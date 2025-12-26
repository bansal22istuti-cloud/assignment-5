students={'alice':95,'john':63,'sanjay':98}
name=input("enter the student name: ")

if name in students:
        print(f"marks of {name} are: {students[name]}")
else:
        print("student not found")

input("press enter to exit")

