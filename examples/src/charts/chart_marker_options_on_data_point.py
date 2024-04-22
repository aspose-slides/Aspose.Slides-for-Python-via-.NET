import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_marker_options_on_data_point(global_opts):
	with slides.Presentation() as pres:
		slide = pres.slides[0]

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
		img = slides.Images.from_file(global_opts.data_dir + "image1.jpg")
		imgx1 = pres.images.add_image(img)

		# Set the picture
		img2 = slides.Images.from_file(global_opts.data_dir + "image2.jpg")
		imgx2 = pres.images.add_image(img2)

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

		pres.save(global_opts.out_dir + "charts_marker_options_on_data_point_out.pptx", slides.export.SaveFormat.PPTX)
