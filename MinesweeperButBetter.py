import random

tile_list = [" " for tile in range(101)]

def print_board():
    print("   \x1B[4m1 2 3 4 5 6 7 8 9 10\x1B[0m")
    tile_count = 0
    for row in range(1, 11):
        return_string = ''
        for col in range(1, 11):
            tile_count += 1
            if tile_count in uncovered_list:
                tile_list[tile_count] = find_surrounding_tiles(tile_count)[0]
            return_string += tile_list[tile_count] + " "
        if row != 10:
            print(str(row) + " |" + str(return_string))
        else:
            print(str(row) + "|" + str(return_string))

bomb_list = []
remaining_list = [tile for tile in range(len(tile_list) - 1)]
def pick_bombs():
    for bomb in range(10):
        new_bomb_idx = remaining_list[random.randint(0, len(remaining_list) - 1)]
        bomb_list.append(new_bomb_idx)
        remaining_list.pop(remaining_list.index(new_bomb_idx))
pick_bombs()

def find_surrounding_tiles(tile):
    bomb_count = 0
    surrounding_list = []
    if tile == 1:
        if 2 in bomb_list: bomb_count += 1
        if 11 in bomb_list: bomb_count += 1
        if 12 in bomb_list: bomb_count += 1
        return [str(bomb_count), [2, 11, 12]]
    else:
     if tile > 10:
        if tile - 10 in bomb_list: 
            bomb_count += 1
        surrounding_list.append(tile - 10)
        if (tile - 1) % 10 != 0:
            if tile - 11 in bomb_list: 
                bomb_count += 1
            surrounding_list.append(tile - 11)
        if tile % 10 != 0:
            if tile - 9 in bomb_list: 
                bomb_count += 1
            surrounding_list.append(tile - 9)
     if tile % 10 != 0:
        if tile + 1 in bomb_list: 
            bomb_count += 1
        surrounding_list.append(tile + 1)
     if (tile - 1) % 10 != 0:
        if tile - 1 in bomb_list: 
            bomb_count += 1
        surrounding_list.append(tile - 1)
     if tile < 91:
        if (tile - 1) % 10 != 0:
            if tile + 9 in bomb_list:
                bomb_count += 1
            surrounding_list.append(tile +9)
        if tile + 10 in bomb_list: 
            bomb_count += 1
        surrounding_list.append(tile + 10)
        if tile % 10 != 0:
            if tile + 11 in bomb_list: 
                bomb_count += 1
            surrounding_list.append(tile + 11)
     return [str(bomb_count), surrounding_list]
        
def find_zero_field(tile):
    for other_tile in find_surrounding_tiles(tile)[1]:
        if other_tile not in uncovered_list:
            uncovered_list.append(other_tile)
            if int(find_surrounding_tiles(other_tile)[0]) == 0:
                find_zero_field(other_tile)

uncovered_list = []
flagged_list = []
print_board()
turn = 0
while len(uncovered_list) <= 90:
    turn += 1
    cords = input("Enter the cords of the tiles you want to uncover (x, y): ")
    x = int(cords[:2])
    y = int(cords[-2:])    
    uncovered_tile = (y - 1)* 10 + (x)
    if uncovered_tile in bomb_list:
        print("YOU LOSE")
        exit()
    if int(find_surrounding_tiles(uncovered_tile)[0]) == 0: find_zero_field(uncovered_tile)
    uncovered_list.append(uncovered_tile)
    print_board()
print("YOU WIN")