import matplotlib.pyplot as plt
import pandas as pd
import math
import random

data = pd.read_csv("sensor_data_600.txt",delimiter=" ",header=None,
                   names=("date","time","ir","lidar"))
index = "lidar"

#ヒストグラムを描く
#data[index].hist(bins=(data[index].max() - data[index].min()),color="orange",align="left")

#データの並び通りにプロット
#data[index].plot()

#各時間ごとにデータをまとめる
data["hour"] = [e//10000 for e in data["time"]]
d = data.groupby("hour")

#d[index]の各時刻の平均値を描く
#d[index].mean().plot()
#d[index]の値が高いところと低いところのhistグラムを色別で描く。
#pd.concat([d[index].get_group(7),d[index].get_group(6),d[index].get_group(5)]).hist() # P(z | 5,6,7時)
#pd.concat([d[index].get_group(13),d[index].get_group(14),d[index].get_group(15)]).hist() # P(z | 13,14,15時)

each_hour = {i:d[index].get_group(i).value_counts().sort_index() for i in range(24)}
freqs = pd.concat(each_hour,axis=1)
freqs = freqs.fillna(0)
print (freqs.sort_index(ascending=True)/len(data))

plt.show()
