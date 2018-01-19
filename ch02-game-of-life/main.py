import curses
import life

GEN = 0

def usage(argc, argv):
    print("Usage: %s <path-to-initial-state-file>" % argv[0] )

def read_initial_state(filename):
    f = open(filename, "r")
    for s in f:
        x, y = (int(z) for z in s.split())
        assert(x < life.WIDTH)
        assert(x >= 0)
        assert(y < life.HEIGHT)
        assert(y >= 0)
        life.CELLS.add((x,y))
    f.close()

def render_board(screen):
    screen.clear()
    for (x,y) in life.CELLS:
        assert ((x >= 0) and (x < life.WIDTH))
        assert ((y >= 0) and (y < life.HEIGHT))
        try:
            screen.addstr(y, x, "o")
        except:
            raise Exception(str((y+1, x)))
        screen.addstr(23, 0, "GEN:"+str(GEN))
    screen.refresh()

def main(argv):
    global GEN
    read_initial_state(argv[1])
    mscreen = curses.initscr()
    try:
        while True:
            render_board(mscreen)
            life.calculate_generation()
            GEN += 1
            
            #if (0 == len(life.CELLS)):
            #    break
            if ("q" == mscreen.getch()) or (0 == len(life.CELLS)):
                break
    except KeyboardInterrupt:
        pass
    except:
        print(life.CELLS)
        raise
    finally:
        curses.endwin()

    
if "__main__" == __name__:
    import sys
    if (len(sys.argv) < 2):
        usage(sys.argv)
        sys.exit(0)
    main(sys.argv)
