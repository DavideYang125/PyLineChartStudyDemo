from pylab import *
import json
import datetime
import mysql.connector
import pymysql
from cr_index_db import *
import decimal

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文

indexData = Read_database("SELECT * FROM `cryindex` where CreateTime >='2019-01-01' and CreateTime < '2020-10-17' ORDER BY CreateTime")

indexList = []
timeList = []
priceList = []
ptimeList = []

for i in indexData:
    indexList.append(i[1])
    timeList.append(i[0])


pData = Read_database("SELECT * FROM `b_price` where daytime >='2019-01-01' ORDER BY daytime")

for i in pData:
    price = decimal.Decimal(i[2])
    priceList.append(price/100)
    ptimeList.append(i[4])

# crIndexPath = r"D:\github\Demo\python\price_index\data_file\crindex.json"

print("index count:",len(indexList))
print("time count:",len(timeList))
print("price count:",len(priceList))


# with open(crIndexPath, 'r', encoding='utf8') as fp:
#     price_json_data = json.load(fp)

# price_json_data.sort(key = lambda x:x["CreateTime"])

# #json_array.sort(key = lambda x:x["time"])

# for i in price_json_data:
#     createTime = i["CreateTime"]
#     timeList.append(createTime)
#     indexNum = i["IndexNum"]
#     priceList.append(indexNum)

# plot中参数的含义分别是横轴值，纵轴值，线的形状，颜色，透明度,线的宽度和标签
plt.plot(timeList,
         indexList,
         'ro-',
         color='#4169E1',
         alpha=0.8,
         linewidth=1,
         label='I')

plt.plot(ptimeList,
         priceList,
         'ro-',
         color='#ff3300',
         alpha=0.8,
         linewidth=1,
         label='P')


# 显示标签，如果不加这句，即使在plot中加了label='一些数字'的参数，最终还是不会显示标签
plt.legend(loc="upper right")
plt.xlabel('x轴数字')
plt.ylabel('y轴数字')

plt.show()
# plt.savefig('demo.jpg')  # 保存该图片


class BPrice:
    createTime:datetime.datetime
    indexNum:int