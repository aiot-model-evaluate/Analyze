import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
print(PATH)

# python generate_result.py && python norm_all_param.py && python Radar_Chart.py && python Radar_Chart_combine.py && python new_Radar_Chart.py

os.system("E:/Anaconda/envs/torch_GPU/python.exe clear.py")
os.system("E:/Anaconda/envs/torch_GPU/python.exe generate_result.py")
os.system("E:/Anaconda/envs/torch_GPU/python.exe norm_all_param.py")
os.system("E:/Anaconda/envs/torch_GPU/python.exe new_Radar_Chart.py")
os.system("E:/Anaconda/envs/torch_GPU/python.exe new_Radar_Chart_combine.py")
os.system("E:/Anaconda/envs/torch_GPU/python.exe Bar_Chart.py")