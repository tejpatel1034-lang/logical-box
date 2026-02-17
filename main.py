
def generate_triangle():
    while True:
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Row count must be a positive number.")
            break
        else:
            print("\nPattern:\n")
            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end="")
                print()
            break


def analyze_numbers():
    while True:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if end < start:
            print("End number must be greater than or equal to start number.")
            continue

        total_sum = 0
        print()

        for num in range(start, end + 1):
            if num == 0:
                pass

            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")

            total_sum += num

        print(f"\nSum of all numbers from {start} to {end} is: {total_sum}")
        break


def main():
    print("\nWelcome to the Pattern Generator and Number Analyzer!")

    while True:
        print("\nSelect an option:")
        print("1. Generate a Pattern")
        print("2. Analyze a Range of Numbers")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_triangle()

        elif choice == "2":
            analyze_numbers()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
