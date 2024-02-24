import aspose.slides as slides


def charts_data_source_type_property_added(options):
    with slides.Presentation(options.data_dir + "charts_with_external_workbook.pptx") as pres:
        slide = pres.slides[0]
        chart = slide.shapes[0]
        source_type = chart.chart_data.data_source_type
        if source_type == slides.charts.ChartDataSourceType.EXTERNAL_WORKBOOK:
            path = chart.chart_data.external_workbook_path
            print("Path to external workbook: {0}".format(path))

        # Saving presentation
        pres.save(options.out_dir + "charts_data_source_type_property_added_out.pptx", slides.export.SaveFormat.PPTX)
