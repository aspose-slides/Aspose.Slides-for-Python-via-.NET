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
    class set_external_workbook
    {
        public static void Run() {
            #ExStart:set_external_workbook
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()
            with slides.Presentation() as pres:
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 400, 600, False)
                IChartData chartData = chart.chart_data
                                
                chartData.set_external_workbook(dataDir+ "externalWorkbook.xlsx")
                              

                chartData.series.add(chartData.chart_data_workbook.get_cell(0, "B1"), ChartType.PIE)
                chartData.series[0].data_points.AddDataPointForPieSeries(chartData.chart_data_workbook.get_cell(0, "B2"))
                chartData.series[0].data_points.AddDataPointForPieSeries(chartData.chart_data_workbook.get_cell(0, "B3"))
                chartData.series[0].data_points.AddDataPointForPieSeries(chartData.chart_data_workbook.get_cell(0, "B4"))

                chartData.categories.add(chartData.chart_data_workbook.get_cell(0, "A2"))
                chartData.categories.add(chartData.chart_data_workbook.get_cell(0, "A3"))
                chartData.categories.add(chartData.chart_data_workbook.get_cell(0, "A4"))
                pres.save(dataDir + "Presentation_with_externalWorkbook.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:set_external_workbook
        }
    }
}
