import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk as tk

# 윈도우 GUI 환경 조성
window = Tk()
window.geometry("300x200")
window.title("P_Ma_BBS Login")

# 1) 사용자 id와 pw를 저장하는 변수 만들기
user_id, password = StringVar(), StringVar()

# 1-1) ID와 PW를 비교하는 함수
def check_data():
    conn = None
    cur = None

    # 데이터베이스 접속
    conn = pymysql.connect(host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"    )

    # 커서
    cur = conn.cursor()

    try user_id.get() == "KSA" and password.get() == "1234":
        cur.excute(sql)
    except:
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")
    else:
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")


# 1-2) 데이터베이스 연동 함수
def insertData():
    conn = None
    cur = None

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )

    # 커서
    cur = conn.cursor()


# 1-3) id, password, login 버튼 UI 만들기
# 라벨1
tk.Label(window, text="ID : ").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Password :").grid(row=1, column=0, padx=10, pady=10)

tk.Entry(window, textvariable=user_id).grid(row=0, column=1, padx=10, pady=10)
tk.Entry(window, textvariable=password, show="*").grid(
    row=1, column=1, padx=10, pady=10
)
tk.Button(window, text="LOGIN", command=check_data).grid(
    row=2, column=1, padx=10, pady=10
)

window.mainloop()
