import requests

def main():
    print_header()
    data = get_location_details()
    print(data)

    weather_details = get_weather_details(data)

    if "cod" in weather_details:
        print("Something went wrong")
        print(f"Code: {weather_details['cod']}, messsage: {weather_details['message']}")
    else:
        print(weather_details)
        print(type(weather_details))
        print_weather(weather_details)




def print_header():
    print("--------------------------------------")
    print("----------WEATHER CLIENT APP----------")
    print("--------------------------------------")


def process_input(input_required=False):
    """
    Function validates if entered input is valid.
    :param input_required: Specifies if input is required or not.
    :return: Return validated String input
    """

    input_string = input().strip()

    if not input_required:

        if input_string == "":
            return None
        elif len(input_string) != 2:
            print("Code needs to be 2 letters, try again")
            return process_input()
        else:
            return input_string

    else:
        if input_string == "":
            print("This field must be filled")
            return process_input(input_required)
        else:
            return input_string


def get_location_details():
    """
    Function takes user input location details
    :return: tuple of values for city, country, state and units in a correct
    form
    """

    print("[required] Enter city name: ")
    city = process_input(True)

    print(("[optional - leave empty and press enter to skip] Enter countrycode"
           " (e.g. PL for Poland): "))
    country = process_input()

    print("[optional - leave empty and press enter to skip] Enter state code"
          " (only for US): ")
    state = process_input()

    units = "metric"
    unit_selection = input("[optional - leave empty and press enter to skip]"
                           " Choose metric: m - metric, i -imperial").strip()

    while (unit_selection != "m" and unit_selection != "i"
           and unit_selection != ""):
        unit_selection = input("Please enter 'm' for metric "
                               "or 'i' for imperial")

    if unit_selection == "m":
        units = "metric"
    elif unit_selection == "i":
        units = "imperial"

    return city, country, state, units


def get_weather_details(location_data):
    city = location_data[0]
    print(city)
    country = location_data[1]
    state = location_data[2]
    units = location_data[3]

    url = r"https://weather.talkpython.fm/api/weather/"
    request = requests.get(url, params={"city": city, "country": country,
                                        "state": state, "units": units})
    response = request.json()
    return response



def print_weather(weather_details):
    weather = weather_details["weather"]["description"]
    wind_speed = weather_details["wind"]["speed"]
    temperature = weather_details["forecast"]["temp"]
    humidity = weather_details["forecast"]["humidity"]
    pressure = weather_details["forecast"]["pressure"]
    city = weather_details["location"]["city"]
    country = weather_details["location"]["country"]
    state = weather_details["location"]["state"]

    print(f"Weather in {city}, {state}, {country} : {weather}. Temperature: {temperature}, humidity: {humidity}, pressure: {pressure}, wind speed: {wind_speed}")


if __name__ == '__main__':
    main()
