import os

def enter_expense():  # Функция для ввода информации о расходах
    expense_date = input("Введите дату расхода (например, 2023-10-21): ")
    expense_description = input("Введите описание расхода: ")
    expense_amount = float(input("Введите сумму расхода: "))
    return {
        "Дата": expense_date,
        "Описание": expense_description,
        "Сумма": expense_amount
    }
def save_expense(expense, filename):  # Функция для сохранения информации о расходах в файл
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{expense['Дата']} - {expense['Описание']} - {expense['Сумма']} руб.\n")
def display_expenses(filename): # Функция для вывода всех расходов из файла
    if not os.path.exists(filename):
        print("Файл с расходами пуст.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        expenses = file.readlines()
        if not expenses:
            print("Файл с расходами пуст.")
        else:
            print("Список расходов:")
            for expense in expenses:
                print(expense, end="")

if __name__ == "__main__":
    expense_file = "zadanie2.txt"  # Имя файла для хранения расходов

    while True:
        print("\nВыберите действие:")
        print("1. Ввести новый расход")
        print("2. Вывести список всех расходов")
        print("3. Выход")
        choice = input("Введите номер действия: ")
        if choice == "1":
            expense = enter_expense()
            save_expense(expense, expense_file)
            print("Расход успешно добавлен.")
        elif choice == "2":
            display_expenses(expense_file)
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
