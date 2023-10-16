import random

placing_flag = False
num_of_bombs = 4
turn = 0
class Tile:
    def __init__(self, position_x, position_y, is_bomb = False, num_of_surrounding_bombs = 0, is_covered = True, is_flagged = False):
        self.position_x = position_x
        self.position_y = position_y
        self.is_bomb = is_bomb
        self.num_of_surrounding_bombs = num_of_surrounding_bombs
        self.is_covered = is_covered
        self.is_flagged = is_flagged
    def __repr__(self):
        bomb_count = 1
        global placing_flag
        global current_tile_x
        global current_tile_y
        global current_tile_if_bomb
        if self.is_covered == False:
            if self.is_bomb == True:
                if placing_flag == True:
                    self.is_flagged = True
                    return "X"
                else:
                    if current_tile_if_bomb == self.is_bomb:
                        print(self.position_x, self.position_y)
                        print("YOU LOSE: UNCOVERED MINE")
                        print("Your Score is: " + str(uncovered_count - 1))
                        for tile in tile_list:
                            if tile.is_bomb == True:
                                print("Mines were at: " + str(tile.position_y) + ", " + str(tile.position_x))
                        exit()
                    else:
                        return "X"
            else:
                if placing_flag == False:
                    for tile in surrounding_tiles[self]:
                        if tile.is_bomb:
                            bomb_count += 1
                    return str(bomb_count - 1)
                else:
                    if self.position_x == current_tile_x and self.position_y == current_tile_y and self.is_bomb == True:
                        print(str(self.is_bomb), str(self.position_x), str(self.position_y))
                        print("YOU LOSE: FLAGGED CLEAR TILE")
                        print("Your Score is: " + str(uncovered_count))
                        for tile in tile_list:
                            if tile.is_bomb == True:
                                print("Mines were at: " + str(tile.position_y) + ", " + str(tile.position_x))
                        exit()
                    else:
                        for tile in surrounding_tiles[self]:
                            if tile.is_bomb:
                                bomb_count += 1
                        return str(bomb_count - 1)

        else:
            return " "
        
    def uncover(self):
        global uncovered_count
        global turn
        turn += 1
        input_flag = input("Add flag or uncover tile? (1 for tile, 0 for flag):")
        while type(input_flag) != str:
            input_flag = input("Type 1 to uncover tile. Type 2 to place flag:")
        if int(input_flag) == 1:
            global placing_flag
            placing_flag = False
        else:
            placing_flag = True
        global current_tile_x
        global current_tile_y
        global current_tile_if_bomb
        current_tile_x = self.position_x
        current_tile_y = self.position_y
        current_tile_if_bomb = self.is_bomb
        if self.is_bomb == True:
            if placing_flag == False:          
                print("YOU LOSE: UNCOVERED MINE")
                print("Your Score is: " + str(uncovered_count ))
                for tile in tile_list:
                    if tile.is_bomb == True:
                        print("Mines were at: " + str(tile.position_y) + ", " + str(tile.position_x))
            if placing_flag == True:
                self.is_covered = False
                print(show_board())
                new_pick()
        else:
            self.is_covered = False
            if is_tile_0(self) == True:
                surrounding_tiles_list = find_surounding_tiles(self)
                for tile in surrounding_tiles_list:
                    tile.is_covered = False
                    if is_tile_0(tile):
                        surrounding_tiles_list_2 = find_surounding_tiles(tile)
                        for tile2 in surrounding_tiles_list_2:
                            tile2.is_covered = False
                            if is_tile_0(tile2):
                                surrounding_tiles_list_3 = find_surounding_tiles(tile2)
                                for tile3 in surrounding_tiles_list_3:
                                    tile3.is_covered = False
                                    if is_tile_0(tile3):
                                        surrounding_tiles_list_4 = find_surounding_tiles(tile3)
                                        for tile4 in surrounding_tiles_list_4:
                                            tile4.is_covered = False
            print(show_board())
            new_pick()


def is_tile_0(tile):
    bomb_count = 0
    for tile in surrounding_tiles[tile]:
        if tile.is_bomb:
            bomb_count += 1
    if bomb_count == 0:
        return True
    else:
        return False

def find_surounding_tiles(self):
    return_list = []
    for tile in surrounding_tiles[self]:
        return_list.append(tile)
    return return_list



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
                     tile18: [tile12, tile13, tile14, tile17, tile19, tile22, tile23, tile24],
                     tile19: [tile13, tile14, tile15, tile18, tile20, tile23, tile24, tile25],
                     tile20: [tile14, tile15, tile19, tile24, tile25],
                     tile21: [tile16, tile17, tile22],
                     tile22: [tile16, tile17, tile18, tile21, tile23],
                     tile23: [tile17, tile18, tile19, tile22, tile24],
                     tile24: [tile18, tile19, tile20, tile23, tile25],
                     tile25: [tile19, tile20, tile24]}
def select_turn_mines():
    global selected_bomb_count
    selected_bomb_count = 0
    def select_bomb():
        new_bomb = tile_list[random.randint(0, 24)]
        if new_bomb.is_bomb == True:
            global selected_bomb_count
            selected_bomb_count = selected_bomb_count - 1
        new_bomb.is_bomb = True

    while selected_bomb_count < num_of_bombs:
        select_bomb()
        selected_bomb_count += 1
select_turn_mines()
def show_board():
    board = """
 0  1  2  3  4  5 (X)
 1 [{tile1}][{tile2}][{tile3}][{tile4}][{tile5}]
 2 [{tile6}][{tile7}][{tile8}][{tile9}][{tile10}]
 3 [{tile11}][{tile12}][{tile13}][{tile14}][{tile15}]
 4 [{tile16}][{tile17}][{tile18}][{tile19}][{tile20}]
 5 [{tile21}][{tile22}][{tile23}][{tile24}][{tile25}]
(Y)
""".format(tile1=tile1,
  tile2=tile2, 
  tile3=tile3,
  tile4=tile4,
  tile5=tile5,
  tile6=tile6,
  tile7=tile7, 
  tile8=tile8,
  tile9=tile9,
  tile10=tile10,
  tile11=tile11,
  tile12=tile12,
  tile13=tile13,
  tile14=tile14,
  tile15=tile15,
  tile16=tile16,
  tile17=tile17,
  tile18=tile18,
  tile19=tile19,
  tile20=tile20,
  tile21=tile21,
  tile22=tile22,
  tile23=tile23,
  tile24=tile24,
  tile25=tile25)
    return board


def new_pick():
    global uncovered_count
    global turn
    uncovered_count = 0
    for tile in tile_list:
        if tile.is_covered == False:
            uncovered_count += 1
    if uncovered_count == 25:
        print("YOU WIN!")
        print("YOU WON IN {turn} TURNS".format(turn=turn))
    else:
        input_cord_x = input("Enter the X cord of the tile you want to uncover: ")
        while type(input_cord_x) != str or input_cord_x == "" or int(input_cord_x) < 0 or int(input_cord_x) > 5:
            input_cord_x = input("Enter a number between 0 and 6 as your X cord: ") 
        input_cord_y = input("Enter the Y cord of the tile you want to uncover: ")  
        while input_cord_y == "" or int(input_cord_y) < 0 or int(input_cord_y) > 5:
            input_cord_y = input("Enter a number between 0 and 6 as your Y cord: ")
        for tile in tile_list:
            if tile.position_y == int(input_cord_x) and tile.position_x == int(input_cord_y):
                tile.uncover()



print(show_board())
new_pick()