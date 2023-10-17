import random

placing_flag = 2
can_remove_flag = input("\nDo want to be able to remove flag? (y/n): ")
if can_remove_flag == "y":
    can_remove_flag = True
else:
    can_remove_flag = False
num_of_bombs = int(input("\nNumber of mines:"))
if can_remove_flag == True:
    num_of_bombs += 1
turn = -1
current_tile_x = 6
current_tile_y = 6
previous_x = 0
previous_y = 0
global uncover_0_count
uncover_0_count = 0
class Tile:
    def __init__(self, position_x, position_y, is_bomb = False, num_of_surrounding_bombs = 0, is_covered = True, is_flagged = False):
        self.position_x = position_x
        self.position_y = position_y
        self.is_bomb = is_bomb
        self.num_of_surrounding_bombs = num_of_surrounding_bombs
        self.is_covered = is_covered
        self.is_flagged = is_flagged
    def __repr__(self):
        global placing_flag
        global current_tile_x
        global current_tile_y
        global current_tile_if_bomb
        if self.is_covered == False:
            if self.is_bomb == True:
                return "X"           
            else:
                if placing_flag == 1:
                    if self.is_flagged == False:
                        return self.find_surrounding_bomb_for_tile()
                    else:
                        return "X"
                elif placing_flag == 2:
                    if can_remove_flag == True:
                        if self.is_flagged == True:
                            return "X"
                        else:
                            return self.find_surrounding_bomb_for_tile()
                    else:
                        return self.find_surrounding_bomb_for_tile()
                elif placing_flag == 3:
                    if self.is_flagged == False:
                        return self.find_surrounding_bomb_for_tile()
                    else:
                        return "X"
        else:
            return " "
        
    def uncover(self):
        global uncovered_count
        global turn
        global current_tile_x
        global current_tile_y 
        global current_tile_if_bomb
        global un_cover_again
        global current_tile
        un_cover_again = True
        current_tile = str(self.position_y) + str(self.position_x)
        current_tile_x = self.position_x
        current_tile_y = self.position_y
        while turn == 0 and self.is_bomb == True and un_cover_again == True:
            print("SELECTING NEW BOMBS")
            self.pick_new_bomb()
        un_cover_again = False

        if int(x_input_list[-2]) == int(current_tile_x) and int(y_input_list[-2]) == int(current_tile_y):
            turn -= 1
        turn += 1

        if can_remove_flag == False:
            input_flag = input("Add flag or uncover tile? (1 to uncover, 2 to flag):")
            while type(input_flag) != str or input_flag == "":
                input_flag = input("Type 1 to uncover tile. Type 2 to place flag:")
        else:
            input_flag = input("Add flag, remove flag, or uncover tile? (1 to uncover, 2 to flag, 3 to remove flag):")
            while type(input_flag) != str or input_flag == "":
                input_flag = input("Type 1 to uncover tile. Type 2 to place flag. Type 3 to remove flag:")
        if int(input_flag) == 2:
            global placing_flag
            placing_flag = 2
        elif int(input_flag) == 3:
            placing_flag = 3
        else:
            placing_flag = 1

        current_tile_if_bomb = self.is_bomb
        if self.is_bomb == True:
            if placing_flag == 1:         
                print("YOU LOSE: UNCOVERED MINE")
                print("Your Score is: " + str(uncovered_count + turn))
                for tile in tile_list:
                    if tile.is_bomb == True:
                        print("Mines were at: " + str(tile.position_y) + ", " + str(tile.position_x))
                exit()
            elif placing_flag == 2:
                self.is_flagged = True
                self.is_covered = False
                print(show_board())
                new_pick()
            elif placing_flag == 3:
                self.is_flagged = False
                self.is_covered = True
                print(show_board())
                new_pick()
        else:
            if placing_flag == 1:
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
                                                if is_tile_0(tile4):
                                                    surrounding_tiles_list_5 = find_surounding_tiles(tile4)
                                                    for tile5 in surrounding_tiles_list_5:
                                                        tile5.is_covered = False
                                                        if is_tile_0(tile5):
                                                            surrounding_tiles_list_6 = find_surounding_tiles(tile5)
                                                            for tile6 in surrounding_tiles_list_6:
                                                                tile6.is_covered = False
                                                                if is_tile_0(tile6):
                                                                    surrounding_tiles_list_7 = find_surounding_tiles(tile6)
                                                                    for tile7 in surrounding_tiles_list_7:
                                                                        tile7.is_covered = False
                                                                        if is_tile_0(tile7):
                                                                            surrounding_tiles_list_8 = find_surounding_tiles(tile7)
                                                                            for tile8 in surrounding_tiles_list_8:
                                                                                tile8.is_covered = False
                                                                                if is_tile_0(tile8):
                                                                                    surrounding_tiles_list_9 = find_surounding_tiles(tile8)
                                                                                    for tile9 in surrounding_tiles_list_9:
                                                                                        tile9.is_covered = False
                                                                                        if is_tile_0(tile9):
                                                                                            surrounding_tiles_list_10 = find_surounding_tiles(tile9)
                                                                                            for tile10 in surrounding_tiles_list_10:
                                                                                                tile10.is_covered = False

            elif placing_flag == 2:
                if can_remove_flag == True:
                    self.is_covered = False
                    self.is_flagged = True
                else:
                    print("YOU LOSE: FLAGGED CLEAR TILE")
                    print("Your Score is: " + str(uncovered_count + turn))
                    for tile in tile_list:
                        if tile.is_bomb == True:
                            print("Mines were at: " + str(tile.position_y) + ", " + str(tile.position_x))
                    exit()
            elif placing_flag == 3:
                self.is_flagged = False
                self.is_covered = True
                   
            print(show_board())
            new_pick()

    def pick_new_bomb(self):
        print("IT PICKING")
        global bomb_list
        self.is_bomb = False
        bomb_list = []
        select_turn_mines()

    def find_surrounding_bomb_for_tile(self):
        bomb_count = 1
        for tile in surrounding_tiles[self]:
            if tile.is_bomb:
                bomb_count += 1
        return str(bomb_count - 1)

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

