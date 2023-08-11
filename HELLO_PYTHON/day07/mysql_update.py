# STEP 1 : import
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8') # 한글처리 (charset = 'utf8')

e_id="3"
e_name="5"
sex="5"
addr = "5"
 
cur = con.cursor()
 
sql=f"""update emp set 
    e_name='{e_name}', sex='{sex}', addr='{addr}'
    where e_id='{e_id}' """
    
cur.execute(sql)
print("cnt : ", cur.rowcount) # cursor에 rowcount를 가지고 있음. 이를 활용해서 출력 가능. 이 방법을 추천
con.commit() # commit 필수!

cur.close()
con.close()