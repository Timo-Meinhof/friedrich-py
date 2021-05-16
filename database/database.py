import sqlite3
from threading import Lock

from table_objects.date import Date
from table_objects.ping_targets import User, Role
from table_objects.creator import Creator
from table_objects.repeat import Repeat
from table_objects.subject import Subject

from db_utils import init_db

lock = Lock()

conn = sqlite3.connect(':memory:', check_same_thread = False)

c = conn.cursor()

init_db(conn)

# -------------------------------------------------
#
#   UPDATED
#
# -------------------------------------------------

# dates()
def dates(body) -> [Date]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates
                    """)
        result = c.fetchall()
        lock.release()
        if result:
            dates = []
            for res in result:
                dates.append(Date(res[0], res[1], res[2], res[3], subject_by_name({"name": res[4]}), res[5], res[6], res[7], repeat_by_id({"id": res[8]}), res[9], res[10], creator_by_id({"id": res[11]}), res[12], pinged_roles({"id": res[0]}), pinged_users({"id": res[0]})))
            return dates

# dates_not_expired()
def dates_not_expired(body) -> [Date]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates
                        WHERE expired = 0
                    """)
        result = c.fetchall()
        lock.release()
        if result:
            dates = []
            for res in result:
                dates.append(Date(res[0], res[1], res[2], res[3], subject_by_name({"name": res[4]}), res[5], res[6], res[7], repeat_by_id({"id": res[8]}), res[9], res[10], creator_by_id({"id": res[11]}), res[12], pinged_roles({"id": res[0]}), pinged_users({"id": res[0]})))
            return dates

# dates_expired()
def dates_expired(body) -> [Date]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates
                        WHERE expired = 1
                    """)
        result = c.fetchall()
        lock.release()
        if result:
            dates = []
            for res in result:
                dates.append(Date(res[0], res[1], res[2], res[3], subject_by_name({"name": res[4]}), res[5], res[6], res[7], repeat_by_id({"id": res[8]}), res[9], res[10], creator_by_id({"id": res[11]}), res[12], pinged_roles({"id": res[0]}), pinged_users({"id": res[0]})))
            return dates

# users()
def users(body) -> [User]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM users
                    """)
        result = c.fetchall()
        lock.release()
        if result:
            users = []
            for res in result:
                users.append(User(*res))
            return users

# roles()
def roles(body) -> [Role]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM roles
                    """)
        result = c.fetchall()
        lock.release()
        if result:
            roles = []
            for res in result:
                roles.append(Role(*res))
            return roles

# subjects()
def subjects(body) -> [Subject]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM subjects
                    """)
        result = c.fetchall()
        lock.release()
        if result:
            subjects = []
            for res in result:
                subjects.append(Subject(*res))
            return subjects

# repeats()
def repeats(body) -> [Repeat]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM repeat
                    """)
        result = c.fetchall()
        lock.release()
        if result:
            repeats = []
            for res in result:
                repeats.append(Repeat(*res))
            return repeats

# creators()
def creators(body) -> [Creator]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM creators
                    """)
        result = c.fetchall()
        lock.release()
        if result:
            creators = []
            for res in result:
                creators.append(Creator(res[0], res[1], res[2], user_by_id({"id": res[3]})))
            return creators

# date_by_id(id: int)
def date_by_id(body) -> Date:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates
                        WHERE id=?
                    """, (int(body['id']), ))
        res = c.fetchone()
        lock.release()
        if res:
            return Date(res[0], res[1], res[2], res[3], subject_by_name({"name": res[4]}), res[5], res[6], res[7], repeat_by_id({"id": res[8]}), res[9], res[10], creator_by_id({"id": res[11]}), res[12], pinged_roles({"id": res[0]}), pinged_users({"id": res[0]}))

# user_by_id(id: str)
def user_by_id(body) -> User:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM users
                        WHERE id=?
                    """, (body['id'], ))
        result = c.fetchone()
        lock.release()
        if result:
            return User(*result)

# role_by_id(id: str)
def role_by_id(body) -> Role:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM roles
                        WHERE id=?
                    """, (body['id'], ))
        result = c.fetchone()
        lock.release()
        if result:
            return Role(*result)

# subject_by_name(name: str)
def subject_by_name(body) -> Subject:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM subjects
                        WHERE name=?
                    """, (body['name'],))
        result = c.fetchone()
        lock.release()
        if result:
            return Subject(*result)

