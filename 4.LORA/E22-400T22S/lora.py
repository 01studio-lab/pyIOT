# use EBYTE E22-400T22S uart lora Module

from machine import UART,Pin
import time,struct

class E22_400T22S():
    def __init__(self, uart=3, baud_rate=9600,M0='Y3',M1='Y4'):
        self.uart = UART(uart, baud_rate)
        self.M0=Pin(M0,Pin.OUT,value=0)
        self.M1=Pin(M1,Pin.OUT,value=0)


    #工作模式 0：一般模式；1：WOR模式; 2：配置模式；3：深度睡眠模式。
    def work_mode(self,mode):

        if 0<= mode <= 3:
            self.M1.value(int(mode/2))
            self.M0.value(int(mode%2))
            time.sleep_ms(50)

################################
########### 参数查看 ############
################################

    #查看模块地址
    def Add_Check(self):

        self.work_mode(2) #配置模式

        Add_Check=[0xC1,0x00,0x02]
        Add_Check_hex=struct.pack("%dB"%(len(Add_Check)),*Add_Check)
        self.uart.write(Add_Check_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)

    #查看网络ID
    def NetID_Check(self):

        self.work_mode(2) #配置模式

        NetID_Check=[0xC1,0x02,0x01]
        NetID_Check_hex=struct.pack("%dB"%(len(NetID_Check)),*NetID_Check)
        self.uart.write(NetID_Check_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)

    #查看信道
    def Channel_Check(self):

        self.work_mode(2) #配置模式

        Channel_Check=[0xC1,0x05,0x01]
        Channel_Check_hex=struct.pack("%dB"%(len(Channel_Check)),*Channel_Check)
        self.uart.write(Channel_Check_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)

    #查看传输方式，透明传输：0x03；定点传输：0x43；中继传输：0x63（中继默认和定点传输搭配）；
    def Transfer_Check(self):

        self.work_mode(2) #配置模式

        Transfer_Check=[0xC1,0x06,0x01]
        Transfer_Check_hex=struct.pack("%dB"%(len(Transfer_Check)),*Transfer_Check)
        self.uart.write(Transfer_Check_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)

    #查看波特率，9600：0x62； 115200：0xE3；
    def Baudrate_Check(self):

        self.work_mode(2) #配置模式

        Baudrate_Check=[0xC1,0x03,0x01]
        Baudrate_Check_hex=struct.pack("%dB"%(len(Baudrate_Check)),*Baudrate_Check)
        self.uart.write(Baudrate_Check_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)


    #查看模块全部参数
    def Module_Check(self):

        self.work_mode(2) #配置模式

        Module_Check=[0xC1,0x00,0x09]
        Module_Check_hex=struct.pack("%dB"%(len(Module_Check)),*Module_Check)
        self.uart.write(Module_Check_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)


############################
######## 参数设置 ###########
############################

    #设置模块地址
    def Add_Set(self,ADDH=0x00,ADDL=0x00):

        self.work_mode(2) #配置模式

        Add_Set=[0xC0,0x00,0x02,ADDH,ADDL]
        Add_Set_hex=struct.pack("%dB"%(len(Add_Set)),*Add_Set)
        self.uart.write(Add_Set_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)

    #设置网络地址，NetID
    def NetID_Set(self,NETID=0x00):

        self.work_mode(2) #配置模式

        NetID_Set=[0xC0,0x02,0x01,NETID]
        NetID_Set_hex=struct.pack("%dB"%(len(NetID_Set)),*NetID_Set)
        self.uart.write(NetID_Set_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)

    #设置信道，0-83，实际频率=410.125+CH*1M
    def Channel_Set(self,CH=0x17):

        self.work_mode(2) #配置模式

        Channel_Set=[0xC0,0x05,0x01,CH]
        Channel_Set_hex=struct.pack("%dB"%(len(Channel_Set)),*Channel_Set)
        self.uart.write(Channel_Set_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)

    #设置传输方式，透明传输：0x03；定点传输：0x43；中继传输：0x63（中继默认和定点传输搭配）；
    def Transfer_Set(self,MODE=0x03):

        self.work_mode(2) #配置模式

        Transfer_Set=[0xC0,0x06,0x01,MODE]
        Transfer_Set_hex=struct.pack("%dB"%(len(Transfer_Set)),*Transfer_Set)
        self.uart.write(Transfer_Set_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)

    #设置波特率，9600：0x62； 115200：0xE3；
    def Baudrate_Set(self,MODE=0x62):

        self.work_mode(2) #配置模式

        Baudrate_Set=[0xC0,0x03,0x01,MODE]
        Baudrate_Set_hex=struct.pack("%dB"%(len(Baudrate_Set)),*Baudrate_Set)
        self.uart.write(Baudrate_Set_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)

    #恢复出厂设置
    #频率：433.125MHz;地址：0x0000;信道0x17;空中速率：2.4kbps;波特率：9600；串口格式：8N1;发射功率：22dbm
    def RESET(self):

        self.work_mode(2) #配置模式

        RESET=[0xC0,0x00,0x09,0x00,0x00,0x00,0x62,0x00,0x17,0x03,0x00,0x00]
        RESET_hex=struct.pack("%dB"%(len(RESET)),*RESET)
        self.uart.write(RESET_hex)#发送一条数据
        while not self.uart.any():
            pass

        self.work_mode(0) #恢复一般模式

        return self.uart.read(128)
