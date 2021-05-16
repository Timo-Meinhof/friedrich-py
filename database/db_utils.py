import sqlite3

def init_db(conn):
    c = conn.cursor()

    #Setup Prgama
    c.execute(""" PRAGMA foreign_keys = ON; """)

    # Create dates table
    c.execute("""
        CREATE TABLE IF NOT EXISTS dates (
            id INTEGER PRIMARY KEY,
            gid TEXT,
            title TEXT,
            subtitle TEXT,
            subject TEXT,
            description TEXT,
            due_date TEXT,
            due_time TEXT,
            repeat INTEGER,
            create_date TEXT,
            create_time TEXT,
            creator TEXT,
            expired INTEGER,
            FOREIGN KEY (subject) REFERENCES subjects (name),
            FOREIGN KEY (repeat) REFERENCES repeat (id)
            FOREIGN KEY (creator) REFERENCES creators (id)
        );
    """)   

    # Create subjects table
    c.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            name TEXT PRIMARY KEY,
            exam_ects REAL,
            prac_ects REAL,
            exam_description TEXT,
            prac_description TEXT,
            studon_url TEXT,
            zoom_url TEXT,
            contact TEXT,
            further_info TEXT,
            ping_tag TEXT,
            color TEXT
        );
    """)   

    # Create repeat table
    c.execute("""
        CREATE TABLE IF NOT EXISTS repeat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            display_name TEXT
        );
    """) 

    # Create roles table
    c.execute("""
        CREATE TABLE IF NOT EXISTS roles (
            id TEXT PRIMARY KEY,
            name TEXT,
            color TEXT
        );
    """)  

    # Create users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT,
            color TEXT,
            studon TEXT
        );
    """)  

    # Create dates_ping_roles table
    c.execute("""
        CREATE TABLE IF NOT EXISTS dates_ping_roles (
            date_id INTEGER,
            role_id TEXT,
            PRIMARY KEY (date_id, role_id)
            FOREIGN KEY (date_id) REFERENCES dates (id),
            FOREIGN KEY (role_id) REFERENCES roles (id)
        );
    """)  

    # Create dates_ping_users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS dates_ping_users (
            date_id INTEGER,
            user_id TEXT,
            PRIMARY KEY (date_id, user_id)
            FOREIGN KEY (date_id) REFERENCES dates (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
    """)  

    # Create creators table
    c.execute("""
        CREATE TABLE IF NOT EXISTS creators (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login_name TEXT,
            password TEXT,
            discord_user TEXT,
            FOREIGN KEY (discord_user) REFERENCES users (id)
        );
    """)  