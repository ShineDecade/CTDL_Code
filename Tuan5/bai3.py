def word_count(file_path):
    # Khởi tạo một dictionary để đếm số lần xuất hiện của các từ
    word_counts = {}
    
    # Mở file và đọc nội dung
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Chia dòng thành các từ
            words = line.split()
            for word in words:
                # Chuyển từ về chữ thường
                word = word.lower()
                # Đếm số lần xuất hiện của từ
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
                    
    return word_counts

# Gọi hàm với đường dẫn đến file txt
result = word_count('P1_data.txt')  # Đường dẫn đến file txt
print(result)