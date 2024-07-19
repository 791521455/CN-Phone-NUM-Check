import requests
import logging # 用于去除warming
def APIinfo (phonenumber,apiN,debug):
    logging.captureWarnings(True)  # 去除python爬虫安全警告
    info = ["省","市","运营商","状态码"]
    if apiN == '1':
        # API-1 哔哩哔哩UP
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
        #API-2 米人
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
        #API-4 便民网
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