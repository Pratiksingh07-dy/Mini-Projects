import json
import argparse
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()

    tasks.append({
        "id": len(tasks) + 1,
        "task": task
    })

    save_tasks(tasks)
    print("✅ Task added successfully.")


def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("📭 No tasks found.")
        return

    print("\n📋 To-Do List:\n")

    for task in tasks:
        print(f"{task['id']}. {task['task']}")


def update_task(task_id, new_task):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["task"] = new_task
            save_tasks(tasks)
            print("✏️ Task updated successfully.")
            return

    print("❌ Task ID not found.")


def delete_task(task_id):
    tasks = load_tasks()

    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        print("❌ Task ID not found.")
        return

    for index, task in enumerate(updated_tasks, start=1):
        task["id"] = index

    save_tasks(updated_tasks)
    print("🗑️ Task deleted successfully.")


parser = argparse.ArgumentParser(description="CLI To-Do List Manager")

subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("task")

list_parser = subparsers.add_parser("list")

update_parser = subparsers.add_parser("update")
update_parser.add_argument("id", type=int)
update_parser.add_argument("task")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)

args = parser.parse_args()

if args.command == "add":
    add_task(args.task)

elif args.command == "list":
    list_tasks()

elif args.command == "update":
    update_task(args.id, args.task)

elif args.command == "delete":
    delete_task(args.id)

else:
    parser.print_help()