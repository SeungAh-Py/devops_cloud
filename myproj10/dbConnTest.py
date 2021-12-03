import pymysql

conn = None
cur = None

# 데이터베이스 접속
conn = pymysql.connect(
    host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
)

# 커서
cur = conn.cursor()

# userTBL의 회원 데이터 insert
sql = ""  # 실제 사용할 쿼리

# userID, name, birthYear, addr - NOT NULL
userID = ""
name = ""
birthYear = ""
addr = ""

while True:
    userID = input("사용자 ID ==> ")
    if userID == "":
        break
    name = input("사용자 이름 ==> ")
    birthYear = input("사용자 출생년도 ==> ")
    addr = input("사용자 주소 ==> ")

    sql = (
        "INSERT INTO userTBL (userID, name, birthYear, addr, mDate) VALUES "
        "( '"
        + userID
        + "', '"
        + name
        + "',  "
        + birthYear
        + ", '"
        + addr
        + "', CURDATE())"
    )
    cur.execute(sql)

conn.commit()
conn.close()


# 과제 userID, name, birthYear, addr, mobile1, mobile2, height(NULL 없이 모든 컬럼의 데이터) INSERT
