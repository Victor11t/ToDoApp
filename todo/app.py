class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = False
        self.tags = []

    def mark_completed(self) -> None:

        self.completed = True

    def add_tag(self, tag: str) -> None:

        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f'{self.code_id} - {self.title}'


class TodoBook:
    def __init__(self):
        self.todos = {}



    def add_todo(self, title, description):
        todo_id = len(self.todos) + 1
        new_todo = Todo(todo_id, title, description)
        self.todos[todo_id] = new_todo
        return todo_id

    def pending_todos(self):
        return [todo for todo_id, todo in self.todos.items() if not todo.completed]

    def completed_todos(self):
        return [todo for todo_id, todo in self.todos.items() if todo.completed]

    def tags_todo_count(self):
        tag_count = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag not in tag_count:
                    tag_count[tag] = 0
                tag_count[tag] += 1
        return tag_count