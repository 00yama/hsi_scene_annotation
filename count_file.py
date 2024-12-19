import os

# 対象のディレクトリを指定
base_dir = "./yourpath"  # フォルダのパスを指定
indoor = 0
outdoor = 0
outdoor_keywords = ["roofgarden", "connecter", "around", "plaza", "outside"]
# サブフォルダを走査
for root, dirs, files in os.walk(base_dir):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)

        # 判定条件
        if "dendai" in dir_name:
            if any(keyword in dir_name for keyword in outdoor_keywords):
                outdoor += 1
                print(dir_name)
            else:
                indoor += 1
        else:
            outdoor += 1
        

# 結果を表示
print(f"Indoor:{indoor}")
print(f"Outdoor: {outdoor}")
