def main():
    n = int(input("enter the total number of students: ").strip())
    1<= n <= 60

    for i in range (n):
        individual_grad = int(input("enter the grade of each student").strip())
        # if the grade is less than 38 it is a fail so it will return it
        if individual_grad < 38:
            print("the final grade is: ", individual_grad)
        # else if it is greater than 38 and the difference between the grades is less than 3 return the grade without
        # rounding it up
        elif individual_grad % 5 < 3:
            print("the final grade is: ", individual_grad)
        else:
            print("the final grade is", (individual_grad + 5-(individual_grad % 5)))


if __name__ == '__main__':
    main()

