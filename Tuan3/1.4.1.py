class Stack:
    """
    Lớp Stack (ngăn xếp) sử dụng danh sách để lưu trữ các phần tử.
    Các phương thức chính:
    - is_empty: Kiểm tra xem ngăn xếp có rỗng hay không.
    - size: Trả về kích thước của ngăn xếp.
    - display: Hiển thị các phần tử trong ngăn xếp theo thứ tự từ đỉnh đến đáy.
    - push: Thêm một phần tử vào đỉnh của ngăn xếp.
    - pop: Xóa và trả về phần tử ở đỉnh của ngăn xếp.
    - peek: Trả về phần tử ở đỉnh của ngăn xếp mà không xóa.
    """

    def __init__(self):
        """Khởi tạo một ngăn xếp rỗng."""
        self.elements = []

    def is_empty(self):
        """Kiểm tra xem ngăn xếp có rỗng hay không."""
        return len(self.elements) == 0

    def size(self):
        """Trả về kích thước của ngăn xếp."""
        return len(self.elements)

    def display(self):
        """Hiển thị các phần tử trong ngăn xếp theo thứ tự từ đỉnh đến đáy."""
        print("Ngăn xếp (đỉnh đến đáy):", self.elements[::-1])

    def push(self, item):
        """Thêm một phần tử vào đỉnh của ngăn xếp."""
        self.elements.append(item)
        print(f"Đã thêm '{item}' vào ngăn xếp.")

    def pop(self):
        """Xóa và trả về phần tử ở đỉnh của ngăn xếp."""
        if not self.is_empty():
            item = self.elements.pop()
            print(f"Đã lấy '{item}' ra khỏi ngăn xếp.")
            return item
        else:
            print("Ngăn xếp trống!")
            return None

    def peek(self):
        """Trả về phần tử ở đỉnh của ngăn xếp mà không xóa."""
        if not self.is_empty():
            return self.elements[-1]
        else:
            print("Ngăn xếp trống!")
            return None

# Minh họa sử dụng ngăn xếp
if __name__ == "__main__":
    stack = Stack()

    stack.push("Sách A")
    stack.push("Sách B")
    stack.push("Sách C")

    stack.display()  # Output: Ngăn xếp (đỉnh đến đáy): ['Sách C', 'Sách B', 'Sách A']

    top_item = stack.peek()
    print("Phần tử ở đỉnh ngăn xếp:", top_item)  # Output: Sách C

    stack.pop()

    stack.display()  # Output: Ngăn xếp (đỉnh đến đáy): ['Sách B', 'Sách A']

    print("Ngăn xếp có trống không?", stack.is_empty())  # Output: False