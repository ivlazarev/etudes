WIDTH, HEIGHT = 80, 23

CELLS = set()

def neighbours_count(x, y):
    """
    NW    N    NE
    W   (x,y)   E
    SW    S    SE
    """
    #global CELLS
    #global WIDTH
    #global HEIGHT
    crds = lambda x, y : (x % WIDTH, y % HEIGHT)
    N  = lambda x, y: crds(x, y+1)
    E  = lambda x, y: crds(x+1, y)
    S  = lambda x, y: crds(x, y-1)
    W  = lambda x, y: crds(x-1, y)
    NE = lambda x, y: crds(x+1, y+1)
    NW = lambda x, y: crds(x-1, y+1)
    SE = lambda x, y: crds(x+1, y-1)
    SW = lambda x, y: crds(x-1, y-1)
    
    tiles = [N(x,y), E(x,y), S(x,y), W(x,y), NE(x,y), NW(x,y), SE(x,y), SW(x,y)]
    return len(list(filter(lambda z : z, map(lambda x : x in CELLS, tiles))))

def calculate_generation():
    #global CELLS
    #global WIDTH
    #global HEIGHT
    newGeneration = []
    toDie = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            nc = neighbours_count(x, y)
            newStatus = False
            if (2 == nc) and ((x,y) in CELLS):
                newStatus = True
            elif (3 == nc):
                newStatus = True

            if newStatus:
                newGeneration.append((x,y))
            elif (x,y) in CELLS:
                toDie.append((x, y))
    for x in toDie: CELLS.remove(x)
    for x in newGeneration: CELLS.add(x)
            
                
