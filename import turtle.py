import turtle

# 터틀 및 스크린 설정
t = turtle.Turtle()
s = turtle.Screen()
s.title("←→↑↓ 키로 부드럽고 자연스럽게 그리기")
s.bgcolor("lightyellow")
t.shape("turtle")
t.color("darkblue")
t.pensize(3)
t.speed(0)

# 상태 플래그
moving = {"Up": False, "Down": False, "Left": False, "Right": False}

# 이동 속도
step = 5

# 방향별 이동 함수
def move_loop():
    if moving["Up"]:
        t.setheading(90)
        t.forward(step)
    if moving["Down"]:
        t.setheading(270)
        t.forward(step)
    if moving["Left"]:
        t.setheading(180)
        t.forward(step)
    if moving["Right"]:
        t.setheading(0)
        t.forward(step)
    s.ontimer(move_loop, 30)  # 30ms마다 반복

# 키 누름 처리
def press_up(): moving["Up"] = True
def press_down(): moving["Down"] = True
def press_left(): moving["Left"] = True
def press_right(): moving["Right"] = True

# 키 뗌 처리
def release_up(): moving["Up"] = False
def release_down(): moving["Down"] = False
def release_left(): moving["Left"] = False
def release_right(): moving["Right"] = False

# 유틸 기능
def clear_drawing(): t.clear()
def pen_up(): t.penup()
def pen_down(): t.pendown()

# 키 바인딩
s.listen()
s.onkeypress(press_up, "w")
s.onkeyrelease(release_up, "w")

s.onkeypress(press_down, "s")
s.onkeyrelease(release_down, "s")

s.onkeypress(press_left, "a")
s.onkeyrelease(release_left, "a")

s.onkeypress(press_right, "d")
s.onkeyrelease(release_right, "d")

s.onkeypress(clear_drawing, "c")
s.onkeypress(pen_up, "u")
s.onkeypress(pen_down, "g")

# 부드러운 이동 루프 시작
move_loop()

s.mainloop()