# repeat_by_id(id: int)
def repeat_by_id(body) -> Repeat:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM repeat
                        WHERE id=?
                    """, (int(body['id']),))
        result = c.fetchone()
        lock.release()
        if result:
            return Repeat(*result)

# creator_by_id(id: int)
def creator_by_id(body) -> Creator:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM creators
                        WHERE id=?
                    """, (int(body['id']),))
        result = c.fetchone()
        lock.release()
        if result:
            return Creator(result[0], result[1], result[2], user_by_id({"id": result[3]}))

# pinged_users(id: int)
def pinged_users(body) -> [User]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates_ping_users
                        WHERE date_id=? 
                    """, (int(body['id']),))
        result = c.fetchall()
        lock.release()
        if result:
            users = []
            for res in result:
                users.append(user_by_id({"id": res[1]}))
            return users

# pinged_roles(id: int)
def pinged_roles(body) -> [Role]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates_ping_roles
                        WHERE date_id=? 
                    """, (int(body['id']),))
        result = c.fetchall()
        lock.release()
        if result:
            roles = []
            for res in result:
                roles.append(role_by_id({"id": res[1]}))
            return roles

# dates_by_subject(name: str)
def dates_by_subject(body) -> [Date]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates
                        WHERE subject=?
                    """, (body['name'], ))
        result = c.fetchall()
        lock.release()
        if result:
            dates = []
            for res in result:
                dates.append(Date(res[0], res[1], res[2], res[3], subject_by_name({"name": res[4]}), res[5], res[6], res[7], repeat_by_id({"id": res[8]}), res[9], res[10], creator_by_id({"id": res[11]}), res[12], pinged_roles({"id": res[0]}), pinged_users({"id": res[0]})))
            return dates

# dates_by_user(id: str)
def dates_by_user(body) -> [Date]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates_ping_users
                        WHERE user_id=? 
                    """, (body['id'],))
        result = c.fetchall()
        lock.release()
        if result:
            dates = []
            for res in result:
                dates.append(date_by_id({"id": res[0]}))
            return dates

# dates_by_role(id: str)
def dates_by_role(body) -> [Date]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates_ping_users
                        WHERE role_id=? 
                    """, (body['id'],))
        result = c.fetchall()
        lock.release()
        if result:
            dates = []
            for res in result:
                dates.append(date_by_id({"id": res[0]}))
            return dates

# dates_by_gid(gid: str)
def dates_by_id(body) -> [Date]:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM dates
                        WHERE gid=?
                    """, (body['gid'], ))
        result = c.fetchall()
        lock.release()
        if result:
            dates = []
            for res in result:
                dates.append(Date(res[0], res[1], res[2], res[3], subject_by_name({"name": res[4]}), res[5], res[6], res[7], repeat_by_id({"id": res[8]}), res[9], res[10], creator_by_id({"id": res[11]}), res[12], pinged_roles({"id": res[0]}), pinged_users({"id": res[0]})))
            return dates

# user_by_name(name: str)
def user_by_name(body) -> User:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM users
                        WHERE name=?
                    """, (body['name'], ))
        result = c.fetchone()
        lock.release()
        if result:
            return User(*result)

# role_by_name(name: str)
def role_by_name(body) -> Role:
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM roles
                        WHERE name=?
                    """, (body['name'], ))
        result = c.fetchone()
        lock.release()
        if result:
            return Role(*result)

# creator_by_login_name(login_name: str)
def creator_by_login_name(body: str):
    with conn:
        lock.acquire(True)
        c.execute(  """ SELECT *
                        FROM creators
                        WHERE login_name=?
                    """, (body['login_name'], ))
        result = c.fetchone()
        lock.release()
        if result:
            return Creator(result[0], result[1], result[2], user_by_id({"id": result[3]}))

# get_dates_by_time(start_date: str, start_time: str, end_date: str, end_time: str)

