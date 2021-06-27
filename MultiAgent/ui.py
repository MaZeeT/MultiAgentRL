

class UserInterface:
    def __init__(self):
        pass

    def render(self, state):
        pass

    def render_field(self, field):
        for row in field:
            print(row)

    def get_input(self):
        return input("Pick Direction, by wasd")

    def get_direction(self):
        d = {
            "w": "up",
            "a": "left",
            "s": "down",
            "d": "right",
        }
        return d[self.get_input()]
