import copy

def alpha_beta_pruning(state, depth, alpha, beta, maximizing_player, game_rules):
    """
    Thuật toán Alpha-Beta Pruning.

    Args:
        state: Trạng thái hiện tại của trò chơi.
        depth: Độ sâu tìm kiếm.
        alpha: Giá trị alpha.
        beta: Giá trị beta.
        maximizing_player: True nếu đang tìm kiếm cho người chơi tối đa, False nếu không.
        game_rules: Hàm xác định các nước đi hợp lệ và điểm số.

    Returns:
        Một tuple (điểm số, nước đi) nếu thành công, None nếu không có nước đi hợp lệ.
    """
    if depth == 0:
        return game_rules.evaluate(state), None

    if maximizing_player:
        value = float('-inf')
        best_move = None
        for move in game_rules.get_possible_moves(state):
            new_state = copy.deepcopy(state)
            game_rules.make_move(new_state, move)
            min_value, _ = alpha_beta_pruning(new_state, depth - 1, alpha, beta, False, game_rules)
            if min_value > value:
                value = min_value
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Cắt tỉa
        return value, best_move
    else:
        value = float('inf')
        best_move = None
        for move in game_rules.get_possible_moves(state):
            new_state = copy.deepcopy(state)
            game_rules.make_move(new_state, move)
            max_value, _ = alpha_beta_pruning(new_state, depth - 1, alpha, beta, True, game_rules)
            if max_value < value:
                value = max_value
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break  # Cắt tỉa
        return value, best_move


# Ví dụ sử dụng (Tic-Tac-Toe) - cần thay đổi logic cho trò chơi khác
class TicTacToeRules:
    def __init__(self):
        self.size = 3

    def get_possible_moves(self, state):
        moves = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    moves.append((i, j))
        return moves

    def make_move(self, state, move):
        row, col = move
        state[row][col] = 1

    def evaluate(self, state):
        # Kiểm tra thắng, thua hoặc hòa trong Tic-Tac-Toe
        for row in state:
            if row[0] == row[1] == row[2] != 0:
                return 1 if row[0] == 1 else -1
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col] != 0:
                return 1 if state[0][col] == 1 else -1
        if state[0][0] == state[1][1] == state[2][2] != 0:
            return 1 if state[0][0] == 1 else -1
        if state[0][2] == state[1][1] == state[2][0] != 0:
            return 1 if state[0][2] == 1 else -1
        # Nếu không thắng/thua, coi như hòa
        return 0


# Ví dụ sử dụng
state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_rules = TicTacToeRules()
best_move_score, best_move = alpha_beta_pruning(state,3, float('-inf'), float('inf'), True, game_rules)

if best_move:
    print("Nước đi tối ưu:", best_move)
    print("Điểm tối ưu:", best_move_score)
else:
    print("Không có nước đi hợp lệ.")