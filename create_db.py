import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("student_result.db")
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# ==========================
# Table: Course
# ==========================
cursor.execute('''
    CREATE TABLE IF NOT EXISTS course (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        duration TEXT NOT NULL,
        charges INTEGER NOT NULL,
        description TEXT
    )
''')

# ==========================
# Table: Student
# ==========================
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        rollno TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        gender TEXT NOT NULL,
        dob TEXT NOT NULL,
        contact INTEGER NOT NULL,
        admission INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        state TEXT NOT NULL,
        city TEXT NOT NULL,
        pin INTEGER NOT NULL,
        address TEXT NOT NULL,
        FOREIGN KEY (course_id) REFERENCES course(id) ON DELETE CASCADE
    )
''')

# ==========================
# Table: Student Log
# ==========================
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rollno TEXT,
        action TEXT,
        log_time TEXT,
        FOREIGN KEY (rollno) REFERENCES Student(rollno) ON DELETE CASCADE
    )
''')

# ==========================
# Trigger: Log student insert
# ==========================
cursor.execute('''
    CREATE TRIGGER IF NOT EXISTS log_student_insert
    AFTER INSERT ON Student
    BEGIN
        INSERT INTO student_log (rollno, action, log_time)
        VALUES (NEW.rollno, 'Student Added', DATETIME('now'));
    END;
''')




cursor.execute('''
    CREATE TABLE IF NOT EXISTS Result(
        rid INTEGER PRIMARY KEY AUTOINCREMENT,
        rollno TEXT,
        name TEXT,
        course TEXT,
        marks_ob TEXT,
        full_marks TEXT,
        per TEXT              
    )
''')
# ==========================
# SELECT Query 1: Student Logs with JOIN
# ==========================
print("\nStudent Log Entries with Trigger (JOIN on Student & Log Table):\n")
cursor.execute('''
    SELECT 
        sl.id AS Log_ID,
        s.name AS Student_Name,
        s.rollno AS Roll_No,
        sl.action AS Performed_Action,
        sl.log_time AS Action_Time
    FROM 
        student_log sl
    JOIN 
        Student s ON sl.rollno = s.rollno
    ORDER BY 
        sl.log_time ASC
''')
logs = cursor.fetchall()

print(f"{'Log_ID':<8} {'Student_Name':<20} {'Roll_No':<10} {'Performed_Action':<18} {'Action_Time'}")
print("-" * 80)
for log in logs:
    print(f"{log[0]:<8} {log[1]:<20} {log[2]:<10} {log[3]:<18} {log[4]}")

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("student_result.db")
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# ==========================
# Table: Course
# ==========================
cursor.execute('''
    CREATE TABLE IF NOT EXISTS course (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        duration TEXT NOT NULL,
        charges INTEGER NOT NULL,
        description TEXT
    )
''')

# ==========================
# Table: Student
# ==========================
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        rollno TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        gender TEXT NOT NULL,
        dob TEXT NOT NULL,
        contact INTEGER NOT NULL,
        admission INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        state TEXT NOT NULL,
        city TEXT NOT NULL,
        pin INTEGER NOT NULL,
        address TEXT NOT NULL,
        FOREIGN KEY (course_id) REFERENCES course(id) ON DELETE CASCADE
    )
''')

# ==========================
# Table: Student Log
# ==========================
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rollno TEXT,
        action TEXT,
        log_time TEXT,
        FOREIGN KEY (rollno) REFERENCES Student(rollno) ON DELETE CASCADE
    )
''')

# ==========================
# Trigger: Log student insert
# ==========================
cursor.execute('''
    CREATE TRIGGER IF NOT EXISTS log_student_insert
    AFTER INSERT ON Student
    BEGIN
        INSERT INTO student_log (rollno, action, log_time)
        VALUES (NEW.rollno, 'Student Added', DATETIME('now'));
    END;
''')

# ==========================
# 1. JOIN Query: Student Logs with Trigger
# ==========================
print("\n[1] Student Log Entries (JOIN on Student & Log Table):\n")
cursor.execute('''
    SELECT 
        sl.id AS Log_ID,
        s.name AS Student_Name,
        s.rollno AS Roll_No,
        sl.action AS Performed_Action,
        sl.log_time AS Action_Time
    FROM 
        student_log sl
    JOIN 
        Student s ON sl.rollno = s.rollno
    ORDER BY 
        sl.log_time ASC
''')
logs = cursor.fetchall()
print(f"{'Log_ID':<8} {'Student_Name':<20} {'Roll_No':<10} {'Performed_Action':<18} {'Action_Time'}")
print("-" * 80)
for log in logs:
    print(f"{log[0]:<8} {log[1]:<20} {log[2]:<10} {log[3]:<18} {log[4]}")

# ==========================
# 2. Aggregate: Count students in each course
# ==========================
print("\n[2] Total Students per Course (GROUP BY + COUNT):\n")
cursor.execute('''
    SELECT 
        c.name AS Course_Name,
        COUNT(s.rollno) AS Total_Students
    FROM 
        Student s
    JOIN 
        course c ON s.course_id = c.id
    GROUP BY 
        c.name
''')
for row in cursor.fetchall():
    print(f"Course: {row[0]}  |  Total Students: {row[1]}")

# ==========================
# 3. MAX charges in course table
# ==========================
print("\n[3] Course with Maximum Charges (MAX function):\n")
cursor.execute('''
    SELECT name, charges 
    FROM course 
    WHERE charges = (SELECT MAX(charges) FROM course)
''')
for row in cursor.fetchall():
    print(f"Course: {row[0]}  |  Charges: ₹{row[1]}")

# ==========================
# 4. Students from Maharashtra with pin > 400000 (Operator + WHERE)
# ==========================
print("\n[4] Students from Maharashtra with PIN > 400000 (Operators):\n")
cursor.execute('''
    SELECT name, rollno, city, pin 
    FROM Student 
    WHERE state = 'Maharashtra' AND pin > 400000
''')
for row in cursor.fetchall():
    print(f"{row[0]} ({row[1]}) | City: {row[2]} | PIN: {row[3]}")

# ==========================
# 5. Students with name length > 10 (Function + Condition)
# ==========================
print("\n[5] Students with long names (LENGTH function):\n")
cursor.execute('''
    SELECT name, LENGTH(name) as Name_Length 
    FROM Student 
    WHERE LENGTH(name) > 10
''')
for row in cursor.fetchall():
    print(f"{row[0]} | Length: {row[1]}")

# ==========================
# 6. First 3 Logs (LIMIT)
# ==========================
print("\n[6] First 3 Log Records (LIMIT):\n")
cursor.execute('''
    SELECT id, rollno, action, log_time 
    FROM student_log 
    ORDER BY log_time ASC 
    LIMIT 3
''')
for row in cursor.fetchall():
    print(f"LogID: {row[0]} | RollNo: {row[1]} | Action: {row[2]} | Time: {row[3]}")

# ==========================
# 7. Group By + Having: Courses with more than 1 student
# ==========================
print("\n[7] Courses with more than 1 student (GROUP BY + HAVING):\n")
cursor.execute('''
    SELECT c.name, COUNT(s.rollno) AS total
    FROM course c
    JOIN Student s ON s.course_id = c.id
    GROUP BY c.name
    HAVING total > 1
''')
for row in cursor.fetchall():
    print(f"Course: {row[0]} | Students: {row[1]}")

# Final commit and close
conn.commit()
conn.close()


