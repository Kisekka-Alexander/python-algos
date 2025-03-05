import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(line_len, my_turtle):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(line_len - 10, my_turtle)
        
draw_spiral(100, my_turtle)
my_win.exitonclick()
