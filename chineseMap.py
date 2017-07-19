
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(111)#fig.add_axes([0.01,0.1,0.95,0.95])
plt.subplots_adjust(left=0.01,right=0.999, bottom=0.01,top=0.999)
map = Basemap(llcrnrlon=70.33,
              llcrnrlat=10.01,
              urcrnrlon=138.16,
              urcrnrlat=56.123,
             resolution='i', projection='merc', lat_0 = 42.5,lon_0=120,ax=ax1)
m.fillcontinents(color='#191919',lake_color='#000000') # dark grey land, black lakes
map.drawmapboundary(fill_color='#000000')                # black background
#m.drawcountries(linewidth=2, color="w")              # thin white line for country borders
#map.fillcontinents(color='#000000',zorder=0)
shp_info_twn = map.readshapefile("./mapfile/TWN_adm_shp/TWN_adm0",'states',drawbounds=True)
for info, shp in zip(map.states_info, map.states):
    poly = Polygon(shp,  facecolor='#000000',edgecolor='c', lw=3)
    ax1.add_patch(poly)


shp_info_chn = map.readshapefile("./mapfile/CHN_adm_shp/CHN_adm1",'states',drawbounds=True)
for info, shp in zip(map.states_info, map.states):
    proid = info['NAME_1']
    if proid == 'Guangdong':
        poly = Polygon(shp,facecolor='g',edgecolor='c', lw=3)
        ax1.add_patch(poly)
    elif proid == 'Shanxi':
        poly = Polygon(shp, facecolor='#E066FF', edgecolor='c', lw=3)
        ax1.add_patch(poly)
    else:
        poly = Polygon(shp,  facecolor='#000000',edgecolor='c', lw=3)
        ax1.add_patch(poly)

#plt.scatter(x=500,y=60,s=200, marker='o', facecolor='#E066FF', edgecolor='w')




ax = plt.axes([0.05, 0.02, .3, .25],axisbg='#000000')
plt.xlim((0,0.2))
plt.ylim((0,0.2))
plt.xticks([])
plt.yticks([])
ax.scatter(x=0.01,y=0.04,marker='s',s=300,facecolor='g', edgecolors='w')
ax.text(0.04, 0.03, 'Guangzhou 89.783%', color='g', fontsize=16)
ax.scatter(x=0.01,y=0.08,marker='s',s=300,facecolor='#E066FF', edgecolors='w')
ax.text(0.04, 0.07, 'Sichuan 19.283%', color='#E066FF', fontsize=16)
ax.scatter(x=0.01,y=0.12,marker='s',s=300,facecolor='c', edgecolors='w')
ax.text(0.04, 0.11, 'Shanxi 39.813%', color='c', fontsize=16)



#000000
#map.drawcoastlines()

plt.show()
