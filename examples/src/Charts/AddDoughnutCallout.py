import aspose.pydrawing as drawing
import aspose.slides as slides


def chart_add_doughnut_callout():
	#ExStart:AddDoughnutCallout
	dataDir = "./examples/data/"
	outDir = "./examples/out/"

	with slides.Presentation() as pres:
		slide = pres.slides[0]
		chart = slide.shapes.add_chart(slides.charts.ChartType.DOUGHNUT, 10, 10, 500, 500, False)
		workBook = chart.chart_data.chart_data_workbook
		chart.chart_data.series.clear()
		chart.chart_data.categories.clear()
		chart.has_legend = False
		seriesIndex = 0
		while seriesIndex < 15:
			series = chart.chart_data.series.add(workBook.get_cell(0, 0, seriesIndex + 1, "SERIES " + str(seriesIndex)), chart.type)
			series.explosion = 0
			series.parent_series_group.doughnut_hole_size = 20
			series.parent_series_group.first_slice_angle = 351
			seriesIndex += 1

		categoryIndex = 0
		while categoryIndex < 15:
			chart.chart_data.categories.add(workBook.get_cell(0, categoryIndex + 1, 0, "CATEGORY " + str(categoryIndex)))
			i = 0
			while i < len(chart.chart_data.series):
				iCS = chart.chart_data.series[i]
				dataPoint = iCS.data_points.add_data_point_for_doughnut_series(workBook.get_cell(0, categoryIndex + 1, i + 1, 1))
				dataPoint.format.fill.fill_type = slides.FillType.SOLID
				dataPoint.format.line.fill_format.fill_type = slides.FillType.SOLID
				dataPoint.format.line.fill_format.solid_fill_color.color = drawing.Color.white
				dataPoint.format.line.width = 1
				dataPoint.format.line.style = slides.LineStyle.SINGLE
				dataPoint.format.line.dash_style = slides.LineDashStyle.SOLID
				
				if i == len(chart.chart_data.series) - 1:
					lbl = dataPoint.label
					lbl.text_format.text_block_format.autofit_type = slides.TextAutofitType.SHAPE
					lbl.data_label_format.text_format.portion_format.font_bold = 1
					lbl.data_label_format.text_format.portion_format.latin_font = slides.FontData("DINPro-Bold")
					lbl.data_label_format.text_format.portion_format.font_height = 12
					lbl.data_label_format.text_format.portion_format.fill_format.fill_type = slides.FillType.SOLID
					lbl.data_label_format.text_format.portion_format.fill_format.solid_fill_color.color = drawing.Color.light_gray
					lbl.data_label_format.format.line.fill_format.solid_fill_color.color = drawing.Color.white
					lbl.data_label_format.show_value = False
					lbl.data_label_format.show_category_name = True
					lbl.data_label_format.show_series_name = False
					#lbl.data_label_format.show_label_as_data_callout = True
					lbl.data_label_format.show_leader_lines = True
					lbl.data_label_format.show_label_as_data_callout = False
					chart.validate_chart_layout()
					lbl.as_ilayoutable.x = lbl.as_ilayoutable.x +0.5
					lbl.as_ilayoutable.y = lbl.as_ilayoutable.y + 0.5

				i += 1

			categoryIndex += 1

		pres.save(outDir + "chart_add_doughnut_callout_out.pptx", slides.export.SaveFormat.PPTX)
	#ExEnd:AddDoughnutCallout