def uncover_0_field(tile):
    global uncover_0_count
    print(uncover_0_count)
    uncover_0_count += 1
    return_list = []
    surrounding_tiles_list = find_surounding_tiles(tile)
    for tile in surrounding_tiles_list:
        tile.is_covered = False
        if is_tile_0(tile):
            return_list.append(tile)
    if uncover_0_count < 12:
        for tile1 in return_list:
            uncover_0_field(tile1)
    else:
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
bomb_list = []
def select_turn_mines():
    global bomb_list
    while len(bomb_list) <= num_of_bombs:
        new_bomb = tile_list[random.randint(0, 24)]
        bomb_list.append(tile_list.index(new_bomb) + 1)
        for bomb in bomb_list:
            if tile_list.index(new_bomb) + 1 != bomb:
                new_bomb.is_bomb = True

select_turn_mines()

def show_board():
    board = """
Turn: {turn}
 0  1  2  3  4  5 (X)
 1 [{tile1}][{tile2}][{tile3}][{tile4}][{tile5}]
 2 [{tile6}][{tile7}][{tile8}][{tile9}][{tile10}]
 3 [{tile11}][{tile12}][{tile13}][{tile14}][{tile15}]
 4 [{tile16}][{tile17}][{tile18}][{tile19}][{tile20}]
 5 [{tile21}][{tile22}][{tile23}][{tile24}][{tile25}]
(Y)
""".format(turn=turn,
  tile1=tile1,
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

turn  += 1
x_input_list = [0]
y_input_list = [0]
def new_pick():
    global uncovered_count
    global turn
    uncovered_count = 0
    uncovered_tile_count = 0
    for tile in tile_list:
        if tile.is_covered == False:
            uncovered_count += 1
    for tile in tile_list:
        if tile.is_covered == False and tile.is_bomb == False:
            uncovered_tile_count += 1
    if uncovered_count == 25 or uncovered_tile_count == 25 - num_of_bombs:
        print("YOU WIN!")
        print("YOU WON IN {turn} TURNS".format(turn=turn))
    else:

        input_cord_x = input("Enter the X cord of the tile you want to uncover: ")
        while type(input_cord_x) != str or input_cord_x == "" or int(input_cord_x) < 1 or int(input_cord_x) > 5:
            input_cord_x = input("Enter a number between 0 and 6 as your X cord: ") 

        x_input_list.append(input_cord_x)

        input_cord_y = input("Enter the Y cord of the tile you want to uncover: ")  
        while input_cord_y == "" or int(input_cord_y) < 1 or int(input_cord_y) > 5:
            input_cord_y = input("Enter a number between 0 and 6 as your Y cord: ")

        y_input_list.append(input_cord_y)

        for tile in tile_list:
            if tile.position_y == int(input_cord_x) and tile.position_x == int(input_cord_y):
                tile.uncover()


print(show_board())
new_pick()