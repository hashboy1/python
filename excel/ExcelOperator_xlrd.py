import xlrd
data = xlrd.open_workbook('固定资产电子台账1.xlsx')
table = data.sheet_by_name(u'卡片列表')
print(table.cell(0,4).value)
print(table.cell(4,0).value)
print(table.max_row)
print(table.max_column)
#table.cell(0,15).value="fff"