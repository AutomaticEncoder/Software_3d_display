#3d software
from ursina import *
from tkinter import filedialog
app = Ursina()
file = filedialog.askopenfilename(title = 'Open model',
                                  filetypes = [('object file (.obj)', '.obj')])
model3 = Entity(model = f'{file}')
#test = Entity(model = 'cube')
def update():
    if held_keys['w']:
        model3.z -= 5 * time.dt
    if held_keys['s']:
        model3.z += 5 * time.dt
    if held_keys['a']:
        model3.x -= 5 * time.dt
    if held_keys['d']:
        model3.x += 5 * time.dt
    if held_keys['y']:
        model3.y -= 5 * time.dt
    if held_keys['h']:
        model3.y += 5 * time.dt
    if held_keys['g']:
        model3.rotation_x += 20 * time.dt
    if held_keys['f']:
        model3.rotation_x -= 20 * time.dt
    if held_keys['x']:
        model3.rotation_y += 20 * time.dt
    if held_keys['z']:
        model3.rotation_y -= 20 * time.dt
app.run()

