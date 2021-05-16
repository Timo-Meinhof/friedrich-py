from .repeat import Repeat
from .ping_targets import User, Role
from .creator import Creator
from .subject import Subject

class Date:
    def __init__(self, id: int, gid: str, title: str, subtitle: str, subject: Subject, description: str, due_date: str, due_time: str, repeat: Repeat, create_date: str, create_time: str, creator: Creator, expired: bool, ping_roles: [Role], ping_users: [User]):
        self.id = id
        self.gid = gid
        self.title = title
        self.subtitle = subtitle
        self.subject = subject
        self.description = description
        self.due_date = due_date
        self.due_time = due_time
        self.repeat = repeat
        self.create_date = create_date
        self.create_time = create_time
        self.creator = creator
        self.expired = expired
        self.ping_roles = ping_roles
        self.ping_users = ping_users