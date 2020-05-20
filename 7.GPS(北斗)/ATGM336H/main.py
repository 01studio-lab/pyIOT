'''
实验名称：GPS模块（中科微 ATGM336H GPS模块）
版本：v1.0
日期：2020-5-20
作者：01Studio
说明：编程实现串口获取GPS数据并显示
'''

#导入串口模块
from machine import UART
import time

#GPS数据说明
#消息ID：$GNGGA,双模GPS
#[0]定位点UTC时间
#[1]纬度[2]纬度方向[3]经度[4]经度方向
#[5]GPS定位状态
#[6]卫星数量
#[7]水平精度衰减因子
#[8]海平面高度[9]高度单位
GPS_INFO=['','','','','','','','','','','','','',''] #14个数据
k1='$GNGGA,' #关键词,双模GPS数据

#构建蓝牙模块对象（串口）
GPS=UART(3,9600) #设置串口号3和波特率,TX--Y9,RX--Y10

#接收信息
while True:

    if GPS.any(): #查询是否有信息
        text0 = GPS.read(1024) #默认单次最多接收128字节'''
        #print(text0) #原始数据

        text=str(text0) #将数据转成字符

        #找到双模定位
        if text.find(k1) != -1 :
            begin_num=text.find(k1)+7 #起始字符
            for i in range(14):
                while text[begin_num]!=',' :
                    GPS_INFO[i] = GPS_INFO[i]+str(text[begin_num])
                    begin_num=begin_num+1
                begin_num=begin_num+1

            print(GPS_INFO) #双模GPS数据

            #时间
            time=GPS_INFO[0].split('.')
            hh=int(int(time[0])/10000)+8 #北京时间东八区
            mm=int(int(time[0])%10000/100)
            ss=int(int(time[0])%100)
            print('Time: '+str(hh)+':'+str(mm)+':'+str(ss))

            #经纬度
            print(GPS_INFO[1]+' '+GPS_INFO[2])
            print(GPS_INFO[3]+' '+GPS_INFO[4])

            #定位状态，1为定位成功
            print('GPS State: '+GPS_INFO[5])

            #卫星数量
            print('Satellites: '+GPS_INFO[6])

            #水平精度衰减因子

            print('Horizontal precision attenuation factor: '+GPS_INFO[7])

            #海拔高度
            print('altitude: '+GPS_INFO[8]+GPS_INFO[9])

            #清空数据
            for i in range(14):
                GPS_INFO[i]=''

