import os
import re, shutil
from shutil import copyfile
class Mapreading():
    def Change_Format():
    #    os.listdir(r"G:\360MoveData\Users\Jin\Desktop\smap")#列出当前目录下所有的文件
        copyfile(r"G:\360MoveData\Users\Jin\Desktop\smap\2.smap",r"G:\360MoveData\Users\Jin\Desktop\txt\2.txt")#把smap文件复制到另外一个文件夹并命名成txt格式
    
                
    def Get_position_line():
        map1 = open(r"G:\360MoveData\Users\Jin\Desktop\txt\2.txt", 'r+')
        map1 = map1.read()#把读取到内存中的文件转换成字符串
        
        print("################获取第一个起始点名称、x坐标、Y坐标#################")
        str_startPos = 'startPos'
        first_startPos_num =  map1.index(str_startPos) #获取第一个startPos的位置名称
        print("first_startPos_num: ", first_startPos_num)
        first_startlocation_name = map1[first_startPos_num+27:first_startPos_num+31]#获取第一个站点的字符名称
        if first_startlocation_name[-1] == "\""   :  #如果名称中最后一位是 “号, 则把它去掉
            first_startlocation_name = first_startlocation_name[:-1]
            print("first_startlocation_name: "+ first_startlocation_name)
            number = re.findall(r'\d+', first_startlocation_name)#提取名称字符中的数字
            print(list(map(int,number)))    
        start_pos_x = map1[first_startPos_num+39:first_startPos_num+50]#获取站点的X坐标名称
        start_pos_y = map1[first_startPos_num+50:first_startPos_num+61]#获取站点的y坐标名称
        number_y = re.findall(r'\d+.\d+',start_pos_y)#提取名称字符中的小数
        number_x = re.findall(r'\d+.\d+',start_pos_x)
        print("number_x: ", number_x)
        print("number_y: ", number_y)
        
      
        print("################获取第一个终点名称、x坐标、Y坐标#################")
        str_endPos = 'endPos'
        first_endPos_num =  map1.index(str_endPos) #获取第一个endPos的位置
        print("first_endPos_num: ", first_endPos_num)
        first_endlocation_name = map1[first_endPos_num+25:first_endPos_num+31]#获取第一个站点的字符名称
    
        if first_endlocation_name[-1] == "\""   :  #如果名称中最后一位是 “号, 则把它去掉
            first_endlocation_name = first_endlocation_name[:-1]
            print("first_endlocation_name: "+ first_endlocation_name)
            number = re.findall(r'\d+', first_endlocation_name)#提取名称字符中的数字
            print(list(map(int,number)))
        end_pos_x = map1[first_startPos_num+39:first_startPos_num+50]#获取站点的X坐标名称
        end_Pos_y = map1[first_startPos_num+50:first_startPos_num+61]#获取站点的y坐标名称
        number_y = re.findall(r'\d+.\d+',end_Pos_y)#提取名称字符中的小数
        number_x = re.findall(r'\d+.\d+',end_pos_x)
        print("number_x: ", number_x)
        print("number_y: ", number_y)
        
        
        print("################输出剩余所有startPos和endpos的名称、x坐标、Y坐标#################")
        next_endPos_num = int(first_startPos_num)
        next_endPos_num = int(first_endPos_num)
        while next_endPos_num < len(map1) :#输出所有startPos和endpos的位置#
            try:
                next_endPos_num = map1.index(str_startPos, next_endPos_num+1 )
                print ("next_endPos_num: ", next_endPos_num)
                next_startlocation_name = map1[next_endPos_num+27:next_endPos_num+31]#获取下一个站点的字符名称
                if next_startlocation_name[-1] == "\""   :  
                    next_startlocation_name = next_startlocation_name[:-1]#如果名称中最后一位是 “号, 则重新赋值把它去掉
                    print("next_startlocation_name: "+next_startlocation_name)
                    number = re.findall(r'\d+', next_startlocation_name)#提取名称字符中的数字
                    print(list(map(int,number)))
                next_start_pos_x = map1[next_endPos_num+39:next_endPos_num+50]#获取站点的X坐标名称
                next_start_pos_y = map1[next_endPos_num+50:next_endPos_num+61]#获取站点的y坐标名称
                number_y = re.findall(r'\d+.\d+',next_start_pos_y)#提取名称字符中的小数
                number_x = re.findall(r'\d+.\d+',next_start_pos_x)
                print("number_x: ", number_x)
                print("number_y: ", number_y)
            except  ValueError as err:
                break
        
            try:
                next_endPos_num = map1.index(str_endPos, next_endPos_num+1 )
                print ("next_endPos_num: ", next_endPos_num)
                next_endlocation_name = map1[next_endPos_num+25:next_endPos_num+31]#获取下一个站点的字符名称
                if next_endlocation_name[-1] == "\""   :  
                    next_endlocation_name = next_endlocation_name[:-1]#如果名称中最后一位是 “号, 则重新赋值把它去掉
                    print("next_endlocation_name: "+next_endlocation_name)
                    number = re.findall(r'\d+', next_endlocation_name)#提取名称字符中的数字
                    print(list(map(int,number)))
                next_end_pos_x = map1[next_endPos_num+39:next_endPos_num+50]#获取站点的X坐标名称
                next_end_pos_y = map1[next_endPos_num+50:next_endPos_num+61]#获取站点的y坐标名称
                number_y = re.findall(r'\d+.\d+',next_end_pos_y)#提取名称字符中的小数
                number_x = re.findall(r'\d+.\d+',next_end_pos_x)
                print("number_x: ", number_x)
                print("number_y: ", number_y)
            except  ValueError as err:
                break    
    

