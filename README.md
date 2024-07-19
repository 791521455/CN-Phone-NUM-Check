# CN-Phone-NUM-Check
Check China Phone 

title: 手机号归属地查询API-Python
date: 2024-07-19 09:23:37

# 准备工作
## 先找资料
>1.[Google一下](https://www.google.com/search?q=%E6%89%8B%E6%9C%BA%E5%BD%92%E5%B1%9E%E5%9C%B0&oq=%E6%89%8B%E6%9C%BA%E5%BD%92%E5%B1%9E%E5%9C%B0&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABgeMgYIAhAAGB4yBggDEAAYHjIICAQQABgPGB4yCAgFEAAYBRge0gEINDk5MmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8)
>2.[Bing](https://www.bing.com/search?q=%E6%89%8B%E6%9C%BA%E5%8F%B7%E5%BD%92%E5%B1%9E%E5%9C%B0&form=QBLH&sp=-1&ghc=1&lq=0&pq=%E6%89%8B%E6%9C%BA%E5%8F%B7%E5%BD%92%E5%B1%9E%E5%9C%B0&sc=10-6&qs=n&sk=&cvid=1B5A14AA34654DA884CF486C23743ADA&ghsh=0&ghacc=0&ghpl=&rdr=1&rdrig=3FD55BBED3534B958708200483D78D1D)
>3.[百度一下](https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%89%8B%E6%9C%BA%E5%8F%B7%E5%BD%92%E5%B1%9E%E5%9C%B0&fenlei=256&rsv_pq=0xb1b6725500631c90&rsv_t=d6daYARgyNbgAh2Xd39H4CvVqqODnK5AznD38S6ioKmwLc8fa8BQQxCr1lbR&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=13&rsv_sug1=13&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=3635&rsv_sug4=5466)
>4.[搜狗搜索](https://www.sogou.com/web?query=%E6%89%8B%E6%9C%BA%E5%8F%B7%E5%BD%92%E5%B1%9E%E5%9C%B0&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sut=4287&sst0=1721375722458&lkt=1%2C1721375718171%2C1721375718171&sugsuv=00F40C04741A679D66969D955AB60895&sugtime=1721375722458)
>5.[Bilibili](https://search.bilibili.com/all?keyword=%E6%89%8B%E6%9C%BA%E5%8F%B7%E5%BD%92%E5%B1%9E%E5%9C%B0)

得到了大量网站数据

#http://www.yulaoban.club/ca/
#https://api.mir6.com/doc/mobile.html
#https://cx.shouji.360.cn/
#http://tools.bugscaner.com/mobile/
#https://uutool.cn/phone-batch/
#https://www.qvdv.net/tools/qvdv-mobile.html
#https://www.haoshudi.com/
#https://shouji.bmcx.com/
#https://tool.lu/mobile/
#https://www.sogou.com/
#https://www.ip138.com/sj/
#https://cx.shouji.360.cn/?number=13556450000
#https://www.10086.cn/support/selfservice/ownership/
#https://m.ip138.com/mobile.html
#https://hao.360.com/sjgs.html
#https://www.wapi.cn/mobile_area.html
#https://236go.com/gongju/shoujihao/
#https://www.w3tool.com/query/
#https://www.wetools.com/shou-ji-hao
#https://www.lddgo.net/common/phone
#https://www.opengps.cn/Data/Phone/Index.aspx
#https://shoujidiqu.suinidai.cn/
#https://phone.265o.com/
#https://www.haoma123.com/dh/
#https://ip.cn/db.php
#https://guishudi.jihaoba.com/
#https://guishudi.hao86.com/
#https://sjhszdcx.tongchahao.com/
#https://www.tongchaba.com/sjhgsd
大量数据
## 下载python库
```cmd
pip requests
```
## 筛选可用API
发现以下3个API
1."https://www.yulaoban.club/ca/aliyun/getMobileAddressByPhoneNum?phoneNum=" + phonenumber
2."https://api.mir6.com/api/mobile?mobile=" +phonenumber+ "&saorao=true"
3."https://shouji.bmcx.com/" +phonenumber+ "__shouji/"
比较好用
# 开始搓键盘
```Python
import requests
import logging 
```
第一个用于发送请求
第二个用于去除warming

```Python
def APIinfo (phonenumber,apiN,debug):
```
定义函数

```Python
logging.captureWarnings(True) 
```
去除python爬虫安全警告

```Python
info = ["省","市","运营商","状态码"]
```
初始化变量

```Python
response_API_1 = requests.get("https://www.yulaoban.club/ca/aliyun/getMobileAddressByPhoneNum?phoneNum=" + phonenumber,verify=False)
info_get = response_API_1.text
```
发送请求,随便输入一个手机号得到数据如下

```py
{"code":100,"msg":"查询成功","extend":{"mobile":{"userId":0,"phoneNum":"13344550000","num":"13344550000","isp":"陕西电信CDMA卡","prov":"陕西","city":"西安","types":null,"cityCode":"029","areaCode":null,"zipCode":"132000\r\n","lng":null,"lat":null,"date":"2024-06-11 16:26:26.0"}}}
```
分析一下，截取数据

```Python
length_province = len("\"prov\":\"")
length_city = len("\"city\":\"")
length_supplier = len("\"isp\":\"")
ength_code = len("\"code\":")
position_province_beg = info_get.find("\"prov\":\"") + length_province
position_city_beg = info_get.find("\"city\":\"") + length_city
position_supplier_beg = info_get.find("\"isp\":\"") + length_supplier
position_code_beg = info_get.find("\"code\":") + length_code
position_province_end = info_get.find("\"", position_province_beg)
position_city_end = info_get.find("\"", position_city_beg)
position_supplier_end = info_get.find("\"", position_supplier_beg)
position_code_end = info_get.find(",", position_code_beg)
info[0] = info_get[position_province_beg : position_province_end]
info[1] = info_get[position_city_beg : position_city_end]
info[2] = info_get[position_supplier_beg : position_supplier_end]
info[3] = info_get[position_code_beg : position_code_end]
```
输出

```Python
return info
```
这些是基本思路

# 源码以及程序下载见Github
```py
import requests
import logging # 用于去除warming
def APIinfo (phonenumber,apiN,debug):
    logging.captureWarnings(True)  # 去除python爬虫安全警告
    info = ["省","市","运营商","状态码"]
    if apiN == '1':
        # API-1 
        #print("******************API-1*******************")
        response_API_1 = requests.get("https://www.yulaoban.club/ca/aliyun/getMobileAddressByPhoneNum?phoneNum=" + phonenumber,verify=False) # 发送请求
        if debug == True:
            print(response_API_1.text)
        info_get = response_API_1.text

        length_province = len("\"prov\":\"")
        length_city = len("\"city\":\"")
        length_supplier = len("\"isp\":\"")
        length_code = len("\"code\":")

        position_province_beg = info_get.find("\"prov\":\"") + length_province
        position_city_beg = info_get.find("\"city\":\"") + length_city
        position_supplier_beg = info_get.find("\"isp\":\"") + length_supplier
        position_code_beg = info_get.find("\"code\":") + length_code

        position_province_end = info_get.find("\"", position_province_beg)
        position_city_end = info_get.find("\"", position_city_beg)
        position_supplier_end = info_get.find("\"", position_supplier_beg)
        position_code_end = info_get.find(",", position_code_beg)

        info[0] = info_get[position_province_beg : position_province_end]
        info[1] = info_get[position_city_beg : position_city_end]
        info[2] = info_get[position_supplier_beg : position_supplier_end]
        info[3] = info_get[position_code_beg : position_code_end]

        if info[3] == "100":  # 正确状态码
            return info
        elif info[3] == "200":  # 错误状态码
            info = [" ", " ", " ", " "]
            info[3] = info_get[position_code_beg: position_code_end]
            return info
        #print("*****************************************")
    if apiN == '2':
        #API-2 
        #print("******************API-2*******************")
        response_API_2 = requests.get("https://api.mir6.com/api/mobile?mobile=" +phonenumber+ "&saorao=true",verify=False) # 发送请求
        if debug == True:
            print(response_API_2.text)
        info_get = response_API_2.text

        length_province = len("\"province\":\"")
        length_city = len("\"city\":\"")
        length_supplier = len("\"isp\":\"")
        length_code = len("\"code\":")

        position_province_beg = info_get.find("\"province\":\"") + length_province
        position_city_beg = info_get.find("\"city\":\"") + length_city
        position_supplier_beg = info_get.find("\"isp\":\"") + length_supplier
        position_code_beg = info_get.find("\"code\":") + length_code

        position_province_end = info_get.find("\"", position_province_beg)
        position_city_end = info_get.find("\"", position_city_beg)
        position_supplier_end = info_get.find("\"", position_supplier_beg)
        position_code_end = info_get.find(",", position_code_beg)

        info[0] = info_get[position_province_beg: position_province_end]
        info[1] = info_get[position_city_beg: position_city_end]
        info[2] = info_get[position_supplier_beg: position_supplier_end]
        info[3] = info_get[position_code_beg: position_code_end]

        if info[3] == "200": #正确状态码
            return info
        elif info[3] == "201": #错误状态码
            info = [" ", " ", " ", " "]
            info[3] = info_get[position_code_beg: position_code_end]
            return info
        #print("*****************************************")
    if apiN == '4':
        #API-4 
        # print("******************API-4*******************")
        response_API_4 = requests.get("https://shouji.bmcx.com/" +phonenumber+ "__shouji/",verify=False)  # 发送请求
        info_get = response_API_4.text

        length_province_city = len("归属地</td><td bgcolor=\"#FFFFFF\" align=\"center\" style=\"font-size:16px;\">.")
        length_supplier = len("卡类型</td><td bgcolor=\"#FFFFFF\" align=\"center\" style=\"font-size:16px;\">.")

        position_province_city = info_get.find("归属地</td>") + length_province_city
        position_supplier = info_get.find("卡类型</td>") + length_supplier
        position_code1 = str(info_get.find("404 Not Found"))
        position_code2 = str(info_get.find("号码格式错误"))

        position_province_city_div = info_get.find("<", position_province_city)
        position_supplier_div = info_get.find("<", position_supplier)
        #print(info_get)
        supplier = info_get[position_supplier: position_supplier_div]
        province_city = info_get[position_province_city: position_province_city_div]

        info[0] = province_city[0:province_city.find(" ")]
        info[1] = province_city[province_city.find(" "):len(province_city)]
        info[2] = supplier

        if debug == True and position_code1 == "-1" and position_code2 == "-1":
            #print(info_get)
            print(info_get[info_get.find("归属地</td>") : position_supplier_div])
            print(position_code1)
            print(position_code2)
        elif debug == True and ((int(position_code2) >= 4400 and int(position_code2) <= 4600) or (int(position_code1) >= 50 and int(position_code1) <= 100)):
            print(position_code1)
            print(position_code2)
        if position_code1 == "-1" and position_code2 == "-1":  # 正确状态码
            info[3] = position_code1
            return info
        elif (int(position_code2) >= 4400 and int(position_code2) <= 4600) or (int(position_code1) >= 50 and int(position_code1) <= 100):  # 错误状态码
            info = [" ", " ", " ", " "]
            info[3] = position_code1
            return info
        # print("*****************************************")

def main():
    phonenumber = input()
    apiN = "1"
    #debug = True
    debug = False
    print(APIinfo(phonenumber, "1", debug))
    print(APIinfo(phonenumber, "2", debug))
    print(APIinfo(phonenumber, "4", debug))
main()
```
