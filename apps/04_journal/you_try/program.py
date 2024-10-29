import os

print("-----------------")
print("   Journal APP   ")
print("-----------------")


def open_journal(file_name):
    """
    This method load an existing journal or create a new one if name is not
     found

    :param file_name: name of the journal file to be loaded
    :return: returns loaded journal file
    """

    try:
        journal = open(file_name, "r+")

    except FileNotFoundError:
        print("File not found")
        new_file = input("Do you want to create new file with this name? y/n ")

        if new_file == "y":
            create_new_file(file_name)
            print("File created successfully")
            return open_journal(file_name)
        elif new_file == "n":
            exit()
        else:
            print("Command unrecognized")
            exit()

    else:
        return journal


def save_new_entry(journal, entry):
    journal.seek(0)
    if len(journal.readlines()) == 0:
        journal.write(entry)
    else:
        formatted_entry = f"\n{entry}"
        journal.write(formatted_entry)

    journal.flush()


def exit_journal(journal):
    path = os.path.join(os.getcwd(), journal.name)
    print(f"...Saving file to {path}...")
    journal.close()
    print(f"...Saved successfully...")


def print_entries(journal_content):
    if len(journal_content) > 0:
        for position, line in enumerate(journal_content, 1):
            print(f"{position}. {line.rstrip()}")
    else:
        print("Your Journal has o entries yet")


def create_new_file(name):
    journal = open(name, "x")
    journal.close()


def action_choice(journal):

    while True:
        journal.seek(0)
        journal_content = journal.readlines()
        user_choice = input("What do you want to do? l - list entries;"
                            " a - add entry; e - exit\n")
        if user_choice.lower() == "l":
            print_entries(journal_content)
        elif user_choice.lower() == "a":
            save_new_entry(journal, input("Enter your new entry: "))
            continue
        elif user_choice.lower() == "e":
            exit_journal(journal)
            break
        else:
            print("Command unrecognized")
            continue


def main():
    file_name = input("Enter the name of your Journal\n")
    path = os.path.join(os.getcwd(), file_name)
    print(f"...Loading file from {path}...")
    journal = open_journal(file_name)
    print(f"...{file_name} journal loaded successfully...")
    action_choice(journal)


if __name__ == "__main__":
    main()
