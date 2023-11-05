import random
import math
import datetime
#Sets of the game

def represents_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True
    
placing_flag = 2
tile_num = int(input("\nHow many tiles in the grid?: "))
while represents_int(tile_num) == False:
    tile_num = int(input("\nEnter an integer for the total number of tiles in the grid: "))
can_remove_flag = input("\nDo want to be able to remove flag? (y/n): ")
if can_remove_flag == "y":
    can_remove_flag = True
else:
    can_remove_flag = False
num_of_bombs = int(input("\nNumber of mines:")) + 1
while represents_int(num_of_bombs) == False:
    num_of_bombs = int(input("\nEnter an integer for the number of mines: ")) + 1
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
    def __init__(self, position_x, position_y, id, is_bomb = False, num_of_surrounding_bombs = 0, is_covered = True, is_flagged = False, is_checked = False):
        self.position_x = position_x
        self.position_y = position_y
        self.id = id
        self.is_bomb = is_bomb
        self.num_of_surrounding_bombs = num_of_surrounding_bombs
        self.is_covered = is_covered
        self.is_flagged = is_flagged
        self.is_checked = is_checked
    #This shows what the tiles will look like on the board
    def __repr__(self):
        #return_string = str(self.position_x) + ", " + str(self.position_y)
        #return return_string
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
                        return find_surrounding_bomb_for_tile(self)
                    else:
                        return "X"
                elif placing_flag == 2:
                    if can_remove_flag == True:
                        if self.is_flagged == True:
                            return "X"
                        else:
                            return find_surrounding_bomb_for_tile(self)
                    else:
                        return find_surrounding_bomb_for_tile(self)
                elif placing_flag == 3:
                    if self.is_flagged == False:
                        return find_surrounding_bomb_for_tile(self)
                    else:
                        return "X"
        else:
            return " "
    #This checks weather the tile is a bomb and flags as well as if you can remove flags.
    def uncover(self):
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
        else:
            input_flag = input("Add flag, remove flag, or uncover tile? (1 to uncover, 2 to flag, 3 to remove flag):")
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
                    print(print_board())
                    new_pick()

        turn += 1

        current_tile_if_bomb = self.is_bomb
        if self.is_bomb == True:
            if placing_flag == 1:         
                print("YOU LOSE: UNCOVERED MINE")
                end_game()
            elif placing_flag == 2:
                self.is_flagged = True
                self.is_covered = False
                print(print_board())
                new_pick()
            elif placing_flag == 3:
                self.is_flagged = False
                self.is_covered = True
                print(print_board())
                new_pick()
        else:
            if placing_flag == 1:
                self.is_covered = False
                if is_tile_0(self) == True:
                    find_surrounding_0s(self)

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
                   
            print(print_board())
            new_pick()

    def recover(self):
        self.is_covered = True

    def unflag(self):
        self.is_flagged = False

    def decover(self):
        self.is_covered = False

    #picks new bombs if your first tile was a bomb
    def pick_new_bomb(self):
        global bomb_list
        self.is_bomb = False
        bomb_list = []
        select_bombs(num_of_bombs)
    
    def check(self):
        self.is_checked == True

    def uncheck(self):
        self.is_checked = False

    def remove_mine(self):
        self.is_bomb = False

#finds the number the tile should be
def find_surrounding_bomb_for_tile(current_tile):
        bomb_count = 1
        for tile_pos in surrounding_tiles[str(tile_pos_dict[str(current_tile.id)][0])]:
            tile = tile_pos_dict[str(tile_pos)][1]
            if tile.is_bomb:
                bomb_count += 1
        return str(bomb_count - 1)

#ends the game
def end_game():
    print("Your Score is: " + str(uncovered_count + turn))
    print("Mines were at: ")
    for bomb in tile_list:
        if bomb.is_bomb == True:
            print(" " + str(bomb.position_y) + ", " + str(bomb.position_x))
    play_again()

#Finds the tiles around it that are 0, is used in the mass clearing of 0s

def find_surrounding_0s(tile):
    for tile_pos in find_tile_in_surrounding_tiles(tile):
        stile = tile_pos_dict[str(tile_pos)][1]
        if stile.is_checked == False:
            stile.is_checked = True
            stile.decover()
            if is_tile_0(stile):
                find_surrounding_0s(stile)

