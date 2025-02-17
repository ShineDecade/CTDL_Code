#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Stack {
private:
    vector<string> elements; // Sử dụng vector để lưu trữ các phần tử

public:
    // Thêm một phần tử vào đỉnh của ngăn xếp
    void push(const string& item) {
        elements.push_back(item);
        cout << "Đã thêm '" << item << "' vào ngăn xếp." << endl;
    }

    // Loại bỏ và trả về phần tử ở đỉnh của ngăn xếp
    string pop() {
        if (!isEmpty()) {
            string item = elements.back();
            elements.pop_back();
            cout << "Đã lấy '" << item << "' ra khỏi ngăn xếp." << endl;
            return item;
        } else {
            cout << "Ngăn xếp trống!" << endl;
            return ""; // Trả về một chuỗi rỗng khi ngăn xếp trống
        }
    }

    // Lấy phần tử ở đỉnh của ngăn xếp (không xóa)
    string peek() const {
        if (!isEmpty()) {
            return elements.back();
        } else {
            throw out_of_range("Ngăn xếp trống!");
        }
    }

    // Kiểm tra xem ngăn xếp có rỗng hay không
    bool isEmpty() const {
        return elements.empty();
    }

    // Trả về kích thước của ngăn xếp
    int size() const {
        return elements.size();
    }

    // Hiển thị tất cả các phần tử trong ngăn xếp
    void display() const {
        cout << "Ngăn xếp (đỉnh đến đáy): ";
        for (auto it = elements.rbegin(); it != elements.rend(); ++it) {
            cout << *it << " ";
        }
        cout << endl;
    }
};

int main() {
    Stack myStack;

    myStack.push("Sách A");
    myStack.push("Sách B");
    myStack.push("Sách C");

    myStack.display(); // Output: Ngăn xếp (đỉnh đến đáy): Sách C Sách B Sách A

    try {
        cout << "Phần tử ở đỉnh ngăn xếp: " << myStack.peek() << endl; // Output: Sách C
    } catch (const out_of_range& e) {
        cout << e.what() << endl;
    }

    myStack.pop();
    myStack.display(); // Output: Ngăn xếp (đỉnh đến đáy): Sách B Sách A

    cout << "Ngăn xếp có trống không? " << (myStack.isEmpty() ? "Có" : "Không") << endl; // Output: Không

    return 0;
}