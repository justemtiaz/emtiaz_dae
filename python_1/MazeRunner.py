import tkinter as tk

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", "#", " ", "#"],
    ["#", "#", "#", "#", " ", "#", "E", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"]
]

player_pos = [1, 1]

root = tk.Tk()
root.title("MazeRunner")

canvas_size = 400
rows = len(maze)
cols = len(maze[0])
cell_size = canvas_size // rows

canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

def draw_maze():
    canvas.delete("all")
    colors = {"#": "black", " ": "white", "E": "green"}
    for y in range(rows):
        for x in range(cols):
            color = colors[maze[y][x]]
            canvas.create_rectangle(x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size, fill=color)
    px, py = player_pos[1], player_pos[0]
    canvas.create_rectangle(px*cell_size, py*cell_size, (px+1)*cell_size, (py+1)*cell_size, fill="blue")

def move(event):
    y, x = player_pos
    if event.keysym == "Up" and maze[y-1][x] != "#":
        player_pos[0] -= 1
    elif event.keysym == "Down" and maze[y+1][x] != "#":
        player_pos[0] += 1
    elif event.keysym == "Left" and maze[y][x-1] != "#":
        player_pos[1] -= 1
    elif event.keysym == "Right" and maze[y][x+1] != "#":
        player_pos[1] += 1
    draw_maze()
    if maze[player_pos[0]][player_pos[1]] == "E":
        canvas.create_text(canvas_size//2, canvas_size//2, text="You Win!", font=("Arial", 30), fill="red")

root.bind("<Up>", move)
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Right>", move)

draw_maze()
root.mainloop()