# STEP 1 : import
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성(자바에서 statement로 사용)
cur = con.cursor()
 
# STEP 4: SQL문 실행 및 Fetch
# sql = "insert into emp values (3,3,3,3)"
# cur.execute(sql)
# """ : 멀티라인. 줄바꿈 허용. sql 작성할 때 효율적
# 
sql="""insert into emp 
values (%s,%s,%s,%s)"""
cur.execute(sql,('4','4','4','4'))

con.commit() # commit 필수!

# STEP 5: DB 연결 종료 
# cursor도 메모리 많이 잡아먹어서 닫아주는게 좋음. 열린 것과 역순으로 닫힘
cur.close()
con.close()