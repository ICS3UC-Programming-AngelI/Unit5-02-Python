# !/u.sr/bin/env python3
# Created by: Angel
# Created on May 6,2025


def calculate_area(base, height):

    area = (base * height) / 2

    print("The area is {0} cm".format(area))


def main():
    user_base = 0
    user_height = 0
    try:
        user_base = float(input("enter the base of the triangle(cm): "))
        user_height = float(input("Enter the height of the triangle(cm): "))
        print("")

        if user_base <= 0:  # if the height from user is 0 or less,

            print("Please enter a bigger number!")
    except:
        print("This is invalid.")

        # call the function
    calculate_area(user_base, user_height)


if __name__ == "__main__":
    main()