def find_tile_in_surrounding_tiles(tile):
    tile_id = tile.id
    stile = tile_pos_dict[tile_id][0]
    return surrounding_tiles[stile]
    
#checks is a tile is 0
def is_tile_0(tile):
    bomb_count = 0
    for tile1 in surrounding_tiles[str(tile_pos_dict[str(tile.id)][0])]:
        if tile_pos_dict[str(tile1)][1].is_bomb:
            bomb_count += 1
    if bomb_count == 0:
        return True
    else:
        return False
    

#finds all the suroundings tiles
def find_surounding_tiles(self):
    return_list = []
    for tile in surrounding_tiles[str(tile_pos_dict[str(self.id)][0])]:
        return_list.append(tile)
    return return_list

def cal_id(x, xd, y, yd):
    return str(x + xd) + str(y + yd)

#find the best pair of factors for the board aspect ratio
def find_factors(n):
    return_list = []
    #makes a list of factors
    for num in range(1, math.ceil(n/2) + 1):
        if num == 0:
            num += 1
        if n % num ==0:
            return_list.append(num)
    if len(return_list) == 1:
        return [1, 1]
    
    #makse a list of pairs of all the factors
    pair_list = []
    for num in return_list:
        if int(num) == 1:
            return_list.pop(return_list.index(num))
    for num in range(len(return_list)):
        if return_list[num] * return_list[num] == n:
            return [return_list[num], return_list[num]]
        if return_list[num] != return_list[-1]:
            pair_list.append([return_list[num], return_list[num + 1]])
    for num in range(len(return_list) - 1):
        if return_list[num] != return_list[-2] and return_list[num] != return_list[-1]:
            pair_list.append([return_list[num], return_list[num + 2]])


    num_removed = 0
    finished_list = [pair for pair in pair_list]

    #removes unnessicary items
    for pair in pair_list:

        if pair[0] * pair[1] != n:

            finished_list.pop(finished_list.index(pair))

            num_removed += 1

    difference_list = []
    #fills in the difference list which is a list of differences between each pair
    for pair in finished_list:
        difference_list.append(pair[1] - pair[0])
    #finds the smallest difference

    for difference in difference_list:
        for difference1 in difference_list:
            if difference > difference1:
                difference_list.pop(difference_list.index(difference))

    for pair in finished_list:
        if pair[1] - pair[0] == difference_list[0]:
            return pair
        
tile_dict = {}
tile_pos_dict = {}
remaining_dict = {}
def make_tiles(num_of_tiles):
    global row_count
    global col_count
    factor_list = find_factors(num_of_tiles)
    row_count = factor_list[0]
    col_count = factor_list[1]
    tile_num = 0
    for row in range(row_count):
        for col in range(col_count):
            tile_num += 1
            var_name = "tile" + str(tile_num)
            tile_dict[var_name] = Tile(row + 1, col + 1, cal_id(row + 1, 0, col + 1, 0))
            remaining_dict[var_name] = Tile(row + 1, col + 1, cal_id(row + 1, 0, col + 1, 0))
    for item in tile_dict:
        tile_pos_dict["{x}{y}".format(x=tile_dict[item].position_x, y=tile_dict[item].position_y)] = [item, tile_dict[item]]


make_tiles(tile_num)

surrounding_tiles = {}
def find_surrounding_tiles():
    for tile in tile_dict:
        x = tile_dict[tile].position_x
        y = tile_dict[tile].position_y
        nearby_tiles = []

        if y > 1:
            nearby_tiles.append(cal_id(x, 0, y, -1))
            if x < row_count:
                nearby_tiles.append(cal_id(x, 1, y, -1))
            if x > 1:
                nearby_tiles.append(cal_id(x, -1, y, -1))
        
        if x > 1:
            nearby_tiles.append(cal_id(x, -1, y, 0))
            if y < col_count:
                nearby_tiles.append(cal_id(x, -1, y, 1))

        if x < row_count:
            nearby_tiles.append(cal_id(x, 1, y, 0))
            if y < col_count:
                nearby_tiles.append(cal_id(x, 1, y, 1))
        
        if y < col_count:
            nearby_tiles.append(cal_id(x, 0, y, 1))
        surrounding_tiles[tile] = nearby_tiles

