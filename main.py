from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI()

DATABASE = 'data/data_simple_crm.db'

# Initialize the database and create the tables if they don't exist
def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        job_title TEXT
    );
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_id INTEGER NOT NULL,
        note TEXT,
        date TEXT,
        FOREIGN KEY (person_id) REFERENCES persons(id)
    );
    ''')
    conn.commit()
    conn.close()

# Call the function to initialize the database
init_db()

class Person(BaseModel):
    full_name: str
    email: str
    job_title: str

class PersonResponse(Person):
    id: int

class Note(BaseModel):
    person_id: int
    note: str
    date: str

class NoteResponse(Note):
    id: int

@app.post("/persons/", response_model=PersonResponse)
def create_person(person: Person):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    try:
        cur.execute('''
        INSERT INTO persons (full_name, email, job_title)
        VALUES (?, ?, ?)
        ''', (person.full_name, person.email, person.job_title))
        person_id = cur.lastrowid
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Email already registered")
    conn.close()
    return PersonResponse(id=person_id, **person.dict())

@app.get("/persons/", response_model=List[PersonResponse])
def read_persons():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT id, full_name, email, job_title FROM persons')
    rows = cur.fetchall()
    conn.close()
    return [PersonResponse(id=row[0], full_name=row[1], email=row[2], job_title=row[3]) for row in rows]

@app.post("/notes/", response_model=NoteResponse)
def create_note(note: Note):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO notes (person_id, note, date)
    VALUES (?, ?, ?)
    ''', (note.person_id, note.note, note.date))
    note_id = cur.lastrowid
    conn.commit()
    conn.close()
    return NoteResponse(id=note_id, **note.dict())

@app.get("/notes/", response_model=List[NoteResponse])
def read_notes():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT id, person_id, note, date FROM notes')
    rows = cur.fetchall()
    conn.close()
    return [NoteResponse(id=row[0], person_id=row[1], note=row[2], date=row[3]) for row in rows]

@app.get("/notes/{note_id}", response_model=NoteResponse)
def read_note(note_id: int):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT id, person_id, note, date FROM notes WHERE id = ?', (note_id,))
    row = cur.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteResponse(id=row[0], person_id=row[1], note=row[2], date=row[3])

