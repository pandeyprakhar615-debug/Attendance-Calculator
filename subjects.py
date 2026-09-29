from storage import save_data
from calculator import percentage, can_skip, need_to_attend


def find_subject(data, name):
    for key in data["subjects"]:
        if key.lower() == name.strip().lower():
            return key
    return None


def pick_subject(data):
    if not data["subjects"]:
        print("No subjects added yet.")
        return None

    print("Subjects:", ", ".join(data["subjects"].keys()))
    name = input("Enter subject name: ")

    key = find_subject(data, name)

    if key is None:
        print("Subject not found.")

    return key


def add_subject(data):
    name = input("Subject name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if find_subject(data, name) is not None:
        print("This subject is already added.")
        return

    total = get_number("Total classes held so far: ")
    attended = get_number("Classes you attended: ")

    if attended > total:
        print("Attended classes cannot be more than total classes.")
        return

    data["subjects"][name] = {
        "attended": attended,
        "total": total
    }

    save_data(data)
    print("Subject added.")


def update_subject(data):
    key = pick_subject(data)

    if key is None:
        return

    present = get_number("New classes you attended: ")
    absent = get_number("New classes you missed: ")

    data["subjects"][key]["attended"] += present
    data["subjects"][key]["total"] += present + absent

    save_data(data)
    print("Attendance updated.")


def show_all(data):
    if not data["subjects"]:
        print("No subjects added yet.")
        return

    required = data["required"]

    print()
    print("Required attendance:", str(required) + "%")
    print("-" * 50)

    for name, s in data["subjects"].items():
        p = percentage(s["attended"], s["total"])

        print(
            name,
            "-",
            str(s["attended"]) + "/" + str(s["total"]),
            "-",
            str(round(p, 2)) + "%"
        )

        if p >= required:
            print(
                "  Safe. You can skip",
                can_skip(s["attended"], s["total"], required),
                "more classes."
            )
        else:
            print(
                "  Low! Attend",
                need_to_attend(s["attended"], s["total"], required),
                "classes in a row to reach",
                str(required) + "%."
            )

    print("-" * 50)


def delete_subject(data):
    key = pick_subject(data)

    if key is None:
        return

    del data["subjects"][key]
    save_data(data)

    print("Subject deleted.")


def get_number(msg):
    while True:
        try:
            n = int(input(msg))

            if n < 0:
                print("Please enter a number that is 0 or more.")
                continue

            return n

        except ValueError:
            print("That is not a valid number, try again.")