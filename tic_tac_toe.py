print("**********************************")
print("Let's play tic-tac-toe!")
print("**********************************")

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
        Setup - asks for player names and assigns to a dictionary of players
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
        Victory - declares a winner
    '''

def check_legal(move):
    legal = False
    for row in range(3):
        for cell in range(3):
            if board[row][cell] == move:
                legal = True
    return legal

def main_loop():
    '''
        Main game loop - nine possible moves
    '''

    print_board()
    player_num = 0
    for move in range(1,5):
        player_move = input(players[player_num].name+", where would you like to place your token? ")

        if check_legal(player_move):
            for row in range(3):
                for cell in range(3):
                    if board[row][cell] == player_move:
                        board[row][cell] = players[player_num].symbol
                        print_board()
        else:
            print("Not a legal move!")
            print("Quitting.")
            break

        if check_victory():
            print("Congratulations, "+players[player_num].name+"! You won!")
            break
        else:
            player_num = (player_num + 1) % 2





#setup()
main_loop()
