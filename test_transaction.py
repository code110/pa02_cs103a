
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

#Tingwei Liu
@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    trans1 = {'amount':50,'category':'food','date':'2021-10-05','desc':'hamburger'}
    trans2 = {'amount':1000,'category':'shopping','date':'2021-10-05','desc':'clothes'}
    trans3 = {'amount':30,'category':'food','date':'2021-11-09','desc':'subway'}
    trans4 = {'amount':250,'category':'shopping','date':'2021-11-05','desc':'daily'}
    trans5 = {'amount':100,'category':'gas','date':'2021-12-05','desc':'gas fee'}
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

#Tingwei Liu
@pytest.fixture
def med_db(small_db):
    rowids=[]
    for i in range(10):
        s = str(i)
        trans ={'amount':500,
                'category':'category'+s,
                'date':'2021-08-1'+s,
                'desc':'desc'+s
                }
        rowid = small_db.add(trans)
        rowids.append(rowid)
    yield small_db
    for j in range(10):
        small_db.delete(rowids[j])

#Tingwei Liu 
@pytest.mark.add
def test_add(small_db):
    tran1 = {'amount':50,'category':'food','date':'2021-10-05','desc':'hamburger'}
    trans0=small_db.select_all()
    rowid=small_db.add(tran1)
    trans1=small_db.select_all()
    assert len(trans1)==len(trans0)+1
    tran2=small_db.select_one(rowid)
    assert tran1['amount']==tran2['amount']
    assert tran1['category']==tran2['category']
    assert tran1['date']==tran2['date']
    assert tran1['desc']==tran2['desc']

#Tingwei Liu
@pytest.mark.delete
def test_delete(med_db):
    trans1 = med_db.select_all()
    tran0 = {'amount':50,'category':'food','date':'2021-10-05','desc':'hamburger'}
    rowid = med_db.add(tran0)
    trans2 = med_db.select_all()
    med_db.delete(rowid)
    trans3 = med_db.select_all()
    assert len(trans1)==len(trans3)
    assert len(trans3) == len(trans2)-1


#Tingwei Liu
@pytest.mark.sum_date
def test_sum_date(empty_db):
    tran0={'amount':50,'category':'food','date':'2021-10-05','desc':'hamburger'}
    tran1={'amount':500,'category':'drink','date':'2021-10-05','desc':'coke'}
    tran2={'amount':5000,'category':'gas','date':'2021-10-05','desc':'car'}
    tran3={'amount':999,'category':'food','date':'2021-10-06','desc':'pizza'}
    empty_db.add(tran0)
    empty_db.add(tran1)
    empty_db.add(tran2)
    empty_db.add(tran3)
    sum_date_db=empty_db.sum_date()
    tran_sum=sum_date_db[0]
    assert tran_sum['Sum']==5550
    assert tran_sum['date']=="2021-10-05"


#Tingwei Liu
@pytest.mark.sum_month()
def test_sum_month(empty_db):
    tran0={'amount':50,'category':'food','date':'2021-10-05','desc':'hamburger'}
    tran1={'amount':500,'category':'drink','date':'2021-10-05','desc':'coke'}
    tran2={'amount':5000,'category':'gas','date':'2021-11-05','desc':'car'}
    tran3={'amount':999,'category':'food','date':'2021-11-05','desc':'pizza'}
    empty_db.add(tran0)
    empty_db.add(tran1)
    empty_db.add(tran2)
    empty_db.add(tran3)
    sum_db=empty_db.sum_month()
    tran_sum=sum_db[1]
    assert tran_sum['Sum']==550
    assert tran_sum['date']=="2021-10"
    tran_sum1=sum_db[0]
    assert tran_sum1['Sum']==5999
    assert tran_sum1['date']=="2021-11"

#Tingwei Liu
@pytest.mark.sum_year()
def test_sum_year(empty_db):
    tran0={'amount':50,'category':'food','date':'2023-10-05','desc':'hamburger'}
    tran1={'amount':500,'category':'drink','date':'2022-10-05','desc':'coke'}
    tran2={'amount':5000,'category':'gas','date':'2023-11-05','desc':'car'}
    tran3={'amount':999,'category':'food','date':'2020-12-06','desc':'pizza'}
    empty_db.add(tran0)
    empty_db.add(tran1)
    empty_db.add(tran2)
    empty_db.add(tran3)
    sum_db=empty_db.sum_year()
    tran_sum=sum_db[2]
    assert tran_sum['Sum']==5050
    assert tran_sum['date']=="2023"

    
