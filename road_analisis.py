import json
import pandas as pd
import geojson
import geopandas as gpd
from jsonpath import jsonpath

#先注释掉了
#路口划分,后续算法检验,l,u,r,d
juction={'路口1':[41,12,44,13,-1,1],
         '路口2':[43,37,31,48,-1,2],
        '路口3':[30,40,25,38,-1,3],
        '路口4':[24,34,27,35,-1,4],
        '路口5':[28,14,16,-1,-1,5],
        '路口6':[15,47,18,-1,-1,6],
        '路口7':[17,39,20,1,2,7],
        '路口8':[19,45,22,3,4,8]}
#路口人行道匹配
juction_walk={'路口1':[87,88,89,90,1],
         '路口2':[173,174,175,176,2],
        '路口3':[121,122,123,124,3],
        '路口4':[135,136,137,138,4],
        '路口5':[71,93,94,0,5],
        '路口6':[95,96,97,98,6],
        '路口7':[99,100,101,0,7],
        '路口8':[102,103,104,0,8]}
#路口停车线处理
junction_stop={
        '路口1':[2001,2019,2014,2012,1],
        '路口2':[67,66,62,63,2],
        '路口3':[1,4,2,2134,3],
        '路口4':[25,24,20,23,4],
        '路口5':[2136,2028,2005,-1,5],
        '路口6':[2006,2072,2007,-1,6],
        '路口7':[2132,2133,2020,-1,7],
        '路口8':[2021,2071,2022,218,8]
}
road_juc=pd.DataFrame(juction)
road_juc=road_juc.T
#road_juc_walk=pd.DataFrame(juction_walk)
#road_juc_walk=road_juc_walk.T
#print(road_juc)
#road_stop=pd.DataFrame(junction_stop)
#road_stop=road_stop.T
# 读取 GeoJSON 文件
#data = gpd.read_file('dataRec/road2-12-9road/laneroad_with9road.geojson')
#data_walk=gpd.read_file('dataRec/road2-12-9road/crosswalkroad_with9road.geojson')
#data_stop=gpd.read_file('dataRec/road2-12-9road/stoplineroad_with9road.geojson')
#info_keys = ['fid', 'geometry']
#stop_juc = pd.DataFrame(data_stop, columns=info_keys)  # Convert list to DataFrame
#print(stop_juc)
car=pd.read_csv("get_car.csv")
car=pd.DataFrame(car)
car=car.drop_duplicates(keep='first', inplace=True)
position=car['position'].iloc[0]
position=str(position)
position=position.replace(',',':')
position=position.split(':')
print(position[3])
#print(car)
'''
def get_junc_stop_value(row):
    fid = row['fid']
    for column in road_stop.columns:
        if fid in road_stop[column].values:
            last_column = road_stop.columns[-1]
            return road_stop.loc[road_stop[column] == fid, last_column].values[0]
    return None

stop_juc['road_junction']=stop_juc.apply(get_junc_stop_value,axis=1)
stop_juc=stop_juc.dropna()
stop_juc.to_csv('stop_divided.csv')
print(stop_juc)'''
'''
def get_junction_value(row):
    road_id = row['road_id']
    for column in road_juc.columns:
        if road_id in road_juc[column].values:
            last_column = road_juc.columns[-1]
            return road_juc.loc[road_juc[column] == road_id, last_column].values[0]
    return None

car['road_junction']=car.apply(get_junction_value,axis=1)
#car.to_csv("car_juc.csv",encoding='utf_8_sig')
print(car)
'''
'''
def get_on_road_value(row):
    fid = row['fid']
    for column in road_df.columns[:21]:
        if fid in road_df[column].values:
            return road_df.loc[road_df[column] == fid, 'on_road'].values[0]
    return None



road_reset['on_road'] = road_reset.apply(get_on_road_value, axis=1)
road_reset=pd.concat([road_reset,ling_df['road_sec_id']],axis=1)

def get_junction_value(row):
    road_sec_id = row['road_sec_id']
    for column in road_juc.columns:
        if road_sec_id in road_juc[column].values:
            last_column = road_juc.columns[-1]
            return road_juc.loc[road_juc[column] == road_sec_id, last_column].values[0]
    return None

def get_junc_walk_value(row):
    fid = row['fid']
    for column in road_juc_walk.columns:
        if fid in road_juc_walk[column].values:
            last_column = road_juc_walk.columns[-1]
            return road_juc_walk.loc[road_juc_walk[column] == fid, last_column].values[0]
    return None

road_reset['road_junction'] = road_reset.apply(get_junction_value, axis=1)
road_reset['category']=ling_df['category']
road_walk['road_juction']=road_walk.apply(get_junc_walk_value,axis=1)
print(road_walk)
road_reset.to_csv('road_divided_1.csv',encoding='utf_8_sig')
#road_walk.to_csv('walk_divided.csv',encoding='utf_8_sig')
#print(road_reset)




#print(road_reset['fid'])'''