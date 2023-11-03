import random
#Sets of the game
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
#defines the tiles
class Tile:
    def __init__(self, position_x, position_y, is_bomb = False, num_of_surrounding_bombs = 0, is_covered = True, is_flagged = False):
        self.position_x = position_x
        self.position_y = position_y
        self.is_bomb = is_bomb
        self.num_of_surrounding_bombs = num_of_surrounding_bombs
        self.is_covered = is_covered
        self.is_flagged = is_flagged
    #This shows what the tiles will look like on the board
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
    #This checks weather the tile is a bomb and flags as well as if you can remove flags.
    def uncover(self):
        print("YYWEG")
        global uncovered_count
        global turn
        global current_tile_x
        global current_tile_y 
        global current_tile_if_bomb
        global un_cover_again
        global tile_id
        un_cover_again = True
        tile_id = str(self.position_y) + str(self.position_x)
        current_tile_x = self.position_x
        current_tile_y = self.position_y
        while turn == 0 and self.is_bomb == True and un_cover_again == True:
            self.pick_new_bomb()
        un_cover_again = False

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

        for tile in tile_list:
            if tile.is_covered == False:
                if tile.position_x == current_tile_x and tile.position_y == current_tile_y:
                    print(show_board())
                    new_pick()

        turn += 1

        current_tile_if_bomb = self.is_bomb
        if self.is_bomb == True:
            print("BOMB")
            if placing_flag == 1:         
                print("YOU LOSE: UNCOVERED MINE")
                end_game()
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
                    find_surrounding_0s(self, 6)

            elif placing_flag == 2:
                if can_remove_flag == True:
                    self.is_covered = False
                    self.is_flagged = True
                else:
                    print("YOU LOSE: FLAGGED CLEAR TILE")
                    end_game()
            elif placing_flag == 3:
                self.is_flagged = False
                self.is_covered = True
                   
            print(show_board())
            new_pick()
    #picks new bombs if your first tile was a bomb
    def pick_new_bomb(self):
        global bomb_list
        self.is_bomb = False
        bomb_list = []
        select_bombs(num_of_bombs, tile_list)

    #finds the number the tile should be
    def find_surrounding_bomb_for_tile(self):
        bomb_count = 1
        for tile in surrounding_tiles[self]:
            if tile.is_bomb:
                bomb_count += 1
        return str(bomb_count - 1)
#ends the game
def end_game():
    print("Your Score is: " + str(uncovered_count + turn))
    for bomb in tile_list:
        if bomb.is_bomb == True:
            print("Mines were at: " + str(bomb.position_y) + ", " + str(bomb.position_x))
    print(bomb_list)
    exit()

#Finds the tiles around it that are 0, is used in the mass clearing of 0s
def find_surrounding_0s(tile, i):
    if i != 0:
        surounding_tiles = find_surounding_tiles(tile)
        for tile1 in surounding_tiles:
            tile1.is_covered = False
            if is_tile_0(tile1) == True:
                find_surrounding_0s(tile1, i-1)
    
#checks is a tile is 0
def is_tile_0(tile):
    bomb_count = 0
    for tile in surrounding_tiles[tile]:
        if tile.is_bomb:
            bomb_count += 1
    if bomb_count == 0:
        return True
    else:
        return False

#finds all the suroundings tiles
def find_surounding_tiles(self):
    return_list = []
    for tile in surrounding_tiles[self]:
        return_list.append(tile)
    return return_list

#does the mass clearing of 0s
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

#sets of the tiles cords
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


#the list of all tiles
tile_list = [
         tile1,tile2,tile3,tile4,tile5,
         tile6,tile7,tile8,tile9,tile10,
         tile11,tile12,tile13,tile14,tile15,
         tile16,tile17,tile18,tile19,tile20,
         tile21,tile22,tile23,tile24,tile25
        ]

#a dict with all surounding tiles
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
for tile in tile_list:
    if tile.is_bomb == True:
        bomb_list.append(tile)
#selects bombs
def select_bombs(bomb_count, tlist):
    if bomb_count != 0:
        new_bomb = tlist[random.randint(0, 24)]
        if new_bomb.is_bomb == True:
            select_bombs(bomb_count, tlist)
        else:
            new_bomb.is_bomb = True
            select_bombs(bomb_count - 1, tlist)
select_bombs(num_of_bombs, tile_list)

#board
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
#starts game
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