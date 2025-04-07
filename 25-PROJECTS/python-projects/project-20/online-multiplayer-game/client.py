import socket

def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))  # Connect to server

    # Receive player symbol (X or O)
    player = client.recv(1024).decode()
    print(f"You are Player {player}")

    while True:
        # Receive updated board from server
        board_data = client.recv(1024).decode()
        if "wins" in board_data or "draw" in board_data:
            print(board_data)
            break

        board = board_data.split(",")
        display_board(board)

        if " " in board:
            # Prompt for move
            move = input("Enter your move (0-8): ")
            client.send(move.encode())

if __name__ == "__main__":
    start_client()