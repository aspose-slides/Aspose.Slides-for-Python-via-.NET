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
	class SupportForSwitchingRowsAndColumns
	{
        public static void Run()
		{
			#ExStart:SupportForSwitchingRowsAndColumns

			dataDir = RunExamples.GetDataDir_Charts()
			using (Presentation pres = new Presentation(dataDir + "Test.pptx"))
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 400, 300)

			    IChartSeries[] series = new IChartSeries[chart.chart_data.series.Count]
			    chart.chart_data.series.CopyTo(series, 0)

			    IChartDataCell[] categoriesCells = new IChartDataCell[chart.chart_data.categories.Count]

			    for (i = 0 i < chart.chart_data.categories.Count i++)
			    {
			        categoriesCells[i] = chart.chart_data.categories[i].as_cell
			    }

			    IChartDataCell[] seriesCells = new IChartDataCell[chart.chart_data.series.Count]
			    for (i = 0 i < chart.chart_data.series.Count i++)
			    {
			        seriesCells[i] = chart.chart_data.series[i].Name.AsCells[0]
			    }

			    chart.chart_data.SwitchRowColumn()

			    pres.save(RunExamples.OutPath + "Test_out.pptx", slides.export.SaveFormat.PPTX)
				#ExEnd:SupportForSwitchingRowsAndColumns
			}

		}
	}
}