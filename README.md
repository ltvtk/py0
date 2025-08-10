## phần mềm LTweb và Vditor hỗ trợ học lập trình
## link tải https://github.com/ltvtk/py0/releases/tag/1.0
## Trên windows cần cài python,mingw c++ từ scoop như sau
### mở powershell quyền admin và chạy các lệnh sau lần lượt từng dòng
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
iex "& {$(irm get.scoop.sh)} -RunAsAdmin"
scoop install git-with-openssh
scoop install python
scoop install mingw
```
## C++ turtle graphic
### Bạn cần tải 2 file CImg.h và CTurtle.hpp xuống và bỏ chung thư mục với code c++ chính. 
### Sau đó mở VSCode chạy lệnh compile và run
```
g++ <file_name>.cpp -lgdi32;./a
```
