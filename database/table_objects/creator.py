from .ping_targets import User

class Creator:
    def __init__(self, id: int, login_name: str, password: str, discord_user: User):
        self.id = id
        self.login_name = login_name
        self.password = password
        self.discord_user = discord_user
