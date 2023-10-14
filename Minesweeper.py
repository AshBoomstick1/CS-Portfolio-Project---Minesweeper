import random

num_of_bombs = 8
num_of_selected_bombs = 0

class Tile:
    def __init__(self, position_x, position_y, is_bomb = False, num_of_surrounding_bombs = 0):
        self.position_x = position_x
        self.position_y = position_y
        self.is_bomb = is_bomb
        self.num_of_surrounding_bombs = num_of_surrounding_bombs
    def __repr__(self):
        #return "This tile is at {x}, {y}.".format(x=self.position_x, y=self.position_y)
        bomb_count = 1
        if self.is_bomb == True:
            return "BOOM"
        else:
            for tile in surrounding_tiles[self]:
                if tile.is_bomb:
                    bomb_count += 1
            return str(bomb_count - 1)
    def select_bombs(self):
        if num_of_selected_bombs < 8:
            if random.randint(1, 100) < 30:
                self.is_bomb = True

tile1 = Tile(1, 1)
tile2 = Tile(1, 2)
tile3 = Tile(1, 3)
tile4 = Tile(1, 4)
tile5 = Tile(1, 5)
tile6 = Tile(2, 1)
tile7 = Tile(2, 2)
tile8 = Tile(2, 3)
tile9 = Tile(2, 4)
tile10 = Tile(2, 5)
tile11 = Tile(3, 1)
tile12 = Tile(3, 2)
tile13 = Tile(3, 3)
tile14 = Tile(3, 4)
tile15 = Tile(3, 5)
tile16 = Tile(4, 1)
tile17 = Tile(4, 2)
tile18 = Tile(4, 3)
tile19 = Tile(4, 4)
tile20 = Tile(4, 5)
tile21 = Tile(5, 1)
tile22 = Tile(5, 2)
tile23 = Tile(5, 3)
tile24 = Tile(5, 4)
tile25 = Tile(5, 5)

board = """
[1]: [{tile1}][{tile2}][{tile3}][{tile4}][{tile5}]
:[2]: [{tile6}][{tile7}][{tile8}][{tile9}][{tile10}]
:[3]: [{tile11}][tile12][{tile13}][{tile14}][{tile15}]
:[4]: [{tile16}][{tile17}][{tile18}][{tile19}][{tile20}]
:[5]: [{tile21}][{tile22}][{tile23}][{tile24}][{tile25}]
"""

tile_list = [
         tile1,tile2,tile3,tile4,tile5,
         tile6,tile7,tile8,tile9,tile10,
         tile11,tile12,tile13,tile14,tile15,
         tile16,tile17,tile18,tile19,tile20,
         tile21,tile22,tile23,tile24,tile25
        ]

surrounding_tiles = {tile1: [tile2, tile7, tile6], 
                     tile2: [tile1, tile3, tile6, tile7, tile8], 
                     tile3:[tile2, tile4, tile7, tile8, tile9], 
                     tile4: [tile3, tile5, tile8, tile9, tile10], 
                     tile5: [tile4, tile9, tile10], 
                     tile6: [tile1, tile2, tile7, tile11, tile12],
                     tile7: [tile1, tile2, tile3, tile6, tile8, tile11, tile12, tile13], 
                     tile8: [tile2, tile3, tile4, tile7, tile9, tile12, tile13, tile14], 
                     tile9: [tile3, tile4, tile5, tile8, tile10, tile13, tile14, tile15], 
                     tile10: [tile4, tile5, tile9, tile14, tile15], 
                     tile11: [tile6, tile7, tile12, tile16, tile17], 
                     tile12: [tile6, tile7, tile8, tile11, tile13, tile16, tile17, tile18], 
                     tile13: [tile7, tile8, tile9, tile12, tile14, tile17, tile18, tile19],
                     tile14: [tile8, tile9, tile10, tile13, tile15, tile18, tile19, tile20],
                     tile15: [tile9, tile10, tile14, tile19, tile20],
                     tile16: [tile11, tile12, tile17, tile21, tile22],
                     tile17: [tile11, tile12, tile13, tile16, tile18, tile21, tile22, tile23],
                     tile18: [tile12, tile13, tile14, tile17, tile18, tile22, tile23, tile24],
                     tile19: [tile13, tile14, tile15, tile18, tile20, tile23, tile24, tile25],
                     tile20: [tile14, tile15, tile19, tile24, tile25],
                     tile21: [tile16, tile17, tile22],
                     tile22: [tile16, tile17, tile18, tile21, tile23],
                     tile23: [tile17, tile18, tile19, tile22, tile24],
                     tile24: [tile18, tile19, tile20, tile23, tile25],
                     tile25: [tile19, tile20, tile24]}

for tile in tile_list:
    tile.select_bombs()
for tile in tile_list:
    if tile.is_bomb == True:
        print("BOOM" + ": " + str(tile_list.index(tile) + 1))
for tile in tile_list:
    if tile.is_bomb == True:
        print(str(tile.position_x) + ", " + str(tile.position_y) + "BOOM")
    else:
        print(str(tile) + ": " + str(tile_list.index(tile) + 1))

print(board)