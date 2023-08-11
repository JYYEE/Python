# import pymysql
# conn=pymysql.connect(HOST='127.0.0.1', USER='root', PASSWORD='python', db='python', CHARSET='utf8')
# cur = conn.cursor()
# cur.execute("SELECT * FROM emp")
# print(" e_id    e_name    sex    addr")
# print("===============================")
# row = None
# while (True) :
#     row = cur.fetchone()
#     if row == None :
#         break
#
#     data1 = row[0]
#     data2 = row[1]
#     data3 = row[2]
#     data4 = row[3]
#     print("%s %10s %25s %10s" % (data1, data2, data3, data4))
#
# conn.close()

# STEP 1 : import
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성(자바에서 statement로 사용)
cur = con.cursor()
 
# STEP 4: SQL문 실행 및 Fetch
sql = "SELECT * FROM emp"
cur.execute(sql)
 
# 데이타 Fetch
rows = cur.fetchall()
print(rows)     # 전체 rows

# STEP 5: DB 연결 종료 
# cursor도 메모리 많이 잡아먹어서 닫아주는게 좋음. 열린 것과 역순으로 닫힘
cur.close()
con.close()