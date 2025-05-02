from stuConn import *

conn = connections()

## 게시판 글쓰기 1개 저장
title = input("게시글 제목을 입력하세요.>> ")
content = input("게시글 내용을 입력하세요.>> ")
# 파일첨부
bfile = []
bfile1 = input("첨부할 파일을 입력하세요.( 1.jpg )>> ")
bfile2 = input("첨부할 파일을 입력하세요.( 2.jpg )>> ")
bfile3 = input("첨부할 파일을 입력하세요.( 3.jpg )>> ")

cursor = conn.cursor()
query = "select board_seq.nextval from dual"
cursor.execute(query)
bno = cursor.fetchone()[0] # 9 / #(9,) -> bno[0]
bfile.append([bno,bfile1])
bfile.append([bno,bfile2])
bfile.append([bno,bfile3])

# 1개씩 저장이 아니라 여러개 저장을 하기 위해 리스트형태로 구성
# [
#    [9,'1.jpg'],[9,'2.jpg'],[9,'3.jpg']
# ]


# query = "insert into board values (board_seq.nextval,\
#         :btitle,:bcontent,'aaa',board_seq.currval,0,0,0,sysdate)"
# cursor.execute(query,btitle=title,bcontent=content)
# conn.commit()

# 게시글 여러개 저장

conn.close()

print("프로그램을 종료합니다.")
