class User:
    def __init__(self, name):
        self.name = name

    def role(self):
        return "Default User"

class Admin(User):
    def role(self):
        return "Admin"

class Editor(User):
    def role(self):
        return "Editor"

class Viewer(User):
    def role(self):
        return "Viewer"

def create_user(user_type, name):
    user_type = user_type.lower()

    match user_type:
        case "admin":
            return Admin(name)
        case "editor":
            return Editor(name)
        case "viewer":
            return Viewer(name)
        case _:
            return Viewer(name)


if __name__ == "__main__":
    users = [
        create_user("admin", "Ben"),
        create_user("editor", "John"),
        create_user("viewer", "Steve"),
        create_user('admin', 'John 2'),
        create_user('editor', 'Ben 2'),
        create_user('viewer', 'Zac'),
        create_user('admin', 'Dylan'),
    ]

    for user in users:
        print(user.name)
        print(user.role)