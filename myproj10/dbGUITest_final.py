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
    userID, name, birthYear, addr = "", "", "", ""

    # GUI에서 입력한 데이터 담기
    userID = edt1.get()
    name = edt2.get()
    birthYear = edt3.get()
    addr = edt4.get()

    # SQL 쿼리 만들기
    sql = ""
    sql = (
        "INSERT INTO userTBL (userID, name, birthYear, addr, mDate) VALUES "
        "('"
        + userID
        + "' , '"
        + name
        + "' , "
        + birthYear
        + " , '"
        + addr
        + "', CURDATE())"
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
    edt3.delete(0, "end")
    edt4.delete(0, "end")

    # DB 접속 종료
    conn.close()


# 프레임 이동(메인화면으로 돌아가기)
def backFrame():
    listFrame.pack_forget()
    label0.pack(side=TOP, padx=30, pady=30)
    pLabel.pack(expand=1, anchor=CENTER)
    editFrame.pack()
    neditFrame.pack()


def selectData():
    conn = None
    cur = None

    userID = edt1.get()
    name = edt2.get()
    birthYear = edt3.get()
    addr = edt4.get()

    editFrame.pack_forget()
    neditFrame.pack_forget()
    pLabel.pack_forget()
    label0.pack_forget()

    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    lUserID, lName, lBirthYear, lAddr = [], [], [], []

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )

    # 커서
    cur = conn.cursor()

    # 데이터 초기화
    lUserID.append("회원 ID")
    lUserID.append("---------")

    lName.append("회원명")
    lName.append("---------")

    lBirthYear.append("출생년도")
    lBirthYear.append("---------")

    lAddr.append("회원주소")
    lAddr.append("---------")

    # select 기능 구현
    sql = (
        "SELECT userID, name, birthYear, addr from userTBL WHERE userID ='"
        + userID
        + "'OR name ='"
        + name
        + "' OR birthYear = '"
        + birthYear
        + "' OR addr = '"
        + addr
        + "' ORDER BY mDate DESC"
    )
    cur.execute(sql)

    while True:
        row = cur.fetchone()

        if row == None:
            break
        # lUserID, lName, lBirthYear, lAddr
        lUserID.append(row[0])
        lName.append(row[1])
        lBirthYear.append(row[2])
        lAddr.append(row[3])

    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1)리스트 박스 초기화 (기존 데이터 삭제)
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


def newwindow():
    global new
    new = Toplevel()
    new.geometry("300x100+600+400")
    new.title("새창")

    NFrame = Frame(new)
    NFrame.pack()

    label5 = Label(NFrame, text="매우 힘들었습니다.", font=("궁서체", 20), fg="red")
    label5.pack(side=TOP)

    def close_window():
        new.destroy()

    clbtn = Button(NFrame, text="Back", command=close_window)
    clbtn.pack(side=BOTTOM, padx=10, pady=10)


# GUI 화면 구성
window = Tk()
window.geometry("900x600+300+100")
window.title("Login")

label0 = Label(window, text="User Registration")
label0.pack(side=TOP, padx=30, pady=30)

mainPhoto = PhotoImage(file="login.gif")
pLabel = Label(window, image=mainPhoto)
pLabel.pack(expand=1, anchor=CENTER)

editFrame = Frame(window)
editFrame.pack()

neditFrame = Frame(window)
neditFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
listFrame.pack_forget()

newFrame = Frame(listFrame)
newFrame.pack(sid=BOTTOM, fill=BOTH, expand=2)

label1 = Label(editFrame, text="회원 ID")
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="회원명")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="출생년도")
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(editFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text="회원 주소")
label4.pack(side=LEFT, padx=10, pady=10)


edt4 = Entry(editFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

# 버튼
btnInsert = Button(neditFrame, text="Join", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnSelect = Button(neditFrame, text="Member inquire", command=selectData)
btnSelect.pack(side=LEFT, fill=BOTH, padx=10, pady=40)

listUserID = Listbox(listFrame)
listUserID.pack(side=LEFT, fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listBirthYear = Listbox(listFrame)
listBirthYear.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame)
listAddr.pack(side=LEFT, fill=BOTH, expand=1)

btnBack = Button(newFrame, text="돌아가기", command=backFrame)
btnBack.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)

btnNewwin = Button(newFrame, text="info", command=newwindow)
btnNewwin.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)

btnlastBack = Button(newFrame, text="프로그램 종료", command=quit)
btnlastBack.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)

window.mainloop()
