import turtle
import colorsys

# 사용자에게 속도 입력 받기
print("터틀 속도를 입력하세요 (1: 느림 ~ 10. 빠름, 기본값: 5)")
try:
        user_speed = int(input("속도 : ") or 5)
        if user_speed < 0 or user_speed > 10:
                print("속도는 1~10 사이여야 합니다. 기본값 5로 설정됩니다.")
                user_speed = 5
except ValueError:
        print("숫자가 아닌 값이 입력되었습니다. 기본값 5로 설정됩니다.")
        user_speed = 5

# 터틀 설정
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(user_speed)     # 입력한 속도 반영
t.width(2)

# 색상 설정
colors = []
h = 0
for i in range(360):
        colors.append(colorsys.hsv_to_rgb(h, 1, 1))
        h += 0.027

# 그리기
for i in range(3600):
    t.color(colors[i % 36])
    t.forward(i * 3)
    t.right(144)
    t.forward(i * 3)
    t.right(144)
    t.right(1)
turtle.done()