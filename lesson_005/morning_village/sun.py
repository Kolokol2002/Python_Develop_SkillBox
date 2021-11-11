import simple_draw as sd

def draw_sun(x, y, size, color=sd.COLOR_YELLOW):

    sd.circle(center_position=sd.get_point(x, y), radius=size*25, color=color, width=0)

    for angle in range(0, 360, 40):
        sun = sd.get_vector(start_point=sd.get_point(x, y), angle=angle, length=size*50, width=size*2)
        sun.draw(color=color)
