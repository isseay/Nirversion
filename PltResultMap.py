# -*- coding: UTF-8 -*-

"""
    该文件是实现一个功能模块， 来讲由算法得出的结果进行可视化。
    可视化是把产地映射到地图中相应的省市，并进行高亮，
    运用matplotlib.Basemap模块，结合shapefile地理位置文件进行可视化

    @author : isseay
    @create on 2017/7/17
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


class PltReultMap:
    def __init__(self):
        """
        :构造函数
           构造sfigure、plt对象等
        """
        self.fig = plt.figure(figsize=(10,8))
        self.ax1 = self.fig.add_subplot(111)

        # 后面画图注的参数
        self.scatter_startx = 0.01
        self.scatter_starty = 0.04
        self.text_startx = 0.04
        self.text_starty = 0.03
        self.scatter_text_offset = 0.04

        # 调整子图边界
        plt.subplots_adjust(left=0.01, right=0.999, bottom=0.01, top=0.999)



    def CreateMapObject(self, lllon=70.33, lllat=10.01, urlon=138.16, urlat=56.123,
                        resolution='i', projection='merc', lat_0=42.5, lon_0=120, filloclor='#000000'):
        """
        创建Basemap对象
        drawmapboundary 是绘制背景颜色
        """
        self.map = Basemap(llcrnrlon=lllon, llcrnrlat=lllat, urcrnrlon=urlon,
                           urcrnrlat=urlat, resolution=resolution, projection=projection, lat_0=lat_0,
                           lon_0=lon_0, ax=self.ax1)
        self.map.drawmapboundary(fill_color=filloclor)
        self.map.fillcontinents(color='#000000', lake_color='c')


    def LoadShapeFile(self, filepath, drawbounds=True):
        """

        :param filepath: shapefile文件路径
        :param drawbounds:  bool变量
        :return: None

        加载shapefile地理位置信息文件
        """
        self.map.readshapefile(filepath, 'states',drawbounds=drawbounds)




    def LoadSahpeFileofTWN(self):
        self.map.readshapefile("./mapfile/TWN_adm_shp/TWN_adm0", 'states', drawbounds=True)



    def DrawCitys(self):
        """
        绘制省市的边界
        :return:
        """
        for info, shp in zip(self.map.states_info, self.map.states):
            poly = Polygon(shp, facecolor='#000000', edgecolor='c', lw=3)
            self.ax1.add_patch(poly)


    def LoadShapeFileOfCHN(self):
        """
         加载 中国 shapefile地理位置信息文件
        :return:
        """
        self.map.readshapefile("./mapfile/CHN_adm_shp/CHN_adm1", 'states', drawbounds=True)

    def DrawStateOnMap(self, states, colors):
        """
        :param state: 省市
        :param color: 颜色
        :return: None

        对特定城市进行高亮显示在地图上
        """
        le = len(colors)

        for info, shp in zip(self.map.states_info, self.map.states):
            proid = info['NAME_1']

            if proid in states:
                ci = states.index(proid)
                poly = Polygon(shp, facecolor=colors[ci], edgecolor='c', lw=3)
                #ci += 1
                self.ax1.add_patch(poly)
            else:
                poly = Polygon(shp, facecolor='#000000', edgecolor='c', lw=3)
                self.ax1.add_patch(poly)



    def DrawStatesOfResult(self, stateslist, colorlist):
        """

        :param stateslist: 城市列表
        :param colorlist:   颜色列表
        :return: NONE

         对几个城市进行在地图上的高亮
        """
        assert len(stateslist)==len(colorlist)
        colorindex = 0
        for sts, clr in zip(stateslist, colorlist):
            self.DrawStateOnMap(sts, clr)

    def DrawResultLegend(self, citys, probs, colors):
        """
        :param citys:  城市列表
        :param probs:  分类结果的概率
        :param colors:  颜色
        :return: None

        对分类结果进行文字和图例的描述

        这里有一个问题：
            在官方文档和网络资源上可以看到大部分直接上shapefile绘制的axes上进行scatter 和 text的绘制
            但经过在本机上这样做， scatter和 text函数失去功效， 不会显示。

        这是个悲伤的事情 - -！

        所以采用了内嵌图的方法进行绘制
        """
        assert len(citys)==len(probs)==len(colors)
        self.ax2 = plt.axes([0.05, 0.02, .3, .25],axisbg='none')
       # set(self.ax2,'Box','off')
        plt.xlim((0, 0.2))
        plt.ylim((0, 0.2))
        plt.xticks([])
        plt.yticks([])
        off_set = range(len(citys))
        for off,city,prob,color in zip(off_set, citys, probs, colors):
            txt = city+'  '+prob+'%'
            self.ax2.scatter(x=self.scatter_startx,y=self.scatter_starty+self.scatter_text_offset*off,
                            marker='s', s=300, facecolor=color, edgecolors='w')
            self.ax2.text(x=self.text_startx, y=self.text_starty+self.scatter_text_offset*off,
                          s=txt, color=color, fontsize=16)



    def ShowResult(self):
        """
        显示图像
        :return:
        """
        plt.show()



    def FastDraw(self,citys, probs, colors):
        """
        绘制可视化的快捷函数
        :param filepaths: shapefile文件
        :param citys:       城市列表
        :param probs:       分类置信度
        :param colors:      颜色列表
        :return:            None
        """
        self.CreateMapObject()
        self.LoadShapeFileOfCHN()
        self.DrawStateOnMap(citys, colors)
        self.LoadSahpeFileofTWN()
        self.DrawCitys()
        self.DrawResultLegend(citys, probs, colors)
        self.ShowResult()