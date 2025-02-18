def count_chars(string):
    char_count = {}  # Khởi tạo dictionary để lưu số lần xuất hiện của từng ký tự
    for char in string:  
        if char in char_count:  
            char_count[char] += 1  # Tăng giá trị nếu ký tự đã tồn tại
        else:
            char_count[char] = 1  # Thêm ký tự mới vào dictionary
    return char_count

# Ví dụ chạy thử
string1 = "Happiness"
string2 = "smiles"

print(count_chars(string1))  # {'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
print(count_chars(string2))  # {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}