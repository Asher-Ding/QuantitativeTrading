import sqlite3
import pytest
from app.models.diary import Diary

# Fixture to create a Diary object for each test case
@pytest.fixture
def diary():
    diary = Diary(':memory:')
    yield diary
    diary.close()

# Test create_entry() method
def test_create_entry(diary):
    title = 'Test Entry'
    content = 'This is a test entry.'
    entry_id = diary.create_entry(title, content)
    assert entry_id == 1

# Test read_entries() method
def test_read_entries(diary):
    # Insert two entries into the database
    diary.create_entry('Entry 1', 'This is entry 1.')
    diary.create_entry('Entry 2', 'This is entry 2.')
    entries = diary.read_entries()
    assert len(entries) == 2
    assert entries[1][1] == 'Entry 2'  # Check that the entries are ordered by created_at DESC

# Test update_entry() method
def test_update_entry(diary):
    title = 'Test Entry'
    content = 'This is a test entry.'
    diary.create_entry(title, content)
    diary.update_entry(1, 'New Title', 'New Content')
    entries = diary.read_entries()
    assert entries[0][1:3] == ('New Title', 'New Content')

# Test delete_entry() method
def test_delete_entry(diary):
    diary.create_entry('Entry to delete', 'This entry will be deleted.')
    diary.delete_entry(1)
    entries = diary.read_entries()
    assert len(entries) == 0