import os
import glob
import shutil

path = ""
# if using wsl
# username = ""
# path = f"/mnt/c/Users/{username}_/Pictures/VRChat"

files = os.listdir(path)

files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]

for dir in files_dir:
    path_month = os.path.join(path, dir)

    for day in range(1, 32):
        day = str(day).zfill(2)

        files_in_a_day = glob.glob(os.path.join(path_month, f"*{dir}-{day}*.png"))
        
        if len(files_in_a_day) > 0:
            if not os.path.isdir(os.path.join(path_month, f"{dir}-{day}")):
                os.mkdir(os.path.join(path_month, f"{dir}-{day}"))

        for file in files_in_a_day:
            shutil.move(os.path.join(path_month, file), os.path.join(path_month, f"{dir}-{day}"))
