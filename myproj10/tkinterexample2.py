from tkinter import *

# 문자를 표현할 수 있는 라벨 사용

window = Tk()
window.title("윈도우창 연습")  # 고정 표시줄 네이밍
window.geometry("400x100")  # 넓이 * 높이

label1 = Label(window, text="This is MariaDB를")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(
    window,
    text="공부 중입니다.",
    font=("궁서체", 15),
    fg="seagreen",
    bg="magenta",
    width=15,
    height=5,
)  # 레이블이 올라갈 윈도우, 출력될 글, 설정 : font, fg=폰튼색, bg=배경색, anchor는 위치(default값은 센터, SE, WN...)

# 위젯 적용
label1.pack()
label2.pack()
label3.pack()

# window.resizable(width=FALSE, height=TRUE)  # 실행창 사이즈 고정


# GUI 화면 코딩
window.mainloop()