# insert_date(date: Date)
def insert_date(date: Date) -> Date:
    date_id = 0
    print(date.gid)
    if subject_by_name({"name": date.subject.name}) and repeat_by_id({"id": date.repeat.id}) and creator_by_id({"id": date.creator.id}):
        with conn:
            lock.acquire(True)
            c.execute("INSERT INTO dates VALUES (:id, :gid, :title, :subtitle, :subject, :description, :due_date, :due_time, :repeat, :create_date, :create_time, :creator, :expired);", {'id': None, 'gid': date.gid, 'title': date.title, 'subtitle': date.subtitle, 'subject': date.subject.name, 'description': date.description, 'due_date': date.due_date, 'due_time': date.due_time, 'repeat': date.repeat.id, 'create_date': date.create_date, 'create_time': date.create_time, 'creator': date.creator.id, 'expired': 0})
            date_id = c.lastrowid
            lock.release()
    else:
        print("Failed to insert Date. (foreign key requirement)")
        return None

    for user in date.ping_users:
        if user_by_id({"id": user.id}):
            with conn:
                lock.acquire(True)
                c.execute("INSERT INTO dates_ping_users VALUES (:date_id, :user_id);", {'date_id': date_id, 'user_id': user.id})
                lock.release()
        else:
            print("Failed to insert user ping, because it did not fulfill the foreign key requirement " + user.id)
    
    for role in date.ping_roles:
        if role_by_id({"id": role.id}):
            with conn:
                lock.acquire(True)
                c.execute("INSERT INTO dates_ping_roles VALUES (:date_id, :role_id);", {'date_id': date_id, 'role_id': role.id})
                lock.release()
        else:
            print("Failed to insert role ping, because it did not fulfill the foreign key requirement")
    date.id = date_id
    print(json.dumps(date, default=lambda o: o.__dict__, sort_keys=False, indent=4))
    return date

# insert_user(user: User)
def insert_user(user: User) -> User:
    with conn:
        lock.acquire(True)
        c.execute("INSERT INTO users VALUES (:id, :name, :color, :studon);", {'id': user.id, 'name': user.name, 'color': user.color, 'studon': user.studon})
        lock.release()
    return user

# insert_role(role: Role)
def insert_role(role: Role) -> Role:
    with conn:
        lock.acquire(True)
        c.execute("INSERT INTO roles VALUES (:id, :name, :color);", {'id': role.id, 'name': role.name, 'color': role.color})
        lock.release()
    return role

# insert_subject(subject: Subject)
def insert_subject(subject: Subject) -> Subject:
    with conn:
        lock.acquire(True)
        c.execute("INSERT INTO subjects VALUES (:name, :exam_ects, :prac_ects, :exam_description, :prac_description, :studon_url, :zoom_url, :contact, :further_information, :ping_tag, :color);", {'name': subject.name, 'exam_ects': subject.exam_ects, 'prac_ects': subject.prac_ects, 'exam_description': subject.exam_description, 'prac_description': subject.prac_description, 'studon_url': subject.studon_url, 'zoom_url': subject.zoom_url, 'contact': subject.contact, 'further_information': subject.further_info, 'ping_tag': subject.ping_tag, 'color': subject.color})
        lock.release()
    return subject

# insert_creator(creator: Creator)
def insert_creator(creator: Creator) -> Creator:
    if user_by_id({"id": creator.discord_user.id}):
        creator_id = 0
        with conn:
            lock.acquire(True)
            c.execute("INSERT INTO creators VALUES (:id, :login_name, :password, :discord_user);", {'id': None, 'login_name': creator.login_name, 'password': creator.password, 'discord_user': creator.discord_user.id})
            creator_id = c.lastrowid
            lock.release()
            creator.id = creator_id
    else:
        print("Failed to insert creator, because discord_user does not exist.")
    return creator

# insert_repeat(repeat: Repeat)
def insert_repeat(repeat: Repeat) -> Repeat:
    with conn:
        lock.acquire(True)
        c.execute("INSERT INTO repeat VALUES (:id, :display_name);", {'id': repeat.id, 'display_name': repeat.display_name})
        lock.release()
    return repeat

# modify_date(id: int, date: Date)
# modify_dates(id: str, date: Date)
# modify_user(id: str, user: User)
# modify_role(id: str, role: Role)
# modify_subject(name: str, subject: Subject)
# modify_creator(id: int, creator: Creator)

import json
def obj_dict(obj):
    return obj.__dict__

# Will not be changed later
rNone = insert_repeat(Repeat(0, "None"))
rDaily = insert_repeat(Repeat(1, "Daily"))
rWeekly = insert_repeat(Repeat(2, "Weekly"))
r2Weekly = insert_repeat(Repeat(3, "Every 2 Weeks"))
rMonthly = insert_repeat(Repeat(4, "Monthly"))

