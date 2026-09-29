from storage import load_data
from subjects import (
    add_subject,
    update_subject,
    show_all,
    delete_subject,
    pick_subject,
)
from calculator import percentage, need_to_attend
from menu import menu


def scenario(data):
    key = pick_subject(data)

    if key is None:
        return

    required = data["required"]
    s = data["subjects"][key]

    print(
        "Now:",
        str(s["attended"]) + "/" + str(s["total"]),
        "=",
        str(round(percentage(s["attended"], s["total"]), 2)) + "%"
    )

    future = get_number("How many classes are left / upcoming: ")
    will_attend = get_number("Out of those, how many will you attend: ")

    if will_attend > future:
        print("You cannot attend more classes than are left.")
        return

    new_attended = s["attended"] + will_attend
    new_total = s["total"] + future

    p = percentage(new_attended, new_total)

    print()
    print(
        "After those classes:",
        str(new_attended) + "/" + str(new_total),
        "=",
        str(round(p, 2)) + "%"
    )

    if p >= required:
        print("You will be above the limit of", str(required) + "%.")
    else:
        print("You will be below the limit of", str(required) + "%.")
        print(
            "You would need to attend",
            need_to_attend(new_attended, new_total, required),
            "more classes after that."
        )


def change_required(data):
    r = get_number("New required percentage (1 to 99): ")

    if r < 1 or r > 99:
        print("Please enter a value between 1 and 99.")
        return

    data["required"] = r

    from storage import save_data
    save_data(data)

    print("Required percentage changed to", str(r) + "%.")


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


def main():
    data = load_data()

    while True:
        menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_subject(data)

        elif choice == "2":
            update_subject(data)

        elif choice == "3":
            show_all(data)

        elif choice == "4":
            scenario(data)

        elif choice == "5":
            change_required(data)

        elif choice == "6":
            delete_subject(data)

        elif choice == "7":
            print("Bye!")
            break

        else:
            print("Wrong choice, please try again.")


if __name__ == "__main__":
    main()