def dfs(graph, start):
  """Thực hiện thuật toán DFS trên đồ thị bắt đầu từ đỉnh 'start'

  Args:
    graph: Một dictionary biểu diễn đồ thị
    start: Đỉnh bắt đầu
  """

  stack = [start]
  visited = set()

  while stack:
    vertex = stack.pop()  # Lấy đỉnh trên cùng ra khỏi stack

    if vertex not in visited:
      visited.add(vertex)
      print(vertex, end=' ')

      # Thêm các nút kề chưa thăm vào stack (đảo ngược để duyệt theo thứ tự)
      neighbors = reversed(graph[vertex])
      stack.extend(neighbors)

# Ví dụ minh họa
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

print("DFS từ nút A:")
dfs(graph, 'A')  # Output: A C F B E D