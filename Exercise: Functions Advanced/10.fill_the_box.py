from collections import deque


def fill_the_box(w, l, h, *cubes):
    space = w * l * h

    cubes = deque(cubes)
    while cubes[0] != 'Finish':
        if space >= cubes[0]:
            space -= cubes.popleft()
        else:
            cubes_left = sum(int(cube) for cube in cubes if cube != 'Finish')
            return f'No more free space! You have {cubes_left - space} more cubes.'

    return f'There is free space in the box. You could put {space} more cubes.'
