import aspose.slides as slides


def charts_set_data_range(global_opts):
    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation(global_opts.data_dir + "charts_with_external_workbook.pptx") as presentation:
        # Access first slide marker and add chart with default data
        slide = presentation.slides[0]
        chart = slide.shapes[0]
        chart.chart_data.set_range("Sheet1!A1:B4")
        presentation.save(global_opts.out_dir + "charts_set_data_range_out.pptx", slides.export.SaveFormat.PPTX)
