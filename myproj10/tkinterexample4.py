from tkinter import *
from tkinter import messagebox


# 버튼을 사용하여 알림 창 띄우기
def clickButton():
    messagebox.showinfo("버튼 클릭", "버튼을 클릭했습니다.")  # (messagebox 타이틀, messagebox 내용)


window = Tk()
window.title("버튼 이벤트 연습")  # 고정 표시줄 네이밍

button1 = Button(window, text="요기 눌러요1", fg="red", bg="yellow", command=clickButton)
button2 = Button(window, text="요기 눌러요2", fg="red", bg="yellow", command=clickButton)
button3 = Button(window, text="요기 눌러요3", fg="red", bg="yellow", command=clickButton)

button1.pack(
    side=TOP, padx=10, pady=10
)  # pad : 패딩값 / padx : x축 패딩값 / pady : y축 패딩값 / side : 정렬값(TOP/LEFT/RIGHT/BOTTOM)
button2.pack(side=TOP, padx=10, pady=10)
button3.pack(side=TOP, padx=10, pady=10)

# GUI 화면 코딩
window.mainloop()
