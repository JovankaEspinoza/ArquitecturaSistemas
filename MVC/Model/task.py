class Task:
    def __init__(self, description, date, done=False):
        self.description = description
        self.date = date
        self.done = done


    def __str__(self):
        status = "done" if self.done else "por hacer"
        return f"{status} {self.description} (creada el {self.date})"