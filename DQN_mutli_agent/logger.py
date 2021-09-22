
class LogToFile:
    def __init__(self, name):
        self.name = name
        file = open(f"{self.name}.txt", "w")
        file.write(f"Environment: {self.name}")
        file.write("\n")
        file.close()

    def add(self, text):
        file = open(f"{self.name}.txt", "a")
        file.write("\n")
        file.write(text)
        file.write("\n")
        file.close()
