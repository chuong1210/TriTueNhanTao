import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Chi phí từ nút gốc đến nút hiện tại
        self.h = h  # Chi phí ước tính từ nút hiện tại đến đích
        self.f = self.g + self.h  # Tổng chi phí ước tính

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.state == other.state


def a_star(start_state, goal_state, get_neighbors, heuristic):
    """
    Thuật toán A* tìm đường đi.

    Args:
        start_state: Trạng thái bắt đầu.
        goal_state: Trạng thái đích.
        get_neighbors: Hàm trả về các nút lân cận của một nút cho trước.
        heuristic: Hàm ước tính chi phí từ nút hiện tại đến nút đích.

    Returns:
        Đường đi từ `start_state` đến `goal_state` hoặc None nếu không tìm thấy.
    """
    open_set = [Node(start_state, g=0, h=heuristic(start_state, goal_state))]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        current_state = current_node.state

        if current_state == goal_state:
            path = []
            current = current_node
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]  # Đảo ngược để có đường đi đúng

        closed_set.add(current_state)

        for neighbor_state in get_neighbors(current_state):
            if neighbor_state in closed_set:
                continue
            g_score = current_node.g + 1  # Giả sử chi phí di chuyển là 1
            h_score = heuristic(neighbor_state, goal_state)
            neighbor = Node(neighbor_state, parent=current_node, g=g_score, h=h_score)

            # Kiểm tra xem nút láng giềng có trong open_set hay không và cập nhật
            in_open = False
            for open_node in open_set:
                if open_node.state == neighbor_state:
                    in_open = True
                    if g_score < open_node.g:
                        open_node.g = g_score
                        open_node.f = g_score + h_score
                        open_node.parent = current_node
                    break  
            if not in_open:
                heapq.heappush(open_set, neighbor)


    return None  # Không tìm thấy đường đi

# Ví dụ sử dụng (ví dụ tìm đường đi trên ma trận)
def get_neighbors(state):
    # Thay thế bằng logic lấy các trạng thái lân cận trong ma trận của bạn
    neighbors = []
    row, col = state
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 5 and 0 <= new_col < 5:  # Kiểm tra giới hạn ma trận
            neighbors.append((new_row, new_col))
    return neighbors

def heuristic(state, goal_state):
    row, col = state
    goal_row, goal_col = goal_state
    return abs(row - goal_row) + abs(col - goal_col)  # Heuristic Manhattan


start_state = (0, 0)
goal_state = (4, 4)
path = a_star(start_state, goal_state, get_neighbors, heuristic)

if path:
    print("Đường đi:", path)
else:
    print("Không tìm thấy đường đi.")