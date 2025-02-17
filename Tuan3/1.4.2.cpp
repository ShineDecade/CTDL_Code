#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    // Tạo một ngăn xếp lưu trữ các chuỗi
    stack<string> myStack;

    // Thêm các phần tử vào ngăn xếp
    myStack.push("Sách A");
    myStack.push("Sách B");
    myStack.push("Sách C");

    // Hiển thị phần tử ở đỉnh ngăn xếp
    cout << "Phần tử ở đỉnh ngăn xếp: " << myStack.top() << endl;

    // Lấy phần tử ở đỉnh ra khỏi ngăn xếp
    myStack.pop();
    cout << "Đã lấy phần tử ra khỏi ngăn xếp." << endl;

    // Hiển thị phần tử ở đỉnh ngăn xếp sau khi pop
    cout << "Phần tử ở đỉnh ngăn xếp sau khi pop: " << myStack.top() << endl;

    // Kiểm tra ngăn xếp có rỗng không
    if (myStack.empty()) {
        cout << "Ngăn xếp trống!" << endl;
    } else {
        cout << "Ngăn xếp không trống." << endl;
    }

    return 0;
}