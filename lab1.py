import math

# def calculator():
#     while True:
#         try:
#             num1 = float(input("Введіть перше число: "))
#             operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
#             if operator not in ('+', '-', '*', '/', '^', '√', '%'):
#                 print("Недопустимий оператор. Спробуйте ще раз.")
#                 continue
#             if operator == '^':
#                 num2 = float(input("Введіть ступінь: "))
#             elif operator == '√':
#                 num2 = None
#             else:
#                 num2 = float(input("Введіть друге число: "))

#             if operator == '+':
#                 result = num1 + num2
#             elif operator == '-':
#                 result = num1 - num2
#             elif operator == '*':
#                 result = num1 * num2
#             elif operator == '/':
#                 result = num1 / num2
#             elif operator == '^':
#                 result = num1 ** num2
#             elif operator == '√':
#                 result = math.sqrt(num1)
#             elif operator == '%':
#                 result = num1 % num2

#             print("Результат:", result)

#             if input("Бажаєте продовжити (Так/Ні)? ").lower() != 'так':
#                 break
#         except ValueError:
#             print("Будь ласка, введіть дійсне число.")
#         except ZeroDivisionError:
#             print("Ділення на нуль неможливе.")
#         except Exception as e:
#             print("Сталася помилка:", e)

# if __name__ == "__main__":
#     calculator()


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