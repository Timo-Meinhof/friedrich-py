class User:
    def __init__(self, id: str, name: str, color: str, studon: str):
        self.id = id
        self.name = name
        self.color = color
        self.studon = studon

class Role:
    def __init__(self, id: str, name: str, color: str):
        self.id = id
        self.name = name
        self.color = color