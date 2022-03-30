using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp

namespace CSharp.Charts
{
	class SettingCalloutForDataLabel
	{
		public static void Run()
		{
			#ExStart:SettingCalloutForDataLabel
			dataDir = RunExamples.GetDataDir_Charts()
			Presentation pres = new Presentation(dataDir+"testc.pptx")
			slide = pres.slides[0]
			chart = slide.shapes.add_chart(slides.charts.ChartType.DOUGHNUT, 10, 10, 500, 500, False)
			workBook = chart.chart_data.chart_data_workbook
			chart.chart_data.series.clear()
			chart.chart_data.categories.clear()
			chart.has_legend = False
			seriesIndex = 0
			while (seriesIndex < 15)
			{
				series = chart.chart_data.series.add(workBook.get_cell(0, 0, seriesIndex + 1, "SERIES " + seriesIndex), chart.type)
				series.explosion = 0
				series.parent_series_group.doughnut_hole_size = (byte)20
				series.parent_series_group.first_slice_angle = 351
				seriesIndex++
			}
			categoryIndex = 0
			while (categoryIndex < 15)
			{
				chart.chart_data.categories.add(workBook.get_cell(0, categoryIndex + 1, 0, "CATEGORY " + categoryIndex))
				i = 0
				while (i < chart.chart_data.series.Count)
				{
					iCS = chart.chart_data.series[i]
					dataPoint = iCS.data_points.add_data_point_for_doughnut_series(workBook.get_cell(0, categoryIndex + 1, i + 1, 1))
					dataPoint.format.fill.fill_type = slides.FillType.SOLID
					dataPoint.format.line.fill_format.fill_type = slides.FillType.SOLID
					dataPoint.format.line.fill_format.solid_fill_color.color = Color.white
					dataPoint.format.line.width = 1
					dataPoint.format.line.style = LineStyle.Single
					dataPoint.format.line.dash_style = LineDashStyle.Solid
					if (i == chart.chart_data.series.Count - 1)
					{
						lbl = dataPoint.label
						lbl.text_format.text_block_format.autofit_type = TextAutofitType.Shape
						lbl.data_label_format.text_format.portion_format.font_bold = 1
						lbl.data_label_format.text_format.portion_format.latin_font = slides.FontData("DINPro-Bold")
						lbl.data_label_format.text_format.portion_format.font_height = 12
						lbl.data_label_format.text_format.portion_format.fill_format.fill_type = slides.FillType.SOLID
						lbl.data_label_format.text_format.portion_format.fill_format.solid_fill_color.color = Color.light_gray
						lbl.data_label_format.format.line.fill_format.solid_fill_color.color = Color.white
						lbl.data_label_format.show_value = False
						lbl.data_label_format.show_category_name = True
						lbl.data_label_format.show_series_name = False
						#lbl.data_label_format.show_label_as_data_callout = True
						lbl.data_label_format.show_leader_lines = True
						lbl.data_label_format.show_label_as_data_callout = False
						chart.validate_chart_layout()
						lbl.as_ilayoutable.x = (float)lbl.as_ilayoutable.x + (float)0.5
						lbl.as_ilayoutable.y = (float)lbl.as_ilayoutable.y + (float)0.5
					}
					i++
				}
				categoryIndex++
			}
			pres.save("chart.pptx", slides.export.SaveFormat.PPTX)

		}
		#ExEnd:SettingCalloutForDataLabel
	}
}