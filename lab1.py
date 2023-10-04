import math

while True:
        try:
            num1 = float(input("Enter num1: "))
            operator = input("Choose operation (+, -, *, /, ^, sqrt, %): ")
            if operator not in ('+', '-', '*', '/', '^', 'sqrt', '%'):
                print("Bad request")
                continue
            num2 = float(input("Enter num2: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            elif operator == '^':
                result = num1 ** num2
            elif operator == 'sqrt':
                result = math.sqrt(num1)
            elif operator == '%':
                result = num1 % num2

            print("Result:", result)

            if input("Contue? (Y/N)? ").lower() != 'y':
                break
        except ValueError:
            print("Enter float")
        except ZeroDivisionError:
            print("Zer oDivision")
        except Exception as e:
            print("Error:", e)