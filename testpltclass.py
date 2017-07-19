#   -*- coding: UTF-8 -*-

import PltResultMap as PRM

list_citys=['Guangdong', 'Sichuan','Shanxi']
list_probs=['78.32', '24.78','92.54']
list_colors=['#E066FF', 'g', 'c']

CHN_PATH = "./mapfile/CHN_adm_shp/CHN_adm1"
TWN_PATH = "./mapfile/TWN_adm_shp/TWN_adm0"
list_file=[CHN_PATH,TWN_PATH]

prm = PRM.PltReultMap()
prm.FastDraw(list_citys, list_probs, list_colors)