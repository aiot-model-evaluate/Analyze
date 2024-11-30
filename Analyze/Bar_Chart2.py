import os
import pandas as pd
from matplotlib import pyplot as plt


class Bar_Chart:
    def __init__(self, csv_file_path, save_path):
        # 存储训练和推理的 DataFrame
        self.csv_file_path = csv_file_path
        self.save_path = save_path
        self.csv_file_list = self.load_files(self.csv_file_path)

    # 获取所有归一化之后的csv文件
    def load_files(self, csv_file_path):
        csv_file_list = []
        root = os.path.abspath(csv_file_path)
        csv_file_list.append(os.path.join(root, "infer_throughput.csv"))
        csv_file_list.append(os.path.join(root, "train_throughput.csv"))
        return csv_file_list

    def draw_bar_chart(self):
        for csv_file in self.csv_file_list:
            # 读取数据
            pd_data = pd.read_csv(csv_file, index_col=0)

            # 获取模式（infer 或 train）
            filename = os.path.basename(csv_file).split(".")[0]
            mode = filename.split("_")[0]

            # 创建对应模式的保存路径
            mode_save_path = os.path.join(self.save_path, mode)
            if not os.path.exists(mode_save_path):
                os.makedirs(mode_save_path)

            # 对每一行生成柱状图
            for model_name, row in pd_data.iterrows():
                x_labels = row.index  # 列标签作为柱状图的X轴标签
                y_values = row.values  # 数据值作为柱状图的高度

                plt.figure(figsize=(10, 6))
                bars = plt.bar(x_labels, y_values, color='skyblue')

                # 在柱子上标记数值
                for bar in bars:
                    height = bar.get_height()
                    plt.text(
                        bar.get_x() + bar.get_width() / 2,  # X 坐标为柱子中心
                        height,                            # Y 坐标为柱子高度
                        f'{height:.2f}',                  # 格式化数值为两位小数
                        ha='center', va='bottom', fontsize=9
                    )

                plt.title(f"{model_name} - {mode.capitalize()} Throughput")
                plt.xlabel("Devices")
                plt.ylabel("Throughput")
                plt.xticks(rotation=45, ha="right")
                plt.tight_layout()

                # 保存图表
                save_file = os.path.join(mode_save_path, f"{model_name}_{mode}_bar_chart.png")
                plt.savefig(save_file)
                plt.close()


if __name__ == '__main__':
    csv_file_path = ".\\..\\Table"
    save_path = ".\\..\\Diagram\\Bar_Chart"
    tool = Bar_Chart(csv_file_path=csv_file_path, save_path=save_path)
    tool.draw_bar_chart()
