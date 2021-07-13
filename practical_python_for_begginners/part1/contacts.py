contacts = {
    "number":4,
    "students":
    [
        {"name":"sarah","email":"sara@gmail.com"},
        {"name":"pjoi","email":"pjoi@gmail.com"},
        {"name":"matt","email":"matt@gmail.com"},
        {"name":"mike","email":"mike@gmail.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])