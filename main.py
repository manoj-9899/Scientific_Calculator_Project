# main program: Scientific Calculator using database

import Scientific_Calculator as calc
import database as db

def display_menu():
    print("\n--- Scientific Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. View Calculation History")
    print("12. Clear Calculation History")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select operation (0 to exit): ")

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        elif choice in ['1', '2', '3', '4', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {calc.divide(num1, num2)}")
            elif choice == '6':
                print(f"Result: {calc.power(num1, num2)}")

        elif choice == '5':
            num = float(input("Enter a number: "))
            print(f"Result: {calc.square_root(num)}")

        elif choice in ['7', '8', '9']:
            angle = float(input("Enter angle in degrees: "))

            if choice == '7':
                print(f"Result: {calc.sine(angle)}")
            elif choice == '8':
                print(f"Result: {calc.cosine(angle)}")
            elif choice == '9':
                print(f"Result: {calc.tangent(angle)}")

        elif choice == '10':
            num = float(input("Enter a number: "))
            base = input("Enter base (default is 10): ")
            base = float(base) if base else 10
            print(f"Result: {calc.logarithm(num, base)}")

        elif choice == '11':
            history = db.get_calculation_history()
            if history:
                for record in history:
                    print(f"ID: {record[0]}, Operation: {record[1]}, Input1: {record[2]}, Input2: {record[3]}, Result: {record[4]}")
            else:
                print("No calculation history available.")

        elif choice == '12':
            db.clear_calculation_history()
            print("Calculation history cleared.")

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
