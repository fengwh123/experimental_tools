import numpy as np
import matplotlib.pyplot as plt

# data
# Fz:1~6; Fx:7~12; My: 31~36
# 0:左前轮; 1: 右前轮; 2: 左中轮; 3: 右中轮; 4: 左后轮; 5: 右后轮

for i in range(11):
    print(i)
    for j in range(6):
        data_record_list = []
        with open(str(i+1)+'.csv', 'r') as f:
            data = f.readline()
            data = f.readline()
            while(len(data)>10):
                # print(data)
                data = data.split('\n')[0]
                data = data.split('\t')
                data = [float(i) for i in data]
                data_record_list.append(data[31+j])
                data = f.readline()
        plt.figure(1)
        plt.plot(data_record_list)
        plt.savefig('./MY/'+str(i+1)+'_My_'+str(j)+'.jpg')
        plt.cla()
