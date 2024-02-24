import aspose.slides as slides


def charts_set_data_range(options):
    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation(options.data_dir + "charts_with_external_workbook.pptx") as presentation:
        # Access first slide marker and add chart with default data
        slide = presentation.slides[0]
        chart = slide.shapes[0]
        chart.chart_data.set_range("Sheet1!A1:B4")
        presentation.save(options.out_dir + "charts_set_data_range_out.pptx", slides.export.SaveFormat.PPTX)
