from collections import deque

def max_sliding_window(num_list, k):
    if not num_list or k == 0:
        return []
    
    result = []
    deque_index = deque()
    
    for i in range(len(num_list)):
        # Loại bỏ các phần tử không thuộc cửa sổ hiện tại
        if deque_index and deque_index[0] < i - k + 1:
            deque_index.popleft()
        
        # Loại bỏ các phần tử nhỏ hơn phần tử hiện tại từ phía cuối deque
        while deque_index and num_list[deque_index[-1]] < num_list[i]:
            deque_index.pop()
        
        # Thêm chỉ mục của phần tử hiện tại vào deque
        deque_index.append(i)
        
        # Bắt đầu thêm giá trị vào kết quả khi cửa sổ có đủ k phần tử
        if i >= k - 1:
            result.append(num_list[deque_index[0]])
    
    return result

# Ví dụ sử dụng
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_sliding_window(num_list, k))
