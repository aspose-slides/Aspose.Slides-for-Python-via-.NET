import aspose.slides as slides


def add_table_from_workbook_example(global_opts):
    # Path to the source Excel file
    excel_file_path = global_opts.data_dir + "Budget.xlsx"
    # Path to the output presentation
    out_path = global_opts.out_dir + "TableFromWorkbook.xlsx"

    with slides.Presentation() as pres:
        # Get the layout of the first slide to reuse when adding new slides
        slide_layout = pres.slides[0].layout_slide

        # Create workbook instance from file
        workbook = slides.excel.ExcelDataWorkbook(excel_file_path)
        # Import the table using an IExcelDataWorkbook instance
        slides.importing.ExcelWorkbookImporter.add_table_from_workbook(pres.slides[0].shapes, 10, 10, workbook, "Month", "D4:H17")

        # Add a new slide
        second_slide = pres.slides.add_empty_slide(slide_layout)
        # Import the table directly from an Excel file path
        slides.importing.ExcelWorkbookImporter.add_table_from_workbook(second_slide.shapes, 10, 10, excel_file_path, "Budget", "B21:E43")

        # Add a new slide
        third_slide = pres.slides.add_empty_slide(slide_layout)
        # Import the table from an Excel stream
        with open(excel_file_path, "rb") as f:
            slides.importing.ExcelWorkbookImporter.add_table_from_workbook(third_slide.shapes, 10, 10, f, "Budget", "B47:E55")

        # Save the presentation
        pres.save(out_path, slides.export.SaveFormat.PPTX)
