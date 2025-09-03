import aspose.slides as slides


def charts_extract_excel_data_example(global_opts):
    external_wb_path = global_opts.data_dir + "book1.xlsx"

    # Extract a value from a cell
    workbook = slides.excel.ExcelDataWorkbook(external_wb_path)
    cell = workbook.get_cell("Sheet2", "B2")
    print(cell.value)

    # Retrieve worksheet names and chart names from an Excel workbook
    sheet_names = workbook.get_worksheet_names()
    for name in sheet_names:
        print("Worksheet", name, "has the following charts:")
        sheet_charts = workbook.get_charts_from_worksheet(name)
        for chart in sheet_charts:
            print(chart.key, "-", chart.value)
