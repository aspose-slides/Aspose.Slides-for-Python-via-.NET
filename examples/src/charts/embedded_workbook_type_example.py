import aspose.slides as slides


def charts_embedded_workbook_type_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "EmbeddedWorkbook.pptx") as pres:
        for shape in pres.slides[0].shapes:
            if type(shape) is not slides.charts.Chart:
                continue
            chart_data = shape.chart_data

            # Skip charts whose embedded workbook format is not supported.
            if chart_data.data_source_type == slides.charts.ChartDataSourceType.INTERNAL_WORKBOOK and chart_data.embedded_workbook_type == slides.charts.WorkbookType.WORKBOOK_BINARY_MACRO:
                print("\nSkip charts whose embedded workbook format is", chart_data.embedded_workbook_type)
                continue

            print("\nWork with charts whose embedded workbook format is:", chart_data.embedded_workbook_type)

            # Read or modify chart workbook data.
            print("\tChart old data:", hash(chart_data.series[0].name.as_cells))

            cell = chart_data.series[0].data_points[0].value.as_cell
            print("\tChart new data:", cell.value)

        pres.save(global_opts.out_dir + "EmbeddedWorkbook-out.pptx", slides.export.SaveFormat.PPTX)