# Temp testinng
math = insert_subject(Subject("Mathe C4", 7.5, 0, "Keine Taschenrechner, aber doppelseitiges handbeschriebenes Blatt", "Keine Bonusbunkte, min. 50% zum bestehen des Scheins", "someStudonURL.com", "someZoomURL.com", "Prof. Dr. Merz contact here", "Space for some further information about math in general, such as requirements idk ...", "@bcibu1391enbc890123ee99a", "#ffffff"))
thprog = insert_subject(Subject("ThProg", 7.5, 0, "Noch keinen Plan", "Bonuspunkte", "someStudonURL.com", "someZoomURL.com", "Prof. Dr. Merz contact here", "Space for some further information about math in general, such as requirements idk ...", "@bcibu1391enbc890123ee99a", "#ffffff"))
rk = insert_subject(Subject("RK", 5, 0, "Keine Taschenrechner, aber doppelseitiges handbeschriebenes Blatt", "Keine Bonusbunkte, min. 50% zum bestehen des Scheins", "someStudonURL.com", "someZoomURL.com", "Prof. Dr. Merz contact here", "Space for some further information about math in general, such as requirements idk ...", "@bcibu1391enbc890123ee99a", "#ffffff"))
algoks = insert_subject(Subject("AlgoKS", 7.5, 0, "Keine Taschenrechner, aber doppelseitiges handbeschriebenes Blatt", "Keine Bonusbunkte, min. 50% zum bestehen des Scheins", "someStudonURL.com", "someZoomURL.com", "Prof. Dr. Merz contact here", "Space for some further information about math in general, such as requirements idk ...", "@bcibu1391enbc890123ee99a", "#ffffff"))

user1 = insert_user(User("@bsca21398c1123", "Timo", "#ff0000", "zi04roby"))
user2 = insert_user(User("@nkjacsxv980zu2", "Kathrin", "#00ff00", "bf25fasa"))
user3 = insert_user(User("@vdscbjdsviu123", "Aurelius", "#0000ff", "keinPlan"))

role1 = insert_role(Role("@scad123hjdj1", "WS20", "#ffffff"))
role2 = insert_role(Role("@asd1231d1123", "SS20", "#ffffff"))
role3 = insert_role(Role("@mnvjkfvu1212", "SS21", "#ffffff"))

creator1 = insert_creator(Creator(0, "DadoSpeedy", "123456", user1))
creator2 = insert_creator(Creator(0, "KathiM", "asdfjkl", user2))

insert_date(Date(0, "mathehomework", "Hausaufgabe", "Blatt 01", math, "Jede Woche abzugeben 30/40 Punkte", "01/01/21", "13:00", rWeekly, "01/01/21", "13:00", creator1, 0, [role1], [user1, user2]))
insert_date(Date(0, "mathehomework", "Hausaufgabe", "Blatt 01", math, "Jede Woche abzugeben 30/40 Punkte", "08/01/21", "13:00", rWeekly, "01/01/21", "13:00", creator1, 0, [role1], [user1, user2]))
insert_date(Date(0, "mathehomework", "Hausaufgabe", "Blatt 01", math, "Jede Woche abzugeben 30/40 Punkte", "15/01/21", "13:00", rWeekly, "01/01/21", "13:00", creator1, 0, [role1], [user1, user2]))
insert_date(Date(0, "mathehomework", "Hausaufgabe", "Blatt 01", math, "Jede Woche abzugeben 30/40 Punkte", "22/01/21", "13:00", rWeekly, "01/01/21", "13:00", creator1, 0, [role1], [user1, user2]))

insert_date(Date(0, "thproghomework", "Hausaufgabe", "Blatt 01", thprog, "Insert your ad here", "13/12/21", "08:00", rWeekly, "01/01/21", "13:00", creator2, 0, [role1, role2], [user2, user3]))
insert_date(Date(0, "thproghomework", "Hausaufgabe", "Blatt 01", thprog, "Insert your ad here", "20/12/21", "08:00", rWeekly, "01/01/21", "13:00", creator2, 0, [role1, role2], [user2, user3]))
insert_date(Date(0, "thproghomework", "Hausaufgabe", "Blatt 01", thprog, "Insert your ad here", "27/12/21", "08:00", rWeekly, "01/01/21", "13:00", creator2, 0, [role1, role2], [user2, user3]))

insert_date(Date(0, "rkexam", "Klausur", "", rk, "Important", "31/04/21", "11:30", rNone, "02/02/21", "13:00", creator1, 0, [role1, role2, role3], [user1, user2, user3]))
