import pymysql
from tkinter import *
from tkinter import messagebox


# 데이터베이스 연동 함수
def insertData():
    conn = None
    cur = None

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )

    # 커서
    cur = conn.cursor()

    # 회원 정보 insert 구현
    # 사용자에게 입력받은 회원 정보 초기화
    userID, name, birthYear, addr = "", "", "", ""

    # GUI에서 입력한 데이터 담기
    userID = edit1.get()
    name = edit2.get()
    birthYear = edit3.get()
    addr = edit4.get()

    # SQL 쿼리 만들기
    sql = ""
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

    print(sql)
    # 쿼리 실행
    try:
        cur.execute(sql)
    except:
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")
    else:
        # 쿼리 실행이 완료(오류 없이)
        # 1) 메시지박스로 성공 알림
        messagebox.showinfo("성공", "회원 정보가 등록 되었습니다.")
        # 2) 데이터 커밋 (진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로 고침)
        selectData()

    # GUI에 입력한 데이터 삭제
    edit1.delete(0, "end")
    edit2.delete(0, "end")
    edit3.delete(0, "end")
    edit4.delete(0, "end")

    # DB 접속 종료
    conn.close()


def selectData():
    conn = None
    cur = None
    lUserID, lName, lBirthYear, lAddr = [], [], [], []

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )

    # 커서
    cur = conn.cursor()

    # 데이터 초기화
    lUserID.append("회원 ID")
    lUserID.append("-------")

    lName.append("회원명")
    lName.append("-------")

    lBirthYear.append("출생년도")
    lBirthYear.append("-------")

    lAddr.append("회원주소")
    lAddr.append("-------")

    # select 기능 구현
    sql = "SELECT userID, name, birthYear, addr from userTBL ORDER BY mDate DESC"
    cur.execute(sql)

    while True:
        row = cur.fetchone()

        if row == None:
            break
        # lUserID, lName, lBrithYear, lAddr
        lUserID.append(row[0])
        lName.append(row[1])
        lBirthYear.append(row[2])
        lAddr.append(row[3])

    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1) 리스트 박스 초기화 (기존 데이터 삭제)
    listUserID.delete(0, listUserID.size() - 1)
    listName.delete(0, listName.size() - 1)
    listBirthYear.delete(0, listBirthYear.size() - 1)
    listAddr.delete(0, listAddr.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2, item3, item4 in zip(lUserID, lName, lBirthYear, lAddr):
        listUserID.insert(END, item1)
        listName.insert(END, item2)
        listBirthYear.insert(END, item3)
        listAddr.insert(END, item4)

    conn.close()


# 윈도우 GUI 환경 조성
window = Tk()
window.geometry("800x300")
window.title("MariaDB 연동 GUI")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

# 라벨1
label1 = Label(editFrame, text="회원 ID")
label1.pack(side=LEFT, padx=10, pady=10)

edit1 = Entry(editFrame, width=10)
edit1.pack(side=LEFT, padx=10, pady=10)

# 라벨2
label2 = Label(editFrame, text="회원명")
label2.pack(side=LEFT, padx=10, pady=10)

edit2 = Entry(editFrame, width=10)
edit2.pack(side=LEFT, padx=10, pady=10)

# 라벨3
label3 = Label(editFrame, text="출생년도")
label3.pack(side=LEFT, padx=10, pady=10)

edit3 = Entry(editFrame, width=10)
edit3.pack(side=LEFT, padx=10, pady=10)

# 라벨4
label4 = Label(editFrame, text="회원주소")
label4.pack(side=LEFT, padx=10, pady=10)

edit4 = Entry(editFrame, width=10)
edit4.pack(side=LEFT, padx=10, pady=10)

# 버튼
btnInsert = Button(editFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnSelect = Button(editFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

listUserID = Listbox(listFrame)
listUserID.pack(side=LEFT, fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listBirthYear = Listbox(listFrame)
listBirthYear.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame)
listAddr.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()
