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
