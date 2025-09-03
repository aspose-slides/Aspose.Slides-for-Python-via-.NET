import aspose.slides as slides


def charts_importing_charts_from_excel_example(global_opts):
    # Path to Excel file
    external_wb_path = global_opts.data_dir + "book1.xlsx"

    # Path to output file
    out_file_name = global_opts.out_dir + "import_excel_chart.pptx"

    # Initializes a new instance using the specified file path
    workbook = slides.excel.ExcelDataWorkbook(external_wb_path)

    with slides.Presentation() as pres:
        blank_layout = pres.layout_slides.get_by_type(slides.SlideLayoutType.BLANK)
        # Gets the names of all worksheets contained in the Excel workbook
        worksheet_names = workbook.get_worksheet_names()
        for name in worksheet_names:
            # Gets a dictionary containing the indexes and names of
            # all charts in the specified worksheet of an Excel workbook
            worksheet_charts = workbook.get_charts_from_worksheet(name)
            for chart in worksheet_charts:
                slide = pres.slides.add_empty_slide(blank_layout)
                # Imports the chart from a workbook file by its name and worksheet name
                slides.importing.ExcelWorkbookImporter.add_chart_from_workbook(slide.shapes, 10, 10, workbook, name,
                                                                               chart.key, False)

        # Saves result
        pres.save(out_file_name, slides.export.SaveFormat.PPTX)
