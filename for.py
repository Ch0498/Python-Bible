print("Student Search Engine")
students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

while True:
    search = input("Enter a Letter to find the students havivng that letter coman in them")
    for key in students.keys():
        for name in students[key]:
            if search in name:
                print(name)
