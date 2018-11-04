# _*_ coding: utf-8 _*_
__author__ = 'xbr'
__date__ = '2018/10/30 22:44'

'''
GADL输出矢量图shp文件的前10个要素
'''
import sys

from osgeo import ogr

# 矢量图shp文件
fn = r'D:\osgeopy-data\global\ne_50m_populated_places.shp'
# 打开文件
ds = ogr.Open(fn, 0)
# 如果文件为空，则报错
if ds is None:
    sys.exit('Could not open {0}.'.format(fn))
# 在确保打开文件后，从数据源中检索第一个图层
lyr = ds.GetLayer(0)
# 下面for循环是获取图层中前10个要素，
# 每个要素所含字段：城市名、最大人口数、经度、纬度
i = 0
for feat in lyr:
    pt = feat.geometry()
    x = pt.GetX()   # 经度
    y = pt.GetY()   # 纬度
    name = feat.GetField('NAME')   # 城市名
    pop = feat.GetField('POP_MAX') # 最大人口数
    print(name, pop, x, y)
    i += 1
    if i == 10:
        break
# 删除ds变量以强制文件关闭
del ds