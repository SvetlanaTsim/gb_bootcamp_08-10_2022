import turtle


def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters ==0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string
    return end_string

def draw_l_systems(t, instructions, angle, distance):
     for cmd in instructions:
         if cmd == 'F':
             t.forward(distance)
         elif cmd == '+':
             t.right(angle)
         elif cmd == '-':
             t.left(angle)

def main(iterations, axiom, rules, angle, length= 8, size=2, y_offset=0, x_offset=0, offset_angle=0, width=450, heigth=450):
    inst = create_l_system(iterations, axiom, rules)
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, heigth)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_systems(t, inst, angle, length)
    t.hideturtle()

    wn.exitonclick()

#Квадратный остров Коха
# axiom = "F+F+F+F"
# rules = {"F": "F-F+F+FFF-F-F+F"}
# iterations = 2  # top:4
# angle = 90

# Снежинка Коха
# axiom = "F--F--F"
# rules = {"F":"F+F--F+F"}
# iterations = 4 # TOP: 7
# angle = 60

# Кристалл
# axiom = "F+F+F+F"
# rules = {"F":"FF+F++F+F"}
# iterations = 3 # TOP: 6
# angle = 90

# Ковер Серпинского
# axiom = "YF"
# rules = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
# iterations = 1 # TOP: 10
# angle = 60

# Кривая Пеано-Госпера
# axiom = "FX"
# rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
# iterations = 3
# angle = 60

# Анклеты Кришны
axiom = " -X--X"
rules = {"X":"XFX--XFX"}
iterations = 4
angle = 45

# Тройная кривая дракона
# axiom = "FX+FX+FX"
# rules = {"X": "X+YF+", "Y": "-FX-Y"}
# iterations = 7
# angle = 90

# Кольца
# axiom = "F+F+F+F"
# rules = {"F":"FF+F+F+F+F+F-F"}
# iterations = 2
# angle = 90

# Кривая Мура
# axiom = "LFL-F-LFL"
# rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
# iterations = 3
# angle = 90

# Кривая Леви
# axiom = "F"
# rules = {"F":"+F--F+"}
# iterations = 8
# angle = 45

main(iterations, axiom, rules, angle, length=8, size=2)
