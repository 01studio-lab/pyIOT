# pyIOT
MicroPython for UART IOT Modules

## 项目简介
Micropython是指使用python做各类嵌入式硬件设备编程。MicroPython发展势头强劲，但在IOT上支持的SOC芯片还不多，
而市面上已经拥有非常成熟的串口物联网模块，本项目旨在为市面上成熟的串口物联网模块开发micropython库,让用户可以快速
实现各类物联网相关应用。本项目推荐使用MicroPython兼容性最好的pyboard（基于STM32）开发板。


## 代码贡献说明
项目预设WiFi、BLE、ZigBee、LORA、NBIOT、4G、GPS(北斗) 分类。请在对应分类新建代码，并以模块名称命名。为了保证项目的易用性，本项目代码贡献者必须要求指定格式，至少需包含以下文件：

### 1.example例程
如 main.py
### 2.py库文件
如 tls02.py
### 3.Wire接线图
模块接线说明
### 4.README文件
模块简介，购买链接，基于micropython的构造函数和使用方法。
### 5.其它
模块手册、特别说明等其它相关资料

请参考范例：https://github.com/01studio-lab/pyIOT/tree/master/BLE/TLS-02

## 合作伙伴
如果你的产品或者服务正在本项目被使用，请提交logo图片到主目录-Parter文件夹。
![WeBee](https://github.com/01studio-lab/MicroPython-Examples/blob/master/1.pyBoard%20v1.1(STM32)/4.%E7%89%A9%E8%81%94%E7%BD%91%E6%A8%A1%E5%9D%97/1.%E8%93%9D%E7%89%99(BLE)/TLS-02/Wire%20picture/WeBee%20TLS-02.png)

## 联系方式
Jackey@01studio.org