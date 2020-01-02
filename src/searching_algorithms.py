import PySimpleGUI as sg

CANVAS_HEIGHT = 816  # for even # squares
CANVAS_WIDTH = 1392  # full
BLOCK_HEIGHT_WIDTH = 8  # pixel width and height
NUM_ELEMENTS_X = (CANVAS_WIDTH // BLOCK_HEIGHT_WIDTH)
NUM_ELEMENTS_Y = (CANVAS_HEIGHT // BLOCK_HEIGHT_WIDTH)
NUM_ELEMENTS = NUM_ELEMENTS_X * NUM_ELEMENTS_Y
BASE_FILL = 'Silver'
MAX_COLOR = 16777215

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light gray', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'Slategray1', 'Slategray2', 'Slategray3',
          'Slategray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlategray1', 'DarkSlategray2', 'DarkSlategray3', 'DarkSlategray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1']


def clear_graph(graph, graph_elements):
    for row in graph_elements:
        for val in row:
            graph.TKCanvas.itemconfig(val, fill=BASE_FILL)



def draw_boxes(graph, rectangles, elements):
    clear_graph(graph, rectangles)  # clear graph elements & clear their IDs
    for i in range(len(elements)):  # When appending to list, allows us to
        # save
        # all figures
        rectangles.append(graph.DrawRectangle((i * BLOCK_WIDTH, elements[i]),
                                              (i * BLOCK_WIDTH + BLOCK_WIDTH,
                                               0),
                                              fill_color='black',
                                              line_color='white'))


def draw_boxes_and_read(graph, rectangles, elements, timeout):
    draw_boxes(graph, rectangles, elements)
    window.read(timeout)


sg.ChangeLookAndFeel('DarkAmber')

layout = [
    [sg.Graph(canvas_size=(CANVAS_WIDTH, CANVAS_HEIGHT),
              graph_bottom_left=(0, 0),
              graph_top_right=(CANVAS_WIDTH, CANVAS_HEIGHT),
              background_color='grey',
              key='traversalGraph',
              enable_events=True,
              drag_submits=True)],
    [sg.T('Generate, and select Searching method:'), sg.Button(
        'Generate'), sg.Button('Clear'), sg.Button('DFS'),
     sg.Button('BFS'), sg.Button('Dijkstra'), sg.Button(
        'A*'), sg.Button('Start'), sg.Button('End')]
]

window = sg.Window('Searching Visualization', layout)
window.Finalize()

graph = window['traversalGraph']
boxes = [[0 for i in range(NUM_ELEMENTS_X)] for j in range(NUM_ELEMENTS_Y)]
last_mouse = (None, None)
mouse = (None, None)
color_iterator = 1

enable_start = enable_end = False
start_point = end_point = (0,0)

while True:
    event, values = window.read()
    last_mouse = mouse
    mouse = values['traversalGraph']

    if event is None:
        break
    if event == 'Generate':
        for y in range(NUM_ELEMENTS_Y):
            for x in range(NUM_ELEMENTS_X):
                x_stretched, y_stretched = x * BLOCK_HEIGHT_WIDTH, \
                                           y * BLOCK_HEIGHT_WIDTH
                # pixel locations
                boxes[y][x] = (graph.DrawRectangle((x_stretched,
                                                    y_stretched +
                                                    BLOCK_HEIGHT_WIDTH),
                                                   (
                                                       x_stretched +
                                                       BLOCK_HEIGHT_WIDTH,
                                                       y_stretched),
                                                   fill_color=BASE_FILL,
                                                   line_color='black'))
    elif event == 'Clear':
        clear_graph(graph, boxes)
    elif event == 'Start':
        enable_start = True
    elif event == 'End':
        enable_end = True
    elif event == 'traversalGraph' and mouse != (None, None) and mouse != \
            last_mouse:
        # Clicking that happens in graph, no duplicates
        if color_iterator < len(COLORS) - 1:
            color_iterator+=1
        else:
            color_iterator=0

        print('It happened at: ', mouse)
        x, y = mouse[0] // BLOCK_HEIGHT_WIDTH, mouse[1] // BLOCK_HEIGHT_WIDTH
        graph.TKCanvas.itemconfig(boxes[y][x], fill=COLORS[color_iterator])

    elif event.endswith("+UP"):  # for dragging and letting go
        if enable_start and not enable_end:
            x, y = mouse[0] // BLOCK_HEIGHT_WIDTH, mouse[
                1] // BLOCK_HEIGHT_WIDTH
            graph.TKCanvas.itemconfig(boxes[y][x], fill='Black')
            start_point = (x, y)
            enable_start = False
        elif enable_end and not enable_start:
            x, y = mouse[0] // BLOCK_HEIGHT_WIDTH, mouse[
                1] // BLOCK_HEIGHT_WIDTH
            graph.TKCanvas.itemconfig(boxes[y][x], fill='Black')
            end_point = (x, y)
            enable_end = False
            print(f"Starting at {start_point} and ending at {end_point}")
