"""score 1 : closest
score 2 : second closest
score 3 : third closest

if on dirty cell:
    clean
if no score 1:
    return 0

if only one score 1:
    go to score 1
else:
    if there is only one score 2:
        go to the farest from score 2
    else:
        if there is only one score 3:
            go to the farthest from score 3
        else:
            pick random closest



"""
def find_closest(srange, pos_i, pos_j, board, width, height):
    i = (srange * -1) #we are iterating on all rows except the peaks
    j = 0
    ret = set()
    while i < 0:
        if pos_i + i >= 0 and pos_j + j < width:
            if board[pos_i + i][pos_j + j] == 'd':
                ret.add((pos_i + i, pos_j + j))
        if pos_i + i >= 0 and pos_j + j * -1 >= 0:
            if board[pos_i + i][pos_j + j * -1] == 'd':
                ret.add((pos_i + i, pos_j + j * -1))
        i += 1
        j += 1
    while i <= srange:
        if pos_i + i < height and pos_j + j < width:
            if board[pos_i + i][pos_j + j] == 'd':
                ret.add((pos_i + i, pos_j + j))
        if pos_i + i < height and pos_j + j * -1 >= 0:        
            if board[pos_i + i][pos_j + j * -1] == 'd':
                ret.add((pos_i + i, pos_j + j * -1))
        i += 1
        j -= 1
    return list(ret)

def check_farthest(closest, next_step):
    res = 0
    for i, t in enumerate(closest):
        sub = (t[0] - next_step[0], t[1] - next_step[1])
        subsum = abs(sub[0]) + abs(sub[1])
        if subsum > res:
            res = subsum
            ret = i
    return closest[ret]

def get_dest(pos_i, pos_j, board, width, height):
    closest = list()
    next_step = list()
    farthest = list()
    srange = 1
    while not closest and (srange < width and srange < height):
        closest = find_closest(srange, pos_i, pos_j, board, width, height)
        srange += 1
    if not closest:
        return None
    elif len(closest) == 1:
        return closest[0]    
    else:
        while not next_step and (srange < width or srange < height):
            next_step = find_closest(srange, pos_i, pos_j, board, width, height)
            srange += 1
    if not next_step:
        return closest[0]
    elif len(next_step) == 1:
        return check_farthest(closest, next_step[0])
    else:
        while not farthest and (srange < width or srange < height):
            farthest = find_closest(srange, pos_i, pos_j, board, width, height)
            srange += 1
    if not farthest:
        return closest[0]
    elif len(farthest) == 1:
        return check_farthest(closest, farthest[0])
    else:
        return closest[0]

def next_move(pos_i, pos_j, board):
    width = len(board[0])
    height = len(board)
    print(get_dest(pos_i, pos_j, board, width, height))

board = ["--dd-",
         "-----",
         "--d--",
         "--d--",
         "-----"]

# a = [(0, 1), (1, 0)]
# b = (0, 5)
# print(check_farthest(a, b))
next_move(1, 2, board)