find_surrounding_tiles()
tile_list = [tile_dict[tile] for tile in tile_dict]
        
#selects bombs
def select_bombs(bomb_count):
    remaining_list = [tile_dict[tile] for tile in tile_dict]
    for bomb in range(1, bomb_count):
        new_bomb = int(random.randint(1, len(remaining_list)) - 1)
        tile_list[new_bomb].is_bomb = True
        remaining_list.pop(new_bomb)

select_bombs(num_of_bombs)

#def select_mines()
  

def print_board():
    def print_top_row():
        def print_0():
            start_list = ""
            for num in range(len(str(row_count)) - 1):
                start_list += (" ")
            start_list += (" 0   ")
            return start_list
        col_list = [str(num) for num in range(1, col_count + 1) ]
        new_list = []
        for num in col_list:
            if num == 1:
                new_list.append("  " + num + "  ")
            elif len(num) == 1:
                new_list.append(" " + num + "  ")
            elif len(num) == 2:
                new_list.append(num + "  ")
            elif len(num) == 3:
                new_list.append(num + " ")
            else:
                new_list.append(num)

        return_string = ""
        for item in new_list:
            return_string += item

        col_string = "\x1B[4m{return_s} \x1B[0m X \n".format(return_s=return_string)
        return print_0() + col_string
    
    print(print_top_row())
    for row in range(1, row_count + 1):
        def print_rows():
            return_string = ""
            if row < 10:
                    return_string += " "
            return_string += " {row} | ".format(row=row)
            for col in range(1, col_count + 1):
                i = cal_id(row, 0, col, 0)
                if row == row_count:
                    return_string += "\x1B[4m  {n} \x1B[0m".format(n=tile_pos_dict[i][1])
                else:
                    return_string += "  {n} ".format(n=tile_pos_dict[i][1])
            print(return_string + " |\n")
        print_rows()
    print(" Y\n\n\n\n")

#starts game
turn  += 1
x_input_list = [0]
y_input_list = [0]
def new_pick():
    global uncovered_count
    global turn
    uncovered_count = 0
    uncovered_tile_count = 0
    bomb_count = 0
    for tile in tile_list:
        if tile.is_covered == False:
            uncovered_count += 1
        if tile.is_bomb == True:
            bomb_count += 1
    for tile in tile_list:
        if tile.is_covered == False and tile.is_bomb == False:
            uncovered_tile_count += 1
    if uncovered_tile_count >= len(tile_dict) - bomb_count :
        end_time = datetime.datetime.now()
        global start_time
        time = str(end_time - start_time)
        time = time[2:7]
        print("YOU WIN!")
        print("YOU WON IN {time} with {turn} TURNS".format(time=time, turn=turn))
        play_again()
    else:

        input_cord_x = input("Enter the X cord of the tile you want to uncover: ")
        while represents_int(input_cord_x) == False:
            input_cord_x = input("Enter an integer between 0 and 6 as your X cord: ")
        if int(input_cord_x) > col_count:
            input_cord_x = input("Enter an integer between 0 and 6 as your X cord: ")

            

        x_input_list.append(input_cord_x)

        input_cord_y = input("Enter the Y cord of the tile you want to uncover: ")  
        while represents_int(input_cord_y) == False:
            input_cord_y = input("Enter an integer between 0 and 6 as your Y cord: ")
        if int(input_cord_y) > row_count:
            input_cord_y = input("Enter an integer between 0 and 6 as your Y cord: ")

        y_input_list.append(input_cord_y)

        for tile in tile_list:
            if tile.position_y == int(input_cord_x) and tile.position_x == int(input_cord_y):
                tile.uncover()

def play_again():
    redo = input("Play again? (y/n): ")
    if redo == "y":
        turn = 0
        for tile in tile_list:
            tile.recover()
            tile.unflag()
            tile.uncheck()
            tile.remove_mine()
        select_bombs(num_of_bombs - 1)
        print(print_board())
        start_time = datetime.datetime.now()
        new_pick()
    else:
        exit()

print(print_board())
start_time = datetime.datetime.now()
new_pick()