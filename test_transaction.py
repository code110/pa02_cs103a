
import pytest
from transactions import Transaction, to_trans_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    trans1 = {'amount':50,'category':'food','date':'2021-10-5','desc':'hamburger'}
    trans2 = {'amount':1000,'category':'shopping','date':'2021-10-5','desc':'clothes'}
    trans3 = {'amount':30,'category':'food','date':'2021-11-9','desc':'subway'}
    trans4 = {'amount':250,'category':'shopping','date':'2021-11-5','desc':'daily'}
    trans5 = {'amount':100,'category':'gas','date':'2021-12-5','desc':'gas fee'}
    id1=empty_db.add(trans1)
    id2=empty_db.add(trans2)
    id3=empty_db.add(trans3)
    id4=empty_db.add(trans4)
    id5=empty_db.add(trans5)
    yield empty_db
    empty_db.delete(id5)
    empty_db.delete(id4)
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)