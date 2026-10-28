import json
import shutil
import os

def show_menu():
    print("\n===TASK MANAGER===")
    print("1) Добавление задачи\n2) Список задач\n3) Завершение задачи\n4) Удаление задачи\n5) Выход\n")

def add_task(tasks):
    task = input("Введите название задачи, которую необходимо добавить: ")
    if task.strip() == "":
        print("Такое название дать задаче нельзя")
        return
    res = {"title": task, "completed": False}
    tasks.append(res)

    save_tasks(tasks)

def show_tasks(tasks):
    if len(tasks) == 0:
        print("Список задач пуст")
        return
    for ind, task in enumerate(tasks):
        if task["completed"]:
            print(f"{ind + 1}. {task['title']}: [✓]")
        else:
            print(f"{ind + 1}. {task['title']}: [ ]")

def get_task_index(tasks):
    number = input("Введите номер задачи: ")

    if not number.isdigit():
        print("Вы ввели некорректное число")
        return None

    number = int(number)

    if (number > len(tasks) or number < 1):
        print("Задачи с таким номером не существует")
        return None

    return number - 1

def complete_task(tasks):
    if len(tasks) == 0:
        print("Список пуст!")
        return

    show_tasks(tasks)

    index = get_task_index(tasks)

    if index is None:
        return

    if tasks[index]["completed"]:
        print("Данная задача уже выполнена")
        return

    tasks[index]["completed"] = True

    print("Статус успешно изменен!")

    save_tasks(tasks)

def delete_task(tasks):
    if len(tasks) == 0:
        print("Список пуст!")
        return

    show_tasks(tasks)

    index = get_task_index(tasks)

    if index is None:
        return

    tasks.pop(index)

    print("Задача успешно удалена!")

    save_tasks(tasks)

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    except json.decoder.JSONDecodeError:
        print("json файл поврежден")
        if not os.path.exists("tasks_backup.json"):
            shutil.copy2("tasks.json", "tasks_backup.json")
        tasks = []

    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        command = input("Введите команду: ")
        if command == "1":
            print("Добавление задачи")
            add_task(tasks)
        elif command == "2":
            print("Список задач")
            show_tasks(tasks)
        elif command == "3":
            print("Завершение задачи")
            complete_task(tasks)
        elif command == "4":
            print("Удаление задачи")
            delete_task(tasks)
        elif command == "5":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда")

if __name__ == '__main__':
    main()