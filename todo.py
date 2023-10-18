import flet as ft
from PIL import Image

def main(page):

    # Load the anime wallpaper image
    image = Image.open("de.jpg")

    # Create a new wallpaper control
    wallpaper = ft.Wallpaper(image)

    # Create a new page for the tasks
    tasks_page = ft.Page(title="Tasks")

    # Create a list of tasks
    tasks = []

    def btn_click(e):
        task = new_task.value
        tasks.append(task)
        new_task.value = ""
        page.update()
        new_task.focus()

    btn = ft.ElevatedButton("Add task", on_click=btn_click)

    # Add the new task text field and button to the tasks page
    tasks_page.add(wallpaper,
        new_task,
        btn,
    )

    # Create a new page for the completed tasks
    completed_tasks_page = ft.Page(title="Completed tasks")

    # Create a list of completed tasks
    completed_tasks = []

    def btn_complete(e):
        task_index = tasks.index(task)
        completed_tasks.append(tasks.pop(task_index))
        page.update()

    # Add a checkbox to each task on the tasks page
    for task in tasks:
        task_checkbox = ft.Checkbox(value=False, on_click=lambda e: btn_complete(e))
        tasks_page.add(task_checkbox)

    # Add the completed tasks to the completed tasks page
    for task in completed_tasks:
        completed_tasks_page.add(ft.Text(task))

    # Add the tasks page and completed tasks page to the main page
    page.add(tasks_page, completed_tasks_page)

ft.app(target=main)
