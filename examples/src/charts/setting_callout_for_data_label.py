import aspose.pydrawing as drawing
import aspose.slides as slides


def charts_setting_callout_for_data_label(global_opts):
	with slides.Presentation() as pres:
		slide = pres.slides[0]
		chart = slide.shapes.add_chart(slides.charts.ChartType.DOUGHNUT, 10, 10, 500, 500, False)
		workbook = chart.chart_data.chart_data_workbook
		chart.chart_data.series.clear()
		chart.chart_data.categories.clear()
		chart.has_legend = False
		series_index = 0
		while series_index < 15:
			series = chart.chart_data.series.add(workbook.get_cell(0, 0, series_index + 1, "SERIES " + str(series_index)), chart.type)
			series.explosion = 0
			series.parent_series_group.doughnut_hole_size = 20
			series.parent_series_group.first_slice_angle = 351
			series_index += 1

		category_index = 0
		while category_index < 15:
			chart.chart_data.categories.add(workbook.get_cell(0, category_index + 1, 0, "CATEGORY " + str(category_index)))
			i = 0
			while i < len(chart.chart_data.series):
				i_cs = chart.chart_data.series[i]
				data_point = i_cs.data_points.add_data_point_for_doughnut_series(workbook.get_cell(0, category_index + 1, i + 1, 1))
				data_point.format.fill.fill_type = slides.FillType.SOLID
				data_point.format.line.fill_format.fill_type = slides.FillType.SOLID
				data_point.format.line.fill_format.solid_fill_color.color = drawing.Color.white
				data_point.format.line.width = 1
				data_point.format.line.style = slides.LineStyle.SINGLE
				data_point.format.line.dash_style = slides.LineDashStyle.SOLID
				if i == len(chart.chart_data.series) - 1:
					lbl = data_point.label
					lbl.text_format.text_block_format.autofit_type = slides.TextAutofitType.SHAPE
					lbl.data_label_format.text_format.portion_format.font_bold = slides.NullableBool.TRUE
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
					lbl.x = lbl.x + 0.5
					lbl.y = lbl.y + 0.5
				i += 1
			category_index += 1
		pres.save(global_opts.out_dir + "charts_setting_callout_for_data_label_out.pptx", slides.export.SaveFormat.PPTX)
