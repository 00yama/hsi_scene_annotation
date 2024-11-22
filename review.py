import json

def modify_json(input_file, output_file):
    """
    JSONファイルを読み込み、指定された形式に変換して新しいファイルに保存する。
    
    :param input_file: 入力JSONファイルのパス
    :param output_file: 出力JSONファイルのパス
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for item in data:
        # data_nameからplaceを抽出
        data_name = item.get("data_name", "")
        if "static/images/" in data_name:
            parts = data_name.split("/")
            if len(parts) > 3:
                item["place"] = parts[3]  # ディレクトリ名をplaceに設定
        
        # statusフィールドを追加
        item["status"] = "not review"
    
    # 結果を新しいJSONファイルに保存
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

# 使用例
input_file = "data.json"  # 入力ファイル
output_file = "data_scene_modified.json"  # 出力ファイル
modify_json(input_file, output_file)
