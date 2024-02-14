

def get_coordinates_from_grid(position, tile_size, offsets = (0, 0)):
    x, y = position
    x_offset, y_offset = offsets
    return x * tile_size + x_offset, y * tile_size + y_offset   