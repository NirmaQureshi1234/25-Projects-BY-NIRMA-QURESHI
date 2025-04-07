import socket
import threading

# Game state
board = [" " for _ in range(9)]  # 3x3 Tic-Tac-Toe board
current_player = "X"
clients = []
lock = threading.Lock()

def handle_client(client_socket, player):
    global current_player
    while True:
        try:
            # Receive move from client
            move = client_socket.recv(1024).decode()
            if not move:
                break

            # Update game state
            with lock:
                if board[int(move)] == " " and current_player == player:
                    board[int(move)] = player
                    current_player = "O" if player == "X" else "X"

            # Send updated board to both clients
            for c in clients:
                c.send(f"{','.join(board)}".encode())

            # Check for win or draw
            if check_win(board):
                for c in clients:
                    c.send(f"Player {player} wins!".encode())
                break
            elif " " not in board:
                for c in clients:
                    c.send("It's a draw!".encode())
                break

        except Exception as e:
            print(f"Error: {e}")
            break

    # Close connection
    client_socket.close()
    clients.remove(client_socket)

def check_win(board):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True
    return False

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))  # Bind to all interfaces on port 5555
    server.listen(2)
    print("Server started. Waiting for players...")

    while len(clients) < 2:
        client_socket, addr = server.accept()
        print(f"Player {len(clients) + 1} connected from {addr}")
        clients.append(client_socket)

        # Assign player symbol (X or O)
        player = "X" if len(clients) == 1 else "O"
        client_socket.send(player.encode())

        # Start a thread to handle the client
        threading.Thread(target=handle_client, args=(client_socket, player)).start()

if __name__ == "__main__":
    start_server()