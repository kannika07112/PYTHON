# Program 5: Tic Tac Toe game (2 players)

board = [" "]*9

def print_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-+-+-")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-+-+-")
    print(board[6]+"|"+board[7]+"|"+board[8])

def check_winner(sign):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==sign for a,b,c in wins)

turn = "X"
for _ in range(9):
    print_board()
    pos = int(input(f"Enter position (0-8) for {turn}: "))
    if board[pos] == " ":
        board[pos] = turn
        if check_winner(turn):
            print_board()
            print(turn, "wins!")
            break
        turn = "O" if turn == "X" else "X"
else:
    print("It's a draw!")
