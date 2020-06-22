#  E22-400T22S

说明：模块厂商 EBYTE，型号：E22-400T22S，购买链接：

出厂参数：工作方式：透传;  波特率：9600

## 构造对象
` ` `
from lora import E22_400T22S
` ` `

` ` `
#构建Lora对象，pybaord串口3，波特率9600, M0和M1为工作模式
Lora=E22_400T22S(3,9600,M0='Y3',M1='Y4') 

` ` `

## 使用方法
### 工作模式
` ` `
#工作模式 0：一般模式；1：WOR模式; 2：配置模式；3：深度睡眠模式。
Lora.work_mode(0) #设置工作模式为模式0
` ` `

### 发送数据
` ` `
Lora.uart.write('Hello 01Studio!') #发送数据
` ` `
### 接收数据
` ` `
Lora.uart.read(512) #接收数据，最多512字节
` ` `

### 查看模块地址
` ` `
Lora.Add_Check()
` ` `
### 设置模块地址
` ` `
Lora.Add_Set(ADDH=0x00,ADDL=0x02) #ADDH：高字节；ADDL：低字节
` ` `

### 查看网络地址 NetID
` ` `
Lora.NetID_Check()
` ` `
### 设置网络地址 NetID
` ` `
Lora.NetID_Set(NETID=0x00)
` ` `

### 查看信道
` ` `
Lora.Channel_Check()
` ` `
### 设置信道
` ` `
Lora.Channel_Set(CH=0x17) #配置信道,0-83，实际频率=410.125+CH*1M, 默认0x17即23
` ` `

### 查看传输方式
` ` `
#查看透明传输：0x03；定点传输：0x43；中继传输：0x63（中继默认和定点传输搭配）；
Lora.Transfer_Check()
` ` `
### 设置传输方式
` ` `
#设置传输方式，透明传输：0x03；定点传输：0x43；中继传输：0x63（中继默认和定点传输搭配）；
Lora.Transfer_Set(MODE=0x43)
` ` `

### 查看波特率
` ` `
#查看波特率，9600：0x62； 115200：0xE3；
Lora.Baudrate_Check()
` ` `
### 设置波特率
` ` `
#设置波特率，9600：0x62； 115200：0xE2；设置完后记得修改开发板波特率以适应
Lora.Baudrate_Set(MODE=0x62)
` ` `

### 模块重置，恢复出厂设置
` ` `
Lora.RESET()  
` ` `

