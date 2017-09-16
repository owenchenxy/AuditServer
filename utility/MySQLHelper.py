import MySQLdb
from conf import HOST,USER,PASSWORD,DB
class MySQLHelper(object):
    def __init__(self):
        self.db=DB
        self.host=HOST
        self.user=USER
        self.password=PASSWORD
        
    def GetDataOne(self,sql,params):
        conn=MySQLdb.connect(self.host,self.user,self.password,self.db)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        
        cur.execute(sql,params)
        data_dict=cur.fetchone()
        
        cur.close()
        conn.close()
        return data_dict
    
    def GetDataAll(self,sql,params):
        conn=MySQLdb.connect(self.host,self.user,self.password,self.db)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        
        cur.execute(sql,params)
        data_dict_list=cur.fetchall()
        
        cur.close()
        conn.close()
        return data_dict_list
    
    def Modify(self,sql,params):
        conn=MySQLdb.connect(self.host,self.user,self.password,self.db)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        
        cur.executemany(sql,params)
        conn.commit()
        
        cur.close()
        conn.close()