

def are_colliding(a, b):
    ax, ay = a
    bx, by = b
     
    if ay != by:
        return False

    return ax >= by - 0.5 and ax <= bx + 0.5