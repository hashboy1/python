import xlrd
from xlutils.copy import copy
import os
import xlwt

def FindFileByStr(No,list):
    returnlist = []
    for i, val in enumerate(list):
        #print("序号：%s   值：%s" % (i + 1, val))
        if val[0:len(No)] == No:
            returnlist.append(val)
    return returnlist


filename='固定资产电子台账1.xlsx'
sheetname='卡片列表'
newname=r'newexcel.xls'
imagePath='E:\workspace\pythonTest\excel\images'

#open the excel
wb = xlrd.open_workbook(filename)
oldsheet=wb.sheet_by_name(sheetname)
#copy one new instance to modify
newb = copy(wb)  # 类型为worksheet 无nrows 方法
newsheet = newb.get_sheet(sheetname)
#get image files list
filelist=os.listdir(imagePath)
print(type(filelist))

#create the hyperlink style
style = xlwt.XFStyle() # 初始化样式
font = xlwt.Font() # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True # 黑体
font.underline = True # 下划线
font.italic = True # 斜体字
font.height = 200
font.colour_index= 4
style.font = font # 设定样式

#traverse the excel
for i in range(1,oldsheet.nrows):
    PropertyNo=oldsheet.cell(i,3).value
    PropertyDept=oldsheet.cell(i,8).value
    print("line:"+ str(i)+ ",no:"+str(PropertyNo)+",dept:"+str(PropertyDept))
    #find the image file by property no
    findfilebyno=FindFileByStr(str(PropertyNo),filelist)
    if  len(findfilebyno) != 0:
        for j, val in enumerate(findfilebyno):
            newsheet.write(i, 21+j,xlwt.Formula('HYPERLINK("images/'+val+'";"'+val+'")'),style)
    #if failed, find the image file by department name
    else:
        findfilebyname = FindFileByStr(str(PropertyDept), filelist)
        if len(findfilebyname) != 0:
            for j, val in enumerate(findfilebyname):
                newsheet.write(i, 21 + j, xlwt.Formula('HYPERLINK("images/' + val + '";"'+val+'")'),style)
        else:
            newsheet.write(i, 21, "no picture")
newb.save(newname)


