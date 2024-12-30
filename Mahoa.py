import base64
import os
from time import sleep
import requests
import concurrent.futures
import time
import os
from pystyle import Colors, Colorate
import nguyenthanhngoc
from nguyenthanhngoc import *
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')
Write.Print("""
                                                                    
                         ,--.                                  ,--. 
   ,---,               ,--.'|            ,---,               ,--.'| 
  '  .' \          ,--,:  : |           '  .' \          ,--,:  : | 
 /  ;    '.     ,`--.'`|  ' :          /  ;    '.     ,`--.'`|  ' : 
:  :       \    |   :  :  | |         :  :       \    |   :  :  | | 
:  |   /\   \   :   |   \ | :         :  |   /\   \   :   |   \ | : 
|  :  ' ;.   :  |   : '  '; |         |  :  ' ;.   :  |   : '  '; | 
|  |  ;/  \   \ '   ' ;.    ;         |  |  ;/  \   \ '   ' ;.    ; 
'  :  | \  \ ,' |   | | \   |         '  :  | \  \ ,' |   | | \   | 
|  |  '  '--'   '   : |  ; .'         |  |  '  '--'   '   : |  ; .' 
|  :  :         |   | '`--'           |  :  :         |   | '`--'   
|  | ,'         '   : |               |  | ,'         '   : |       
`--''           ;   |.'               `--''           ;   |.'       
                '---'                                 '---'         
    ╔══════════════════════════════════════════════════════╗
    ║     Data Encryption     | Develop by: AnAn           ║
    ╚══════════════════════════════════════════════════════╝                                                                    
    \n""",Colors.blue, interval=0.0009)
  
input_dir = "FileCanMaHoa"
output_dir = "FileDaDuocMaHoa"
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


file_name = input(Colorate.Diagonal(Colors.purple_to_blue,f"Nhập tên tệp cần mã hóa : "))
file_path = os.path.join(input_dir, file_name)


if not os.path.isfile(file_path):
 print(Colorate.Diagonal(Colors.purple_to_blue,f"Tệp {file_name} không tồn tại trong thư mục {input_dir}. "))
 exit()
with open(file_path, 'rb') as file:
    file_content = file.read()

encoded_content = base64.b64encode(file_content)

encoded_file_path = os.path.join(output_dir, 'encoded_file.txt')
with open(encoded_file_path, 'wb') as encoded_file:
    encoded_file.write(encoded_content)

print(Colorate.Diagonal(Colors.purple_to_blue,"Tệp đã được mã hóa thành công!"))
sleep(2)

try:
    # 
    with open(encoded_file_path, 'rb') as file:
        encoded_content = file.read()

    # Tạo nội dung Python để lưu vào tệp enc.py
    python_code = f"""import base64

# Nội dung mã hóa
encoded_content = {repr(encoded_content.decode('utf-8'))}

# Giải mã và thực thi nội dung
decoded_content = base64.b64decode(encoded_content.encode('utf-8'))
exec(decoded_content.decode('utf-8'))"""


    python_file_path = os.path.join(output_dir, file_name)
    with open(python_file_path, 'w') as python_file:
        python_file.write(python_code)

    print(Colorate.Diagonal(Colors.purple_to_blue, f"file mã hóa đã được lưu trong thư mục FileDaDuocMaHoa!"))
except Exception as e:
    print(Colorate.Diagonal(Colors.red_to_white,f"Đã xảy ra lỗi: {e}"))
