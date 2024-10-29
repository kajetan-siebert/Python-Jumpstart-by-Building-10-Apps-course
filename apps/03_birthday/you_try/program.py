import datetime

print('------------------------')
print('      BIRTHDAY APP      ')
print('------------------------')


def get_birth_date():
    print("When were you born?")
    birth_year = int(input("Year [YYYY]: "))
    birth_month = int(input("Month [MM]: "))
    birth_day = int(input("Day [DD]: "))

    birth_date = datetime.date(birth_year, birth_month, birth_day)

    return birth_date


def calculate_days_before_after(birth_date):
    current_date = datetime.date.today()
    birthday_date = datetime.date(current_date.year, birth_date.month,
                                  birth_date.day)

    days_difference = (current_date - birthday_date).days

    return days_difference


def main():
    birth_date = get_birth_date()
    days_before_after=calculate_days_before_after(birth_date)

    print(f"It looks like you were born on {birth_date}")

    if days_before_after<0:
        print(f"There are {abs(days_before_after)} days left until your"
              f"birthday")
    elif days_before_after>0:
        print(f"It's {days_before_after} days after your birthday")
    else:
        print("Happy birthday, it's today!")


if __name__ == '__main__':
    main()

