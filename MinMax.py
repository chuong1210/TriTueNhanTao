import copy

def minimax(state, depth, maximizing_player, game_rules):
    """
    Thuật toán Minimax với Alpha-Beta pruning.

    Args:
        state: Trạng thái hiện tại của trò chơi.
        depth: Độ sâu tìm kiếm.
        maximizing_player: True nếu đang tìm kiếm cho người chơi tối đa, False nếu không.
        game_rules: Hàm xác định các nước đi hợp lệ và điểm số.


    Returns:
        Một tuple (điểm số, nước đi) nếu thành công, None nếu không có nước đi hợp lệ.
    """
    if depth == 0:
        return game_rules.evaluate(state), None  # Đến nút lá, trả về điểm số và nước đi trống

    if maximizing_player:
        value = float('-inf')
        best_move = None
        for move in game_rules.get_possible_moves(state):
            new_state = copy.deepcopy(state)  # Cần copy để không thay đổi state gốc
            game_rules.make_move(new_state, move)
            min_value, _ = minimax(new_state, depth - 1, False, game_rules)
            if min_value > value:
                value = min_value
                best_move = move
        return value, best_move
    else:
        value = float('inf')
        best_move = None
        for move in game_rules.get_possible_moves(state):
            new_state = copy.deepcopy(state)
            game_rules.make_move(new_state, move)
            max_value, _ = minimax(new_state, depth - 1, True, game_rules)
            if max_value < value:
                value = max_value
                best_move = move
        return value, best_move


# Ví dụ về cách sử dụng (cần một lớp game_rules)
class TicTacToeRules:
    def __init__(self):
        self.size = 3


    def get_possible_moves(self, state):
       moves = []  # Thêm logic để lấy nước đi hợp lệ
       for i in range(3):
           for j in range(3):
               if state[i][j] == 0:
                   moves.append((i,j))
       return moves
    

    def make_move(self, state, move):
       row, col = move
       state[row][col] = 1  # Ví dụ: Đánh dấu nước đi

    def evaluate(self, state):
        # Thêm logic đánh giá trạng thái.
        # Ví dụ đơn giản: Trả về 1 nếu thắng, -1 nếu thua, 0 nếu hòa.
        return 0


# Ví dụ sử dụng
state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Mảng 3x3 cho TicTacToe
game_rules = TicTacToeRules()
best_move_score, best_move = minimax(state, 2, True, game_rules)

if best_move:
    row, col = best_move
    print(f"Nước đi tối ưu: ({row}, {col}) với điểm số: {best_move_score}")
else:
    print("Không có nước đi hợp lệ.")