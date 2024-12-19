import json
import matplotlib.pyplot as plt
def count_indoor_outdoor(json_files):
    """
    JSONファイル群を処理してindoorとoutdoorの数をカウントする。

    :param json_files: 処理するJSONファイルのリスト
    :return: indoorとoutdoorのカウント結果
    """
    indoor_count = 0
    outdoor_count = 0
    
    # dendai関連 outdoor判定に使うキーワード
    outdoor_keywords = ["roofgarden", "connecter", "around", "plaza","outside"]

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for item in data:
                data_name = item.get("data_name", "")
                
                if "dendai" in data_name:
                    # dendai を含む場合
                    if any(keyword in data_name for keyword in outdoor_keywords):
                        outdoor_count += 1
                    else:
                        indoor_count += 1
                else:
                    # dendai を含まない場合
                    outdoor_count += 1
    
    return indoor_count, outdoor_count

def plot_pie_chart(indoor_count, outdoor_count):
    """
    indoorとoutdoorのカウントを円グラフとして表示する。

    :param indoor_count: indoorのカウント数
    :param outdoor_count: outdoorのカウント数
    """
    labels = ['Indoor', 'Outdoor']
    counts = [indoor_count, outdoor_count]
    colors = ['#66b3ff', '#99ff99']  # 色のカスタマイズ
    explode = (0.1, 0)  # Outdoorを少し強調表示

    # ラベルに割合とカウント数を追加
    total = sum(counts)
    label_with_counts = [
        f'{label}\n{count} ({count / total:.1%})'
        for label, count in zip(labels, counts)
    ]

    plt.figure(figsize=(6, 6))
    # plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
    plt.pie(
        counts, labels=label_with_counts, autopct=None, startangle=90,
        colors=colors, explode=explode
    )
    # plt.title('Count location')
    plt.show()


# 実行例
json_files = ["data.json"]  # 処理対象のJSONファイルリスト
indoor, outdoor = count_indoor_outdoor(json_files)

print(f"Indoor count: {indoor}")
print(f"Outdoor count: {outdoor}")
plot_pie_chart(indoor, outdoor)