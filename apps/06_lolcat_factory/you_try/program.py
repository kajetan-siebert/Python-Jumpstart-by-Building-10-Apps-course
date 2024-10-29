import requests
import shutil
import subprocess
import os
import platform


def main():

    print_header()

    abs_path = get_path()

    no_of_cats = 8
    for i in range(no_of_cats):
        print(f"Downloading cat no 1...", end=" ")
        res = get_image()
        with open(fr"{abs_path}\cat{i}.jpg", 'wb') as fout:
            shutil.copyfileobj(res, fout)
        print("Done")

    open_folder(abs_path)


def print_header():
    print("----------------------")
    print("   Cat Factory App    ")
    print("----------------------")


def get_image():
    url = r"http://consuming-python-services-api.azurewebsites.net/cats/random"
    response = requests.get(url, stream=True)
    return response.raw


def get_path():
    abs_path = input("Enter absolute path to the folder you want to save"
                     " images to, press enter to save it in a cats images"
                     " folder in your current working directory\n")
    if abs_path == "":
        # abs_path = (r"C:\Users\kajetan.siebert"
        #             r"\PycharmProjects\python-jumpstart-course-demos"
        #             r"\apps\06_lolcat_factory\you_try\cats")
        abs_path = os.path.join(os.getcwd(), "cats images")
        os.mkdir(abs_path)
    return abs_path


def open_folder(path):
    """
    This function opens a folder with path specified in the argument

    :param path: Path to folder with cats images
    :return: Doesn't return anything, just opens folder
    """
    print("Opening folder: ", os.path.basename(path))
    if platform.system().lower() == "windows":
        subprocess.call(['explorer', path])
    elif platform.system().lower() == "linux":
        subprocess.call(['xdg-open', path])
    elif platform.system().lower() == "darwin":
        subprocess.call(['open', path])
    else:
        print("Sorry, I don't know how to open the folder for this OS")


if __name__ == '__main__':
    main()
