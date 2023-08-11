import pymysql
class DaoEmp:
    def __init__(self): # 생성자
        self.con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
        # pymysql.cursors.DictCursor : 데이터를 딕셔너리 형태로 넘겨줌
    
    def selectList(self):
        sql = "SELECT * FROM emp"
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
    
    def selectOne(self, e_id):
        sql = f"""select 
                e_id, e_name, sex, addr
                from emp where e_id={e_id}"""
        self.cur.execute(sql)
        emp = self.cur.fetchone()
        return emp
    
    def insert(self, e_id, e_name, sex, addr):
        sql = f"insert into emp values({e_id},{e_name},{sex},{addr})"
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        return cnt
    
    def update(self, e_id, e_name, sex, addr):
        sql=f"""update emp set 
                e_name='{e_name}', sex='{sex}', addr='{addr}'
                where e_id='{e_id}' """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        return cnt 
    
    def delete(self, e_id):
        sql=f"""delete from emp 
                where e_id='{e_id}' """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        return cnt
            
    def __del__(self):
        self.cur.close()
        self.con.close()
        
if __name__=='__main__':
    de = DaoEmp()
    