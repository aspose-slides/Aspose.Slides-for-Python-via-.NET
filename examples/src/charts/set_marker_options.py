import aspose.slides as slides


def charts_set_marker_options(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:
        slide = presentation.slides[0]

        # Creating the default chart
        chart = slide.shapes.add_chart(slides.charts.ChartType.LINE_WITH_MARKERS, 0, 0, 400, 400)

        # Getting the default chart data worksheet index
        default_worksheet_index = 0

        # Getting the chart data worksheet
        fact = chart.chart_data.chart_data_workbook

        # Delete demo series
        chart.chart_data.series.clear()

        # Add new series
        chart.chart_data.series.add(fact.get_cell(default_worksheet_index, 1, 1, "Series 1"), chart.type)
        
        # Set the picture
        image1 = slides.Images.from_file(global_opts.data_dir + "image1.jpg")
        imgx1 = presentation.images.add_image(image1)

        # Set the picture
        image2 = slides.Images.from_file(global_opts.data_dir + "image2.jpg")
        imgx2 = presentation.images.add_image(image2)

        # Take first chart series
        series = chart.chart_data.series[0]

        # Add new point (1:3) there.
        point = series.data_points.add_data_point_for_line_series(fact.get_cell(default_worksheet_index, 1, 1, 4.5))
        point.marker.format.fill.fill_type = slides.FillType.PICTURE
        point.marker.format.fill.picture_fill_format.picture.image = imgx1

        point = series.data_points.add_data_point_for_line_series(fact.get_cell(default_worksheet_index, 2, 1, 2.5))
        point.marker.format.fill.fill_type = slides.FillType.PICTURE
        point.marker.format.fill.picture_fill_format.picture.image = imgx2

        point = series.data_points.add_data_point_for_line_series(fact.get_cell(default_worksheet_index, 3, 1, 3.5))
        point.marker.format.fill.fill_type = slides.FillType.PICTURE
        point.marker.format.fill.picture_fill_format.picture.image = imgx1

        point = series.data_points.add_data_point_for_line_series(fact.get_cell(default_worksheet_index, 4, 1, 4.5))
        point.marker.format.fill.fill_type = slides.FillType.PICTURE
        point.marker.format.fill.picture_fill_format.picture.image = imgx2

        # Changing the chart series marker
        series.marker.size = 15

        # Write presentation to disk
        presentation.save(global_opts.out_dir + "charts_set_marker_options_out.pptx", slides.export.SaveFormat.PPTX)
