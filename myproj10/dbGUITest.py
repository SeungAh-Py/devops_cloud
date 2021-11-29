import pymysql

conn = None
cur = None

# 데이터베이스 접속
conn = pymysql.connect(
    host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
)

# 커서
cur = conn.cursor()

# 실제 사용할 쿼리
sql = "SELECT userID, name, birthYear, addr, IFNULL(CONCAT(mobile1, '-', mobile2), '-') AS mobile, IFNULL(height, 0), IFNULL(mDate, '-') FROM userTBL"

cur.execute(sql)
print("회원 ID    회원명 출생년도    주소  연락처 키   가입일")
print("-----------------------------------------------------------------")

while True:
    row = cur.fetchone()
    if row == None:
        break
    userID = row[0]
    name = row[1]
    birthYear = row[2]
    addr = row[3]
    if row[4] == None:
        mobile = "-"
    else:
        mobile = row[4]
    if row[5] == None:
        height = 0
    else:
        height = row[5]
    if row[6] == None:
        mobile = "-"
    else:
        mDate = row[6]

    print(
        "%5s %5s %d %5s %10s %d %5s"
        % (userID, name, birthYear, addr, mobile, height, mDate)
    )
conn.close()


# 과제 userID, name, birthYear, addr, mobile1, mobile2, height(NULL 없이 모든 컬럼의 데이터) INSERT
