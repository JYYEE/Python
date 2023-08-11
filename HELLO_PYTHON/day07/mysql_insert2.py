# STEP 1 : import
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8') # 한글처리 (charset = 'utf8')

e_id = "5"
e_name="5"
sex="5"
addr = "5"
 
cur = con.cursor()
 
# STEP 4: SQL문 실행 및 Fetch
# f스트링 : "" 앞에 f붙이기. 파라미터 받을 수 있음.
sql=f"""insert into emp 
    values ('{e_id}','{e_name}','{sex}','{addr}')"""
cnt = cur.execute(sql)

print(cnt) # 추가된 행의 개수를 반환
print("cnt : ", cur.rowcount) # cursor에 rowcount를 가지고 있음. 이를 활용해서 출력 가능. 이 방법을 추천
con.commit() # commit 필수!

# STEP 5: DB 연결 종료 
# cursor도 메모리 많이 잡아먹어서 닫아주는게 좋음. 열린 것과 역순으로 닫힘
cur.close()
con.close()