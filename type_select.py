import json
import numpy as np
import pandas as pd

i=0
get_car=pd.DataFrame()
get_motor=pd.DataFrame()
get_people=pd.DataFrame()
#处理得到车辆坐标
for i in range(10):
    data=pd.read_json("dataRec/final_part_{}.json".format(i),lines='True')
    car = data[data['type'].isin([1, 4, 6])]  # isin函数多次筛选
    car = car.groupby('id').filter(lambda x: x['is_moving'].sum() != 0)
    car = car[~car['road_id'].isin([0])]
    car = car[car['velocity'].isin([0])]
    x_values=[]
    y_values=[]
    id_values=[]
    vel_values=[]
    time_values=[]
    road_id=[]
    position=''
    for j in range(len(car)):
        position = car['position'].iloc[j]
        position = str(position)
        position = position.replace(',', ':').replace('}',":")
        position = position.split(':')
        id_values.append(car['id'].iloc[j])
        vel_values.append(car['velocity'].iloc[j])
        time_values.append(car['time_meas'].iloc[j])
        road_id.append(car['road_id'].iloc[j])
        x_values.append(position[1])
        y_values.append(position[3])

    car_pos=pd.DataFrame({'id': id_values,'velocity':vel_values,'time_meas':time_values,'road_id':road_id,'x_pos':x_values,'y_pos':y_values})
    print(car_pos)
get_car = pd.concat([get_car, car_pos], axis=0)
get_car.to_csv("wait_car_deal.csv",encoding='utf_8_sig')
print(get_car)
#得到大致处理的车辆
'''
for i in range(10):
    data=pd.read_json("dataRec/final_part_{}.json".format(i),lines='True')
    car = data[data['type'].isin([1, 4, 6])]  # isin函数多次筛选
    car = car.groupby('id').filter(lambda x: x['is_moving'].sum() != 0)
    #car = car.drop_duplicates(keep='first', inplace=True)
    get_car = pd.concat([get_car, car], axis=0)
    print(car)
'''

'''
    motor=data[data['type'].isin([3,10])]
    motor = motor.groupby('id').filter(lambda x: x['is_moving'].sum() != 0)
    people=data[data['type'].isin([2])]
    get_motor=pd.concat([get_motor,motor],axis=0)
    get_people = pd.concat([get_people, people], axis=0)
    print(motor)

get_motor.to_csv("get_motor.csv",encoding='utf_8_sig')
get_people.to_csv("get_people.csv",encoding='utf_8_sig')
'''
'''
    car = data[data['type'].isin([1, 4, 6])]#isin函数多次筛选
    car = car.groupby('id').filter(lambda x: x['is_moving'].sum() != 0)
    get_car=pd.concat([get_car,car],axis=0)
    print(car)

get_car.to_csv("get_car.csv",encoding='utf_8_sig')
print(get_car)'''