import oracledb as ora

def connection():
    try:
        conn = ora.connect(user='ora_user',password='1111',
                           dsn='localhost:1521/xe')
    except Exception as e:
        print(e)
    return conn    

### 학생성적 프로그램
print("-"*40)
print("[ 학생성적 프로그램 ]")
input("원하는 번호>>")
conn = connection()
cursor = conn.cursor()
cursor.execute("select * from stuscore where sno>=:sno",sno=70)
rows = cursor.fetchall()

for row in rows:
    print(row[0])


# print("-"*30)
# print("1. 학생성적입력")
# print("2. 학생성적출력")
# print("3. 학생성적수정")
# print('4. 학생성적삭제')
# print("5. 학생성적정렬")
# print("6. 학생성적검색")
# print("0. 프로그램 종료")