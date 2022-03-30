import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
	public class TreeMapChart
	{

		#ExStart:TreeMapChart
		public static void Run()
		{

         
		dataDir = RunExamples.GetDataDir_Charts()
           using (Presentation pres = new Presentation(dataDir+"test.pptx"))
			{
				chart = pres.slides[0].shapes.AddChart(Aspose.slides.Charts.ChartType.Treemap, 50, 50, 500, 400)
				chart.chart_data.categories.clear()
				chart.chart_data.series.clear()

				wb = chart.chart_data.chart_data_workbook

				wb.clear(0)

				#branch 1
				IChartCategory leaf = chart.chart_data.categories.add(wb.get_cell(0, "C1", "Leaf1"))
				leaf.GroupingLevels.SetGroupingItem(1, "Stem1")
				leaf.GroupingLevels.SetGroupingItem(2, "Branch1")

				chart.chart_data.categories.add(wb.get_cell(0, "C2", "Leaf2"))

				leaf = chart.chart_data.categories.add(wb.get_cell(0, "C3", "Leaf3"))
				leaf.GroupingLevels.SetGroupingItem(1, "Stem2")

				chart.chart_data.categories.add(wb.get_cell(0, "C4", "Leaf4"))


				#branch 2
				leaf = chart.chart_data.categories.add(wb.get_cell(0, "C5", "Leaf5"))
				leaf.GroupingLevels.SetGroupingItem(1, "Stem3")
				leaf.GroupingLevels.SetGroupingItem(2, "Branch2")

				chart.chart_data.categories.add(wb.get_cell(0, "C6", "Leaf6"))

				leaf = chart.chart_data.categories.add(wb.get_cell(0, "C7", "Leaf7"))
				leaf.GroupingLevels.SetGroupingItem(1, "Stem4")

				chart.chart_data.categories.add(wb.get_cell(0, "C8", "Leaf8"))

				series = chart.chart_data.series.add(Aspose.slides.Charts.ChartType.Treemap)
				series.labels.default_data_label_format.show_category_name = True
				series.data_points.AddDataPointForTreemapSeries(wb.get_cell(0, "D1", 4))
				series.data_points.AddDataPointForTreemapSeries(wb.get_cell(0, "D2", 5))
				series.data_points.AddDataPointForTreemapSeries(wb.get_cell(0, "D3", 3))
				series.data_points.AddDataPointForTreemapSeries(wb.get_cell(0, "D4", 6))
				series.data_points.AddDataPointForTreemapSeries(wb.get_cell(0, "D5", 9))
				series.data_points.AddDataPointForTreemapSeries(wb.get_cell(0, "D6", 9))
				series.data_points.AddDataPointForTreemapSeries(wb.get_cell(0, "D7", 4))
				series.data_points.AddDataPointForTreemapSeries(wb.get_cell(0, "D8", 3))

				series.ParentLabelLayout = ParentLabelLayoutType.Overlapping

				pres.save("Treemap.pptx", slides.export.SaveFormat.PPTX)
			}

		}
        #ExEnd:TreeMapChart
	}
}