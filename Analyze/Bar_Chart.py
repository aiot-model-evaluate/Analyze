import os
import pandas as pd
from matplotlib import pyplot as plt


class Bar_Chart:
    def __init__(self, csv_file_path, save_path, choice):
        # 存储训练和推理的 DataFrame
        self.csv_file_path = csv_file_path
        self.save_path = save_path
        self.choice = choice
        self.param = ""
        self.csv_file_list = self.load_files(self.csv_file_path)
        
    # 获取所有归一化之后的csv文件
    def load_files(self, csv_file_path):
        csv_file_list = []
        root = os.path.abspath(csv_file_path)
        # 比较训练/推理的吞吐量
        if self.choice == 0:
            csv_file_list.append(os.path.join(root, "infer_throughput.csv"))
            csv_file_list.append(os.path.join(root, "train_throughput.csv"))
            self.param = "Throughput"
        # 比较平均前向推理时延
        elif self.choice == 1:
            csv_file_list.append(os.path.join(root, "infer_average_inference_delay.csv"))
            self.param = "Average Inference Delay"
        # 比较训练/推理的能效比
        elif self.choice == 2:
            csv_file_list.append(os.path.join(root, "infer_energy_efficiency.csv"))
            csv_file_list.append(os.path.join(root, "train_energy_efficiency.csv"))
            self.param = "Energy Efficiency"
        return csv_file_list

    def draw_bar_chart(self):
        FontSize = 16
        for csv_file in self.csv_file_list:
            # 读取数据
            pd_data = pd.read_csv(csv_file, index_col=0)
            
            # 删除 4090 所在的列
            pd_data = pd_data.drop("4090", axis=1)

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
                
                # 设置 y 轴数字为白色字体
                plt.rcParams['ytick.color'] = 'white'
                
                # 设置整个方形边框为白色
                plt.gca().spines['top'].set_color('white')
                plt.gca().spines['bottom'].set_color('white')
                plt.gca().spines['left'].set_color('white')
                plt.gca().spines['right'].set_color('white')
                
                # 绘制柱状图，制定宽度和颜色
                plt.bar(x_labels, y_values, width=0.5, color='skyblue')
                plt.title(f"{model_name} - {mode.capitalize()} "+self.param, fontsize=FontSize, color='white')
                plt.xlabel("Devices", fontsize=FontSize, color='white')
                plt.ylabel(self.param, fontsize=FontSize, color='white')
                plt.xticks(rotation=45, ha="right", fontsize=FontSize, color='white')
                plt.tight_layout()

                # 保存图表
                save_file = os.path.join(mode_save_path, self.param, f"{model_name}_{mode}_" + self.param + ".png")
                # 如果路径不存在则创建路径
                if not os.path.exists(os.path.join(mode_save_path, self.param)):
                    os.makedirs(os.path.join(mode_save_path, self.param))
                
                plt.savefig(save_file, dpi=300, bbox_inches='tight', transparent=True)
                plt.close()


if __name__ == '__main__':
    csv_file_path = ".\\..\\Table"
    save_path = ".\\..\\Diagram\\Bar_Chart"
    for i in range(0, 3):
        tool = Bar_Chart(csv_file_path=csv_file_path, save_path=save_path, choice=i)
        tool.draw_bar_chart()

