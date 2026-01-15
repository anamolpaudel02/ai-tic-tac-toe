from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [' ' for _ in range(9)]

def check_winner(b):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] != ' ':
            return b[combo[0]]
    if ' ' not in b:
        return 'Draw'
    return None

def minimax(b, is_ai_turn):
    result = check_winner(b)
    if result == 'O': return 1
    if result == 'X': return -1
    if result == 'Draw': return 0

    if is_ai_turn:
        best_score = -float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = 'O'

@app.route('/')
def index():
    return render_template('index.html', board=board)

@app.route('/move', methods=['POST'])
def move():
    global board
    data = request.json
    index = data['index']
    if board[index] == ' ':
        board[index] = 'X'
        winner = check_winner(board)
        if winner is None:
            ai_move()
            winner = check_winner(board)
        return jsonify({'board': board, 'winner': winner})
    return jsonify({'board': board, 'winner': None})

@app.route('/reset')
def reset():
    global board
    board = [' ' for _ in range(9)]
    return jsonify({'board': board})

if __name__ == '__main__':
    app.run(debug=True)
