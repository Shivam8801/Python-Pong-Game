import turtle

window = turtle.Screen()
window.title("Pong Game By Shivam")
window.bgcolor("black")
window.setup(width=800, height=600)

# stops window from updating
window.tracer(0)

# main game loop
while True:
    window.update()
