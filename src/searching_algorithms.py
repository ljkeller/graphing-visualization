import PySimpleGUI as sg
from math import sqrt

CANVAS_HEIGHT = 816  # for even # squares
CANVAS_WIDTH = 1392  # full
BLOCK_HEIGHT_WIDTH = 8  # pixel width and height
NUM_ELEMENTS_X = (CANVAS_WIDTH // BLOCK_HEIGHT_WIDTH)
NUM_ELEMENTS_Y = (CANVAS_HEIGHT // BLOCK_HEIGHT_WIDTH)
NUM_ELEMENTS = NUM_ELEMENTS_X * NUM_ELEMENTS_Y
BASE_FILL = 'Silver'
MAX_COLOR = 16777215
COLOR_COUNTER = 0

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white',
          'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque',
          'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue',
          'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray',
          'slate gray',
          'light slate gray', 'gray', 'light gray', 'midnight blue', 'navy',
          'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue',
          'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue',
          'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise',
          'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine',
          'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green',
          'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green',
          'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki',
          'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod',
          'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink',
          'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet',
          'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1',
          'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4',
          'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3',
          'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2',
          'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3',
          'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2',
          'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1',
          'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4',
          'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1',
          'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3',
          'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1',
          'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'Slategray1', 'Slategray2',
          'Slategray3',
          'Slategray4', 'LightSteelBlue1', 'LightSteelBlue2',
          'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3',
          'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1',
          'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2',
          'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4',
          'cyan2', 'cyan3',
          'cyan4', 'DarkSlategray1', 'DarkSlategray2', 'DarkSlategray3',
          'DarkSlategray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2',
          'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1',
          'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3',
          'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3',
          'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1',
          'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3',
          'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3',
          'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3',
          'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3',
          'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3',
          'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1',
          'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3',
          'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2',
          'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3',
          'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4',
          'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4',
          'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3',
          'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3',
          'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2',
          'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2',
          'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4',
          'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1',
          'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3',
          'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3',
          'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2',
          'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3',
          'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1',
          'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1']

color_gradient = ["#E100FF", "#DF01FF", "#DE02FF", "#DD03FF", "#DC04FF",
              "#DB05FF", "#DA06FF", "#D907FF", "#D708FF", "#D609FF", "#D50BFF", "#D40CFF", "#D30DFF", "#D20EFF", "#D10FFF", "#D010FF", "#CE11FF", "#CD12FF", "#CC13FF", "#CB15FF", "#CA16FF", "#C917FF", "#C818FF", "#C619FF", "#C51AFF", "#C41BFF", "#C31CFF", "#C21DFF", "#C11FFF", "#C020FF", "#BF21FF", "#BD22FF", "#BC23FF", "#BB24FF", "#BA25FF", "#B926FF", "#B827FF", "#B729FF", "#B62AFF", "#B42BFF", "#B32CFF", "#B22DFF", "#B12EFF", "#B02FFF", "#AF30FF", "#AE31FF", "#AC33FF", "#AB34FF", "#AA35FF", "#A936FF", "#A837FF", "#A738FF", "#A639FF", "#A53AFF", "#A33BFF", "#A23DFF", "#A13EFF", "#A03FFF", "#9F40FF", "#9E41FF", "#9D42FF", "#9C43FF", "#9A44FF", "#9945FF", "#9847FF", "#9748FF", "#9649FF", "#954AFF", "#944BFF", "#924CFF", "#914DFF", "#904EFF", "#8F4FFF", "#8E51FF", "#8D52FF", "#8C53FF", "#8B54FF", "#8955FF", "#8856FF", "#8757FF", "#8658FF", "#8559FF", "#845BFF", "#835CFF", "#825DFF", "#805EFF", "#7F5FFF", "#7E60FF", "#7D61FF", "#7C62FF", "#7B63FF", "#7A65FF", "#7866FF", "#7767FF", "#7668FF", "#7569FF", "#746AFF", "#736BFF", "#726CFF", "#716DFF", "#6F6FFF", "#6E70FF", "#6D71FF", "#6C72FF", "#6B73FF", "#6A74FF", "#6975FF", "#6876FF", "#6677FF", "#6579FF", "#647AFF", "#637BFF", "#627CFF", "#617DFF", "#607EFF", "#5E7FFF", "#5D80FF", "#5C81FF", "#5B83FF", "#5A84FF", "#5985FF", "#5886FF", "#5787FF", "#5588FF", "#5489FF", "#538AFF", "#528BFF", "#518DFF", "#508EFF", "#4F8FFF", "#4E90FF", "#4C91FF", "#4B92FF", "#4A93FF", "#4994FF", "#4895FF", "#4797FF", "#4698FF", "#4499FF", "#439AFF", "#429BFF", "#419CFF", "#409DFF", "#3F9EFF", "#3E9FFF", "#3DA1FF", "#3BA2FF", "#3AA3FF", "#39A4FF", "#38A5FF", "#37A6FF", "#36A7FF", "#35A8FF", "#34A9FF", "#32ABFF", "#31ACFF", "#30ADFF", "#2FAEFF", "#2EAFFF", "#2DB0FF", "#2CB1FF", "#2AB2FF", "#29B3FF", "#28B5FF", "#27B6FF", "#26B7FF", "#25B8FF", "#24B9FF", "#23BAFF", "#21BBFF", "#20BCFF", "#1FBDFF", "#1EBFFF", "#1DC0FF", "#1CC1FF", "#1BC2FF", "#1AC3FF", "#18C4FF", "#17C5FF", "#16C6FF", "#15C7FF", "#14C9FF", "#13CAFF", "#12CBFF", "#10CCFF", "#0FCDFF", "#0ECEFF", "#0DCFFF", "#0CD0FF", "#0BD1FF", "#0AD3FF", "#09D4FF", "#07D5FF", "#06D6FF", "#05D7FF", "#04D8FF", "#03D9FF", "#02DAFF", "#01DBFF", "#00DDFF"]
color_gradient2 = ["#FFEE00", "#FEEC01", "#FEEB02", "#FEEA03", "#FEE905",
                  "#FEE806", "#FEE607", "#FEE508", "#FEE40A", "#FEE30B", "#FEE20C", "#FEE00E", "#FDDF0F", "#FDDE10", "#FDDD11", "#FDDC13", "#FDDA14", "#FDD915", "#FDD817", "#FDD718", "#FDD619", "#FDD41A", "#FDD31C", "#FDD21D", "#FCD11E", "#FCD020", "#FCCE21", "#FCCD22", "#FCCC23", "#FCCB25", "#FCCA26", "#FCC827", "#FCC729", "#FCC62A", "#FCC52B", "#FCC42C", "#FBC22E", "#FBC12F", "#FBC030", "#FBBF31", "#FBBE33", "#FBBC34", "#FBBB35", "#FBBA37", "#FBB938", "#FBB839", "#FBB63A", "#FAB53C", "#FAB43D", "#FAB33E", "#FAB240", "#FAB141", "#FAAF42", "#FAAE43", "#FAAD45", "#FAAC46", "#FAAB47", "#FAA949", "#FAA84A", "#F9A74B", "#F9A64C", "#F9A54E", "#F9A34F", "#F9A250", "#F9A152", "#F9A053", "#F99F54", "#F99D55", "#F99C57", "#F99B58", "#F99A59", "#F8995A", "#F8975C", "#F8965D", "#F8955E", "#F89460", "#F89361", "#F89162", "#F89063", "#F88F65", "#F88E66", "#F88D67", "#F78B69", "#F78A6A", "#F7896B", "#F7886C", "#F7876E", "#F7856F", "#F78470", "#F78372", "#F78273", "#F78174", "#F77F75", "#F77E77", "#F67D78", "#F67C79", "#F67B7B", "#F6797C", "#F6787D", "#F6777E", "#F67680", "#F67581", "#F67482", "#F67283", "#F67185", "#F67086", "#F56F87", "#F56E89", "#F56C8A", "#F56B8B", "#F56A8C", "#F5698E", "#F5688F", "#F56690", "#F56592", "#F56493", "#F56394", "#F56295", "#F46097", "#F45F98", "#F45E99", "#F45D9B", "#F45C9C", "#F45A9D", "#F4599E", "#F458A0", "#F457A1", "#F456A2", "#F454A4", "#F353A5", "#F352A6", "#F351A7", "#F350A9", "#F34EAA", "#F34DAB", "#F34CAC", "#F34BAE", "#F34AAF", "#F348B0", "#F347B2", "#F346B3", "#F245B4", "#F244B5", "#F242B7", "#F241B8", "#F240B9", "#F23FBB", "#F23EBC", "#F23CBD", "#F23BBE", "#F23AC0", "#F239C1", "#F238C2", "#F137C4", "#F135C5", "#F134C6", "#F133C7", "#F132C9", "#F131CA", "#F12FCB", "#F12ECD", "#F12DCE", "#F12CCF", "#F12BD0", "#F029D2", "#F028D3", "#F027D4", "#F026D5", "#F025D7", "#F023D8", "#F022D9", "#F021DB", "#F020DC", "#F01FDD", "#F01DDE", "#F01CE0", "#EF1BE1", "#EF1AE2", "#EF19E4", "#EF17E5", "#EF16E6", "#EF15E7", "#EF14E9", "#EF13EA", "#EF11EB", "#EF10ED", "#EF0FEE", "#EF0EEF", "#EE0DF0", "#EE0BF2", "#EE0AF3", "#EE09F4", "#EE08F6", "#EE07F7", "#EE05F8", "#EE04F9", "#EE03FB", "#EE02FC", "#EE01FD", "#EE00FF"]

color_gradient3 = ["#FFEE00", "#FEEA03", "#FEE706", "#FEE409", "#FEE10C",
             "#FDDE10", "#FDDB13", "#FDD816", "#FDD519", "#FDD21D", "#FCCF20", "#FCCC23", "#FCC926", "#FCC629", "#FBC32D", "#FBC030", "#FBBD33", "#FBBA36", "#FBB73A", "#FAB43D", "#FAB140", "#FAAE43", "#FAAB47", "#FAA84A", "#F9A54D", "#F9A250", "#F99F53", "#F99C57", "#F8995A", "#F8965D", "#F89360", "#F89064", "#F88D67", "#F78A6A", "#F7876D", "#F78470", "#F78174", "#F77E77", "#F67B7A", "#F6787D", "#F67581", "#F67284", "#F56F87", "#F56C8A", "#F5698E", "#F56691", "#F56394", "#F46097", "#F45D9A", "#F45A9E", "#F457A1", "#F454A4", "#F351A7", "#F34EAB", "#F34BAE", "#F348B1", "#F245B4", "#F242B7", "#F23FBB", "#F23CBE", "#F239C1", "#F136C4", "#F133C8", "#F130CB", "#F12DCE", "#F12AD1", "#F027D5", "#F024D8", "#F021DB", "#F01EDE", "#EF1BE1", "#EF18E5", "#EF15E8", "#EF12EB", "#EF0FEE", "#EE0CF2", "#EE09F5", "#EE06F8", "#EE03FB", "#EE00FF"]
def clear_graph(graph, graph_elements):
    for row in graph_elements:
        for val in row:
            graph.TKCanvas.itemconfig(val, fill=BASE_FILL)


def update_color(graph: sg.Graph, element: int, color_index: int):
    if graph.TKCanvas.itemconfig(element)['fill'][-1] == 'Silver':
        graph.TKCanvas.itemconfig(element, fill=color_gradient3[color_index])
        window.read(5)

# def update_colors(graph: sg.Graph, elements: list):
#     for y in range(NUM_ELEMENTS_Y):
#         for x in range(NUM_ELEMENTS_X):
#             if marked[y][x] = 1:
#                 update_list.append((x,y))




def check_end(tup, end):
    if tup == end:
        return True
    else:
        return False


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
boxes = [[0 for i in range(NUM_ELEMENTS_X)] for j in range(
    NUM_ELEMENTS_Y)]
marked = [[0 for i in range(NUM_ELEMENTS_X)] for j in range(
    NUM_ELEMENTS_Y)]
bfs_queue = []
update_list = []
last_mouse = (None, None)
mouse = (None, None)
color_iterator = 1

enable_start = enable_end = False
start_point = end_point = (-1, -1)  # false values

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
        marked = [[0 for i in range(NUM_ELEMENTS_X)] for j in range(
            NUM_ELEMENTS_Y)]
        bfs_queue.clear()
    elif event == 'Start':
        enable_start = True
    elif event == 'End':
        enable_end = True
    elif event == 'DFS':
        print(f'Start point: {start_point} and '
              f'end point: {end_point}')
        if start_point == (-1, -1) or end_point == (-1, -1):
            continue  # if start or end dont exist, ignore
        x, y = start_point[0], start_point[1]
        bfs_queue.append((x,y))
        while len(bfs_queue) > 0:
            check_end((x,y), end_point)
            x, y = bfs_queue.pop()

            above_exists = y < NUM_ELEMENTS_Y - 1
            below_exists = y > 0
            right_exists = x < NUM_ELEMENTS_X - 1
            left_exists = x > 0

            if right_exists and marked[y][x + 1] == 0:
                right = boxes[y][x + 1]
                bfs_queue.append((x+1, y))
                update_color(graph, right)
                marked[y][x+1] = 1
                if check_end((x+1, y), end_point):
                    break

            if above_exists and right_exists and marked[y + 1][x + 1] == 0:
                top_right = boxes[y + 1][x + 1]
                bfs_queue.append((x+1, y+1))
                update_color(graph, top_right)
                marked[y+1][x+1] = 1
                if check_end((x+1, y+1), end_point):
                    break
            if below_exists and right_exists and marked[y - 1][x + 1] == 0:
                bot_right = boxes[y - 1][x + 1]
                bfs_queue.append((x+1, y-1))
                update_color(graph, bot_right)
                marked[y-1][x+1] = 1
                if check_end((x+1, y-1), end_point):
                    break
            if above_exists and marked[y + 1][x] == 0:
                top = boxes[y + 1][x]
                bfs_queue.append((x, y+1))
                update_color(graph, top)
                marked[y+1][x] = 1
                if check_end((x, y+1), end_point):
                    break
            if left_exists and marked[y][x - 1] == 0:
                left = boxes[y][x - 1]
                bfs_queue.append((x-1, y))
                update_color(graph, left)
                marked[y][x-1] = 1
                if check_end((x-1, y), end_point):
                    break
            if above_exists and left_exists and marked[y + 1][x - 1] == 0:
                top_left = boxes[y + 1][x - 1]
                bfs_queue.append((x-1, y+1))
                update_color(graph, top_left)
                marked[y+1][x-1] = 1
                if check_end((x-1, y+1), end_point):
                    break
            if below_exists and left_exists and marked[y - 1][x - 1] == 0:
                bot_left = boxes[y - 1][x - 1]
                bfs_queue.append((x-1, y-1))
                update_color(graph, bot_left)
                marked[y-1][x-1] = 1
                if check_end((x-1, y-1), end_point):
                    break
            if below_exists and marked[y - 1][x] == 0:
                bot = boxes[y - 1][x]
                bfs_queue.append((x, y-1))
                update_color(graph, bot)
                marked[y-1][x] = 1
                if check_end((x, y-1), end_point):
                    break
    elif event == 'BFS':
        color_iterator = 0
        print(f'Start point: {start_point} and '
              f'end point: {end_point}')
        if start_point == (-1, -1) or end_point == (-1, -1):
            continue  # if start or end dont exist, ignore
        x, y = start_point[0], start_point[1]
        bfs_queue.append((x,y))
        while len(bfs_queue) > 0:
            check_end((x,y), end_point)
            x, y = bfs_queue.pop(0)
            color_iterator = int(sqrt(((start_point[0] - x) ** 2) + (
                    (start_point[1] - y) ** 2))) * 2
            if color_iterator >= len(color_gradient3):
                color_iterator = len(color_gradient3) - 2

            above_exists = y < NUM_ELEMENTS_Y - 1
            below_exists = y > 0
            right_exists = x < NUM_ELEMENTS_X - 1
            left_exists = x > 0

            if right_exists and marked[y][x + 1] == 0:
                right = boxes[y][x + 1]
                bfs_queue.append((x+1, y))
                update_color(graph, right, color_iterator)
                marked[y][x+1] = 1
                if check_end((x+1, y), end_point):
                    break

            if above_exists and right_exists and marked[y + 1][x + 1] == 0:
                top_right = boxes[y + 1][x + 1]
                bfs_queue.append((x+1, y+1))
                update_color(graph, top_right, color_iterator)
                marked[y+1][x+1] = 1
                if check_end((x+1, y+1), end_point):
                    break
            if below_exists and right_exists and marked[y - 1][x + 1] == 0:
                bot_right = boxes[y - 1][x + 1]
                bfs_queue.append((x+1, y-1))
                update_color(graph, bot_right, color_iterator)
                marked[y-1][x+1] = 1
                if check_end((x+1, y-1), end_point):
                    break
            if above_exists and marked[y + 1][x] == 0:
                top = boxes[y + 1][x]
                bfs_queue.append((x, y+1))
                update_color(graph, top, color_iterator)
                marked[y+1][x] = 1
                if check_end((x, y+1), end_point):
                    break
            if left_exists and marked[y][x - 1] == 0:
                left = boxes[y][x - 1]
                bfs_queue.append((x-1, y))
                update_color(graph, left, color_iterator)
                marked[y][x-1] = 1
                if check_end((x-1, y), end_point):
                    break
            if above_exists and left_exists and marked[y + 1][x - 1] == 0:
                top_left = boxes[y + 1][x - 1]
                bfs_queue.append((x-1, y+1))
                update_color(graph, top_left, color_iterator)
                marked[y+1][x-1] = 1
                if check_end((x-1, y+1), end_point):
                    break
            if below_exists and left_exists and marked[y - 1][x - 1] == 0:
                bot_left = boxes[y - 1][x - 1]
                bfs_queue.append((x-1, y-1))
                update_color(graph, bot_left, color_iterator)
                marked[y-1][x-1] = 1
                if check_end((x-1, y-1), end_point):
                    break
            if below_exists and marked[y - 1][x] == 0:
                bot = boxes[y - 1][x]
                bfs_queue.append((x, y-1))
                update_color(graph, bot, color_iterator)
                marked[y-1][x] = 1
                if check_end((x, y-1), end_point):
                    break


    elif event == 'traversalGraph' and mouse != (None, None) and mouse != \
            last_mouse and not (enable_start or enable_end):
        # Clicking that happens in graph, no duplicates
        if color_iterator < len(COLORS) - 1:
            color_iterator += 1
        else:
            color_iterator = 0

        print('It happened at: ', mouse)
        x, y = mouse[0] // BLOCK_HEIGHT_WIDTH, mouse[1] // BLOCK_HEIGHT_WIDTH
        graph.TKCanvas.itemconfig(boxes[y][x], fill='white')
        print(graph.TKCanvas.itemconfig(boxes[y][x])['fill'][-1])  # box color
        marked[y][x] = 1

    elif event.endswith("+UP"):  # for dragging and letting go
        if enable_start and not enable_end:
            if start_point != (-1, -1):  # remove last instance, if exists
                graph.TKCanvas.itemconfig(
                    boxes[start_point[1]][start_point[0]],
                    fill=BASE_FILL)
            x, y = mouse[0] // BLOCK_HEIGHT_WIDTH, mouse[
                1] // BLOCK_HEIGHT_WIDTH
            graph.TKCanvas.itemconfig(boxes[y][x], fill='Black')
            start_point = (x, y)
            enable_start = False
        elif enable_end and not enable_start:
            if start_point != (-1, -1):  # remove last instance, if exists
                graph.TKCanvas.itemconfig(
                    boxes[end_point[1]][end_point[0]],
                    fill=BASE_FILL)
            x, y = mouse[0] // BLOCK_HEIGHT_WIDTH, mouse[
                1] // BLOCK_HEIGHT_WIDTH
            graph.TKCanvas.itemconfig(boxes[y][x], fill='Black')
            end_point = (x, y)
            enable_end = False
            print(f"Starting at {start_point} and ending at {end_point}")
