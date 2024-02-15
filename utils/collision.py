

def are_colliding(a, b):
    ax, ay, *_ = a
    bx, by, *_ = b
     
    if ay != by:
        return False

    return ax >= by - 0.5 and ax <= bx + 0.5