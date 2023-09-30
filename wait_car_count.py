import datetime

import numpy as np
import pandas as pd
import math

#获得等待车辆数和长度
wait_car=pd.read_excel("wait_deal.xlsx")
wait_car=wait_car.dropna()
wait_car=wait_car.sort_values(by='distance')
wait_car['datatime1'] = pd.to_datetime(wait_car['time_meas']/1000 , unit='ms')
wait_car['datatime1'] = wait_car['datatime1'] + datetime.timedelta(hours=8)
wait_car['wait_number']=np.NaN
#wait_car['wait_length']=np.NaN
#wait_car['wait_s']=np.NaN
#wait_car['final']=np.NaN
#wait_car1=wait_car.groupby(['road_id',pd.Grouper(key='datatime1', freq='20Min')])
d=10

wait_length=[]

wait_car2=wait_car.groupby(['road_id',pd.Grouper(key='datatime1', freq='20Min')])
road_junction=[]
wait_car_number=[]
junction_1=0
d=10
for name,group in wait_car2:
    group['wait_number']=len(group)
    wait_car_number.append(group)
    print(group)

wait_car_number_df=pd.concat(wait_car_number)
wait_car_number_df=wait_car_number_df.drop_duplicates(subset='wait_number')
wait_car_number_df.to_csv('wait_car_static_id.csv')
'''
#第一次统计
for name,group in wait_car1:
    x=1
    z=0
    y=1
    judge=True
    for i in range(len(group)):
            if x==1 and group['distance'].iloc[i]>0 and group['distance'].iloc[i]<=(x*d):
                      group['wait_length'].iloc[x-1]=i+1
            if x>=2 and group['distance'].iloc[i]>d*(x-1) and group['distance'].iloc[i]<=(x*d):
                      group['wait_length'].iloc[x-1]=i+1-group['wait_length'].iloc[x-2]
            elif group['distance'].iloc[i]>(x*d):
                    x+=1
    #print(group)
    group1=group.sort_values(by='wait_length',ascending=False)
   # print(group1)
    if len(group1['wait_length'])>=2:
     if group1['wait_length'].iloc[0]!=None and group1['wait_length'].iloc[1]!=None:
        group['wait_s'].iloc[0]=group1['wait_length'].iloc[0]+group1['wait_length'].iloc[1]
'''
'''
    for i in range(len(group)):
                if y == 1 and group['distance'].iloc[i] > 0 and group['distance'].iloc[i] <= (y * d):
                    group['wait_length_sec'].iloc[y - 1] = i + 1
                if y >= 2 and group['distance'].iloc[i] > d * (y - 1) and group['distance'].iloc[i] <= (y * d):
                    group['wait_length_sec'].iloc[y - 1] = i + 1 - group['wait_length_sec'].iloc[y - 2]
                elif group['distance'].iloc[i] > (y * d):
                    y += 1
    for i in range(len(group['wait_length'])):
        print((group['wait_s'].iloc[0]))
        print(group['wait_length'].iloc[i])
        if group['wait_s'].iloc[0]!=np.NaN:
            if group['wait_length'].iloc[i]<=((group['wait_s'].iloc[0])/4):
             if i==0:
              group['final'].iloc[i]=5
             elif i>0:
                 group['final'].iloc[i]=(i+1)*5
            if (group['wait_s'].iloc[0])==np.NaN or group['final'].iloc[0]==np.NaN:
             group['final'].iloc[i]=15
    wait_length.append(group)
    #print(group)

length_df=pd.concat(wait_length)
length_df=length_df.dropna(subset='final')
length_df.to_csv('wait_length.csv',encoding='utf_8_sig')
print(length_df)'''




#暂时屏蔽
'''
data_stop=pd.read_excel("stop_divided_csv.xlsx")
id_values=[]
x_values=[]
y_values=[]
juc_values=[]
road_values=[]
for i in range(len(data_stop)):
    x0=data_stop['geometry'].iloc[i]
    x0=str(x0)
    x1=x0.split(' ')[0]
    x2=x0.split(' ')[3]
    x=(float(x1)+float(x2))/2
    y0 = data_stop['geometry'].iloc[i]
    y0 = str(y0)
    y1 = y0.split(' ')[1]
    y2 = y0.split(' ')[4]
    y = (float(y1) + float(y2)) / 2
    id_values.append(data_stop['fid'].iloc[i])
    juc_values.append(data_stop['road_junction'].iloc[i])
    road_values.append(data_stop['road_id'].iloc[i])
    x_values.append(x)
    y_values.append(y)

stop_pos=pd.DataFrame({'fid': id_values, 'road_junction':juc_values,'road_id':road_values,'x_pos':x_values,'y_pos':y_values})
#print(stop_pos)

car=pd.read_csv('wait_car_deal.csv')
info_keys = ['id','time_meas', 'road_id','x_pos','y_pos']
car_pos = pd.DataFrame(car, columns=info_keys)  # Convert list to DataFrame


#取速度为0的车，取二十分钟内同一车道上的车
car_pos=car_pos.drop_duplicates(subset=['id','road_id'],keep='last')
car_pos['datatime'] = pd.to_datetime(car_pos['time_meas']/1000 , unit='ms')
car_pos['datatime'] = car_pos['datatime'] + datetime.timedelta(hours=8)
car_pos['distance']=np.NaN
car_pos = car_pos.sort_values(by='time_meas')  # Sort by 'time_meas'
car_pos=car_pos.groupby(['road_id',pd.Grouper(key='datatime', freq='20Min')])
print(car_pos)

def get_distance(m1,m2,n1,n2):
    dis=math.sqrt(math.pow((m1-m2),2)+math.pow((n1-n2),2))
    return dis


car_dis=[]
id=[]
road_id=[]
dis=0
time=[]
time_meas=[]
dis_values=[]

for name,group in car_pos:
    for j in range(len(stop_pos)):
            for i in range(len(group)):
                if stop_pos['road_id'].iloc[j]==group['road_id'].iloc[i]:
                 group['distance'].iloc[i]=get_distance(group['x_pos'].iloc[i],stop_pos['x_pos'].iloc[j],group['y_pos'].iloc[i],stop_pos['y_pos'].iloc[j])
    car_dis.append(group)

dis_df=pd.concat(car_dis)
dis_df.to_csv('wait_deal.csv')
print(dis_df)'''