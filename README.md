# CS112.L12.KHCL

# Mục lục
- [Thành viên](#thành-viên)
- [Tiến độ bài tập](#tiến-độ-bài-tập)
- [Hướng dẫn sử dụng test_tool.py](#hướng-dẫn-dùng-test_tool)
    - [Cú pháp](#cú-pháp)
    - [Format file input](#format-của-file-test-input)
    - [Format file output](#format-của-file-test-output)

# Thành viên
| Họ và Tên           | MSSV     |
| ------------------- | -------- |
| Nguyễn Trường Thịnh | 18521447 |
| Trần Hoàng Sơn      | 18521351 |
| Lê Anh Triều        | 18521536 |
# Tiến độ bài tập
- [ ] [Bài tập 1 BOT](https://github.com/18521447/CS112.L12.KHCL/tree/master/bt1)
# Hướng dẫn dùng test_tool
## Cú pháp
```
python test_tool.py [file python cần test] [file test input] [file test output]
```
Ví dụ:
```
python test_tool.py bt1/brute_force.py bt1/tests_input.txt bt1/tests_output.txt
```
![kết quả](https://i.imgur.com/2CyhGxC.png)
## Format của file test input
1. Dòng 1 chứa số lượng test
2. Dòng 2 chứa số dòng input của mỗi test case
3. Dòng 3 chứa số dòng output của mỗi test case
2. Các dòng tiếp theo là input của từng test
## Format của file test output
1. Output của từng test (output của mỗi test có thể nằm trên nhiều dòng)
2. Cuối file phải chứa đúng 1 kí tự xuống dòng
