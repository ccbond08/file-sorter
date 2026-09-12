import os
import shutil
import time

path = os.path.join(os.path.expanduser('~'), 'Desktop', 'test_downloads')
categories = {
    '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    '文档': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    '压缩包': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '视频': ['.mp4', '.avi', '.mkv', '.mov'],
    '其他': []
}

for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    
    if os.path.isdir(file_path):
        continue
    
    if os.path.isfile(file_path):
        mod_time = os.path.getmtime(file_path)
        if time.time() - mod_time < 3600:
            continue
        date_str = time.strftime('%Y-%m-%d', time.localtime(mod_time))
        ext = os.path.splitext(filename)[1].lower()
        moved = False
        
        for folder_name, extensions in categories.items():
            if ext in extensions:
                target_folder = os.path.join(path, folder_name, date_str)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, target_folder)
                moved = True
                break
        
        if not moved:
            other_folder = os.path.join(path, '其他', date_str)
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, other_folder)

print("文件整理完成！")
input("按回车键退出...")
