from project.task import Task


class Section:
    def __init__(self, name : str):
        self.name = name
        self.tasks:list[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name : str):
        t = next((t for t in self.tasks if t.name == task_name), None)
        if t:
            t.completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        current_tasks_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.completed == False]
        return f"Cleared {current_tasks_len - len(self.tasks)} tasks."

    def view_section(self):
        tasks_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{tasks_details}"
