import random


print("***************************************")
print("****    Let's play tic-tac-toe!    ****")
print("***************************************")

class player:
    name = ""
    symbol = ''

players = [player(), player()]

'''
    Initialize players for testing
'''

players[0].name = 'Justin'
players[0].symbol = ' J'
players[1].name = 'Keili'
players[1].symbol = 'K '

row1 = ['A1', 'B1', 'C1']
row2 = ['A2', 'B2', 'C2']
row3 = ['A3', 'B3', 'C3']
board = [row1, row2, row3]

def print_board():
    print("     |    |     ")
    print("  "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]+"  ")
    print("_____|____|_____")
    print("     |    |     ")
    print("  "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]+"  ")
    print("_____|____|_____")
    print("     |    |     ")
    print("  "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+"  ")
    print("     |    |     ")

def setup():
    '''
        Setup - asks for player names and assigns to a list of players
    '''
    players[0].name = input("Player one, enter your name: ")
    players[0].symbol = " "+players[0].name[0]
    print("I've got your name as", players[0].name + ". Your symbol is", players[0].symbol + '.')

    players[1].name = input("Player two, enter your name: ")
    players[1].symbol = players[1].name[0]+" "
    print("I've got your name as", players[1].name + ". Your symbol is", players[1].symbol + '.')

    print("\nLet's Play!")

def check_victory():
    '''
        Checks to see if a player has won the game
    '''

    #Horizontal
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2]:
            return True

    #Vertical
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]:
            return True

    #Diagonal
    if board[0][0]==board[1][1]==board[2][2]:
        return True
    if board[2][0]==board[1][1]==board[0][2]:
        return True

    #Default
    return False



def main_loop():
    '''
        Main game loop - nine possible moves
    '''

    print_board()
    player_num = random.randint(0,1)
    for move in range(1,10):
        player_move = (input(players[player_num].name+", where would you like to place your token? ")).upper()
        legal = False

        for row in range(3):
            for cell in range(3):
                if board[row][cell] == player_move:
                    legal = True
                    board[row][cell] = players[player_num].symbol
        if legal:
            print_board()
        else:
            print("Not a legal move!")
            print("Quitting.")
            break

        if check_victory():
            print("Congratulations, "+players[player_num].name+"! You won!")
            break
        else:
            if move == 9:
                print("Cat got the game!")
            else:
                player_num = (player_num + 1) % 2



#setup()b2
main_loop()
