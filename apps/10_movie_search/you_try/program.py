import movie_service
import exceptions
import requests


def main():

    print_header()

    search_text = get_search_text()
    try:
        for result in movie_service.search_movie(search_text):
            print(f"{result.title} - {result.year}")
    except requests.exceptions.ConnectionError as e:
        print(f"We encountered a connection error. Error details below: \n{e}")
    except ValueError as e:
        print(f"Error occurred: {e}")


def print_header():
    print("----------------------")
    print("-----Movie search-----")
    print("----------------------")


def get_search_text():
    try:
        search_text = input("Enter movie title/keyword: ").strip()
        if not search_text:
            raise exceptions.EmptyTextError
    except exceptions.EmptyTextError as e:
        print(f"Something went wrong: {e}")
        exit()
    else:
        return search_text


if __name__ == '__main__':
    main()



