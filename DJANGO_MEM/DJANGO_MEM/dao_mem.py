import pymysql

class DaoMem:
    def __init__(self):
        self.con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = "SELECT * FROM mem"
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
    
    def selectOne(self, m_id):
        sql = f"""select 
            m_id, m_name, tel, address
            from mem where m_id={m_id}"""
        self.cur.execute(sql)
        mem = self.cur.fetchone()
        return mem
    
    def insert(self, m_id, m_name, tel, address):
        sql = f"insert into mem values({m_id},{m_name},{tel},{address})"
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        return cnt
    
    def update(self, m_id, m_name, tel, address):
        sql=f"""update mem set 
            m_name='{m_name}', tel='{tel}', address='{address}'
            where m_id={m_id} """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        return cnt 
    
    def delete(self, m_id):
        sql=f"""delete from mem 
            where m_id={m_id} """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        return cnt
            
    def __del__(self):
        self.cur.close()
        self.con.close()
        
if __name__=='__main__':
    dao = DaoMem()