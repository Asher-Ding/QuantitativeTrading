import sqlite3
import pytest
# Import the Diary class from the app.modules.diary module
from app.modules.diary.diary_controller import Diary

# Fixture to create a Diary object for each test case
@pytest.fixture
def diary():
    diary = Diary(':memory:')
    yield diary
    diary.close()

# Test the create_table() method
def test_create_table(diary):
    diary.create_table()
    # Get the names of all tables in the database
    diary.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = diary.cur.fetchall()
    # Check that the 'diary' table exists
    assert ('diary',) in tables
    
# Test the insert() method
def test_insert(diary):
    diary.create_table()
    # Insert a row into the 'diary' table
    diary.insert('2021-01-01 00:00:00', 'open', 0.0, 0.0, 'long', 1, 0.0, 0.0, 1)
    # Select all rows from the 'diary' table
    diary.cur.execute("SELECT * FROM diary")
    rows = diary.cur.fetchall()
    # Check that the row was inserted
    assert rows[0] == ('2021-01-01 00:00:00', 'open', 0.0, 0.0, 'long', 1, 0.0, 0.0, 1)
    
# Test the select_all() method
def test_select_all(diary):
    diary.create_table()
    # Insert two rows into the 'diary' table
    diary.insert('2021-01-01 00:00:00', 'open', 0.0, 0.0, 'long', 1, 0.0, 0.0, 1)
    diary.insert('2021-01-01 00:00:00', 'open', 0.0, 0.0, 'long', 1, 0.0, 0.0, 1)
    # Select all rows from the 'diary' table
    rows = diary.select_all()
    # Check that the two rows were inserted
    assert rows[0] == ('2021-01-01 00:00:00', 'open', 0.0, 0.0, 'long', 1, 0.0, 0.0, 1)
    assert rows[1] == ('2021-01-01 00:00:00', 'open', 0.0, 0.0, 'long', 1, 0.0, 0.0, 1)