'''
实验名称：串口LORA模块通信（WeBee TLS-02 BLE模块）
版本：v1.0
日期：2020-5-27
作者：01Studio
说明：通过编程实现串口通信，跟电脑串口助手实现数据收发。
'''

#导入串口模块
from lora import E22_400T22S
from machine import Pin
import time

#构建Lora模块对象（串口）,M0&M1为GPIO配置工作模式
Lora=E22_400T22S(3,9600,M0='Y3',M1='Y4') #设置串口号3和波特率,TX--Y9,RX--Y10

################################################
#####################数据收发####################
################################################

#模式0，默认透传；工作模式 0：一般模式；1：WOR模式; 2：配置模式；3：深度睡眠模式。
Lora.work_mode(0)

###############信息发送################
Lora.uart.write('Hello 01Studio!')#发送一条数据

###############信息接收################
while True:
    if Lora.uart.any(): #查询是否有信息
        text = Lora.uart.read(512) #默认单次最多接收128字节
        print(text)

#################参数查看######################

#查看模块地址
#print(Lora.Add_Check())

#查看网络地址 NetID
#print(Lora.NetID_Check())

#查看信道
#print(Lora.Channel_Check())

#查看传输方式，透明传输：0x03；定点传输：0x43；中继传输：0x63（中继默认和定点传输搭配）；
#print(Lora.Transfer_Check())

#查看波特率，9600：0x62； 115200：0xE3；
#print(Lora.Baudrate_Check())

#查看模块全部参数
#print(Lora.Module_Check())

#################参数设置######################

#配置模块地址,ADDH：高字节；ADDL：低字节
#print(Lora.Add_Set(ADDH=0x00,ADDL=0x02))

#配置网络ID,NetID
#print(Lora.NetID_Set(NETID=0x00))

#配置信道,0-83，实际频率=410.125+CH*1M, 默认0x17即23
#print(Lora.Channel_Set(CH=0x17))

#设置传输方式，透明传输：0x03；定点传输：0x43；中继传输：0x63（中继默认和定点传输搭配）；
#print(Lora.Transfer_Set(MODE=0x43))

#设置波特率，9600：0x62； 115200：0xE2；设置完后需要修改开发板波特率以适应
#print(Lora.Baudrate_Set(MODE=0x62))

#恢复出厂设置
#print(Lora.RESET())

#查看传输方式，透明传输：0x03；定点传输：0x43；中继传输：0x63（中继默认和定点传输搭配）；
#print(Lora.Baudrate_Check())
