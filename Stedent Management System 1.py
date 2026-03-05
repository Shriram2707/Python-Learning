students = {
    "101": {"name": "Ganesh",
            "marks": {"Math": 85, "Science": 90, "English": 78, "Physics": 87, "Chemistry": 78, "Computer": 77}},
    "102": {"name": "Karthik",
            "marks": {"Math": 70, "Science": 85, "English": 80, "Physics": 92, "Chemistry": 80, "Computer": 89}},
    "103": {"name": "Shiva",
            "marks": {"Math": 72, "Science": 75, "English": 81, "Physics": 84, "Chemistry": 86, "Computer": 95}},
    "104": {"name": "Parvathi",
            "marks": {"Math": 73, "Science": 85, "English": 82, "Physics": 76, "Chemistry": 83, "Computer": 76}},
    "105": {"name": "Vishnu",
            "marks": {"Math": 74, "Science": 67, "English": 83, "Physics": 73, "Chemistry": 82, "Computer": 77}},
    "106": {"name": "Lakshmi",
            "marks": {"Math": 75, "Science": 95, "English": 84, "Physics": 82, "Chemistry": 81, "Computer": 82}},
    "107": {"name": "Indran",
            "marks": {"Math": 87, "Science": 85, "English": 85, "Physics": 80, "Chemistry": 80, "Computer": 81}},
    "108": {"name": "Keshav",
            "marks": {"Math": 80, "Science": 75, "English": 86, "Physics": 77, "Chemistry": 79, "Computer": 84}},
    "109": {"name": "Bhagya",
            "marks": {"Math": 90, "Science": 65, "English": 87, "Physics": 79, "Chemistry": 78, "Computer": 80}}
}

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print(
        "1. Add Student\n2. View All Students\n3. Search Student\n4. Calculate Result\n5. Show Unique Subjects\n6. Exit")

    choice = input("\nPlease enter your choice (1-6): ")

    if choice == '1':
        s_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        # Inputting all subjects for the new student
        m = int(input("Math: "))
        s = int(input("Science: "))
        e = int(input("English: "))
        p = int(input("Physics: "))
        ch = int(input("Chemistry: "))
        co = int(input("Computer: "))

        students[s_id] = {
            "name": name,
            "marks": {"Math": m, "Science": s, "English": e, "Physics": p, "Chemistry": ch, "Computer": co}
        }
        print(f"Student {name} added successfully!")

    elif choice == '2':
        print("\nID\tName\t\tMarks")
        for s_id, info in students.items():
            print(f"{s_id}\t{info['name']}\t{info['marks']}")

    elif choice == '3':
        s_id = input("Enter ID to search: ")
        if s_id in students:
            print(f"Found: {students[s_id]['name']} | Marks: {students[s_id]['marks']}")
        else:
            print("Error: Student ID not found.")

    elif choice == '4':
        s_id = input("Enter Student ID for Result: ")
        if s_id in students:
            marks_dict = students[s_id]["marks"]
            total = sum(marks_dict.values())
            count = len(marks_dict)
            avg = total / count

            if avg >= 90:
                grade = "A"
            elif avg >= 80:
                grade = "B"
            elif avg >= 70:
                grade = "C"
            else:
                grade = "D"

            print(f"\nStudent: {students[s_id]['name']}")
            print(f"Average: {avg:.2f} | Grade: {grade}")
        else:
            print("Student ID not found!")

    elif choice == '5':
        all_subjects = set()
        for info in students.values():
            all_subjects.update(info['marks'].keys())
        print("Unique Subjects in System:", ", ".join(all_subjects))

    elif choice == '6':
        print("Exiting program. Goodbye!")
        break