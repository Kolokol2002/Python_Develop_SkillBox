import simple_draw as sd

snowlist = []

sd.resolution = (1500, 900)

def create_snowfall(count):
    global snowlist

    for _ in range(count):
        snowlist.append([sd.random_number(50, 700), sd.random_number(550, 1200), sd.random_number(10, 25)])

def draw_snowfall_color(color):
    for x, y, length in snowlist:
        point = sd.get_point(x, y)
        # sd.start_drawing()
        sd.snowflake(center=point, length=length, color=color)

def move_snowfall():
    for i in range(len(snowlist)):
        random_x = sd.random_number(-10, 10)
        snowlist[i][1] -= 10
        snowlist[i][0] += random_x

def number_snowfall_down_screen():

    list_snow_down = []
    for i, (x, y, length) in enumerate(snowlist):
        if y < length*2:
            list_snow_down.append(snowlist[i])

    return list_snow_down

def del_snowfall():
    for i in number_snowfall_down_screen():
        snowlist.remove(i)


