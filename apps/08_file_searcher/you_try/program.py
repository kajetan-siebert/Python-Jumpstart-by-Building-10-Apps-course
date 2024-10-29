import os


def main():
    matches_count = 0
    directory = get_directory()
    search_text = get_search_text()

    print(f"Searching for {search_text} in {directory}")
    for file in search_for_files(directory):
        filename = os.path.basename(file)

        for match in search_in_file(search_text, file):
            line_no = match[0]
            line_text = match[1]

            print(f"{filename} file, line {line_no} >> {line_text}")
            matches_count += 1

    print()
    print(f"Total matches:{matches_count}")
    print("End of search")


def get_directory():
    abs_path = input("Enter absolute path to the folder with the files you "
                     "want to search through. Leave empty for getting current "
                     "working directory\n")
    if abs_path == "":
        abs_path = os.getcwd()
        return abs_path

    elif os.path.exists(abs_path) is False:
        print("Directory does not exist. Please try again.")
        return get_directory()
    else:
        return abs_path


def get_search_text():
    search_text = input("Enter the text you want to search for:\n")
    return search_text


def search_for_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path


def search_in_file(search_text, file_path):

    with open(file_path, 'r') as f:
        for line_number, line in enumerate(f, start=1):

            if line.find(search_text) != -1:
                yield line_number, line


if __name__ == '__main__':
    main()
