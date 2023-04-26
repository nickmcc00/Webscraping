import openpyxl as xl
from openpyxl.styles import Font

wb = xl.Workbook()

ws = wb.active

ws.title = 'First Sheet'

wb.create_sheet(index=1, title='Second Sheet')


ws['A1'] = 'Invoice'

ws['A1'].font = Font(name='Times New Roman', size=24, bold=True, italic=False)

myfont = Font(name='Times New Roman', size=24, bold=True, italic=False)

ws['A1'].font = myfont

ws['A2'] = 'Tires'
ws['A3'] = 'Brakes'
ws['A4'] = 'Alignment'

ws.merge_cells('A1:B1')

ws['B2'] = 450
ws['B3'] = 225
ws['B4'] = 150

ws['A8'] = 'Total'

ws['A8'].font = myfont

ws['B8'] = '=SUM(B2:B4)'


write_sheet = wb['Second Sheet']


new = xl.load_workbook('ProduceReport.xlsx')

produce_sheet = new['ProduceReport']

write_sheet['A1'] = 'Produce'
write_sheet['B1'] = 'Cost Per Pound'
write_sheet['C1'] = 'Amt Sold'
write_sheet['D1'] = 'Total'



for currentrow in produce_sheet.iter_rows(min_row=1, max_row=produce_sheet.max_row, max_col=produce_sheet.max_column):
    print(currentrow[0].value)
    print(currentrow[1].value)
    print(currentrow[2].value)
    print(currentrow[3].value)
    






wb.save('PythontoExcel.xlsx')





