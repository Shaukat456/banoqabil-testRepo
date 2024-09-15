def get_user_input():
    try:
        name = input("Please enter your name: ")

        age = int(input("Please enter your age: "))
        return name, age
    except ValueError:
        print("Invalid input! Please enter a valid age as a number.")
        return None


def calculate_birth_year(age):
    current_year = (
        2023  # You can use datetime module to get the current year dynamically
    )
    return current_year - age


def main():
    print("Welcome to the Age Calculator!")

    name, age = get_user_input()

    if name and age is not None:
        birth_year = calculate_birth_year(age)
        print(f"{name}, you were born in the year {birth_year}.")
    else:
        print("Could not process your input. Please try again.")


hellowthere = "sdhsdhsd"
