import sqlite3

# Junhao Wang
def to_trans_dict(trans_tuple):
    trans = {'item #': trans_tuple[0], 'amount': trans_tuple[1],
             'category': trans_tuple[2], 'date': trans_tuple[3], 'desc': trans_tuple[4]}
    return trans

# Junhao Wang
def to_trans_date_dict(trans_tuple):
    trans = {'Sum': trans_tuple[0], 'date': trans_tuple[1]}
    return trans
# Junhao Wang
def to_trans_category_dict(trans_tuple):
    trans = {'Sum': trans_tuple[0], 'category': trans_tuple[1]}
    return trans
# Junhao Wang
def to_trans_dict_list(trans_tuples):
    return [to_trans_dict(trans) for trans in trans_tuples]


class Transaction:
    # Junhao Wang
    def __init__(self, dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (amount integer, category text, date text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile
    # Junhao Wang
    def select_all(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    #Tingwei Liu
    def select_one(self,rowid):
        
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict(tuples[0])
    
    # Junhao Wang
    def add(self, item):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",
                    (item['amount'], item['category'], item['date'], item['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]
    
    # Junhao Wang
    def delete(self, rowid):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);''', (rowid,))
        con.commit()
        con.close()

    # Junhao Wang
    def sum_date(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT sum(amount) as Sum, date from transactions group by date")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_trans_date_dict(trans) for trans in tuples]
    # Junhao Wang
    def sum_month(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT sum(amount) as Sum, strftime('%Y-%m',date) as month 
			from transactions group by month ORDER BY month desc""")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_trans_date_dict(trans) for trans in tuples]

    #Zihao Liu
    def sum_year(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT sum(amount) as Sum, strftime('%Y',date) as year 
			from transactions group by year""")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_trans_date_dict(trans) for trans in tuples]

    #Zihao Liu
    def sum_cat(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT sum(amount) as Sum, category from transactions 
			group by category order by Sum desc""")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_trans_category_dict(trans) for trans in tuples]
