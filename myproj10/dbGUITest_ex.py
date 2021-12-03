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

    # 회원 정보 insert 기능 구현
    # 사용자에게 입력받은 회원 정보 초기화
    userID, pw = "", ""

    # GUI에서 입력한 데이터 담기
    userID = edt1.get()
    pw = edt2.get()

    # SQL 쿼리 만들기
    sql = ""
    sql = (
        "INSERT INTO bbsuserTBL (userID, password) VALUES "
        "('" + userID + "' , '" + pw + "' "
    )

    print(sql)
    # 쿼리 실행
    try:
        cur.execute(sql)  # 실제 실행(DB select 실행문)
    except:
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")
    else:
        # 쿼리 실행이 완료 (오류 없이)
        # 1) 메시지박스로 성공 알림
        messagebox.showinfo("성공", "회원 정보가 등록 되었습니다.")
        # 2) 데이터 커밋 (진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로고침)
        selectData()

    # GUI에 입력한 데이터 삭제
    edt1.delete(0, "end")
    edt2.delete(0, "end")

    # DB 접속 종료
    conn.close()


# 프레임 이동(메인화면으로 돌아가기)
def backFrame():
    editFrame.pack()
    listFrame.pack_forget()


def selectData():
    conn = None
    cur = None

    userID = edt1.get()

    editFrame.pack_forget()
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    lbbsNo, luserID, ltitle, lcontext, lmdate = [], [], [], [], []

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )

    # 커서
    cur = conn.cursor()

    # select 기능 구현
    sql = (
        "SELECT bbsNo, userID, title, context, mDate from bbsTBL WHERE userID ='"
        + userID
        + "' ORDER BY bbsNo ASC"
    )
    cur.execute(sql)

    while True:
        row = cur.fetchone()

        if row == None:
            break
        # lUserID, lName, lBirthYear, lAddr
        lbbsNo.append(row[0])
        luserID.append(row[1])
        ltitle.append(row[2])
        lcontext.append(row[3])
        lmdate.append(row[4])

    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1)리스트 박스 초기화 (기존 데이터 삭제)
    listbbsNo.delete(0, listbbsNo.size() - 1)
    listuserID.delete(0, listuserID.size() - 1)
    listtitle.delete(0, listtitle.size() - 1)
    listcontext.delete(0, listcontext.size() - 1)
    listmDate.delete(0, listmDate.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2, item3, item4, item5 in zip(
        lbbsNo, luserID, ltitle, lcontext, lmdate
    ):
        listbbsNo.insert(END, item1)
        listuserID.insert(END, item2)
        listtitle.insert(END, item3)
        listcontext.insert(END, item4)
        listmDate.insert(END, item5)

    conn.close()


# GUI 화면 구성
window = Tk()
window.geometry("1200x800")
window.title("MariaDB 연동 GUI")

editFrame = Frame(window)
editFrame.pack()

# (editFrame, text="로그인 화면")

label1 = Label(editFrame, text="회원 ID")
label1.pack(side=LEFT, padx=20, pady=20)

edt1 = Entry(editFrame, width=10)
edt1.pack(side=LEFT, padx=20, pady=20)

label2 = Label(editFrame, text="비밀번호")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)


mainPhoto = PhotoImage(file="login.gif")
pLabel = Label(window, image=mainPhoto)
pLabel.pack(expand=1, anchor=CENTER)

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
listFrame.pack_forget()

# 게시판 화면
label1 = Label(listFrame, text="bbsNo")
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(listFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(listFrame, text="userID")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(listFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(listFrame, text="title")
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(listFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(listFrame, text="context")
label4.pack(side=LEFT, padx=10, pady=10)

edt4 = Entry(listFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

label5 = Label(listFrame, text="mDate")
label5.pack(side=LEFT, padx=10, pady=10)

edt5 = Entry(listFrame, width=10)
edt5.pack(side=LEFT, padx=10, pady=10)


# 버튼

btnSelect = Button(editFrame, text="LOGIN", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)


listbbsNo = Listbox(listFrame)
listbbsNo.pack(side=LEFT, fill=BOTH, expand=1)

listuserID = Listbox(listFrame)
listuserID.pack(side=LEFT, fill=BOTH, expand=1)

listtitle = Listbox(listFrame)
listtitle.pack(side=LEFT, fill=BOTH, expand=1)

listcontext = Listbox(listFrame)
listcontext.pack(side=LEFT, fill=BOTH, expand=1)

listmDate = Listbox(listFrame)
listmDate.pack(side=LEFT, fill=BOTH, expand=1)

btnInsert = Button(listFrame, text="글쓰기", command=insertData)
btnInsert.pack(side=TOP, padx=10, pady=10)

btnBack = Button(listFrame, text="돌아가기", command=backFrame)
btnBack.pack(side=TOP, padx=10, pady=10)


window.mainloop()
