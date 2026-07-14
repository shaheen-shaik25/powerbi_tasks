def list_example():
    print("\n--- LIST (Ordered & Mutable) ---")

    subjects = ["Math", "Physics", "Chemistry"]
    print("Subjects:", subjects)

    subjects.append("Biology")
    subjects.remove("Physics")

    print("Updated Subjects:", subjects)


def tuple_example():
    print("\n--- TUPLE (Fixed Student Info) ---")

    student_info = (101, "Varshitha", "CSE")
    print("Student Info:", student_info)

    print("Student ID:", student_info[0])
    print("Department:", student_info[2])


def set_example():
    print("\n--- SET (Unique Course Enrollments) ---")

    enrollments = {"Python", "Java", "Python", "SQL"}
    print("Unique Enrollments:", enrollments)

    enrollments.add("AI")
    enrollments.discard("Java")

    print("Updated Enrollments:", enrollments)


def dict_example():
    print("\n--- DICTIONARY (Marks Record) ---")

    marks = {
        "Math": 85,
        "Physics": 90,
        "Chemistry": 88
    }

    marks["Math"] += 5
    marks["Biology"] = 92

    print("Final Marks:")
    for subject, score in marks.items():
        print(subject, ":", score)


if __name__ == "__main__":
    list_example()
    tuple_example()
    set_example()
    dict_example()
