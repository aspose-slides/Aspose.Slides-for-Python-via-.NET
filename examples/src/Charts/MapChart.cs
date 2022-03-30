using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export

/*
Map charts example.
*/
namespace CSharp.Charts
{
    public class MapChart
    {
        # This example demonstrates creating Map charts.
        # Please pay attension that when you first open a presentation in PP it may take a few seconds to upload an image 
        # of the chart from the Bing service since we don't provide cached image.

        public static void Run()
        {
            resultPath = Path.Combine(RunExamples.OutPath, "MapChart_out.pptx")

            with slides.Presentation() as presentation:
            {
                #create empty chart
                chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.Map, 50, 50, 500, 400, False)

                wb = chart.chart_data.chart_data_workbook

                #Add series and few data points
                series = chart.chart_data.series.add(ChartType.Map)
                series.data_points.AddDataPointForMapSeries(wb.get_cell(0, "B2", 5))
                series.data_points.AddDataPointForMapSeries(wb.get_cell(0, "B3", 1))
                series.data_points.AddDataPointForMapSeries(wb.get_cell(0, "B4", 10))

                #add categories
                chart.chart_data.categories.add(wb.get_cell(0, "A2", "United States"))
                chart.chart_data.categories.add(wb.get_cell(0, "A3", "Mexico"))
                chart.chart_data.categories.add(wb.get_cell(0, "A4", "Brazil"))

                #change data point value    
                dataPoint = series.data_points[1]
                dataPoint.ColorValue.as_cell.value = "15"

                #set data point appearance    
                dataPoint.format.fill.fill_type = slides.FillType.SOLID
                dataPoint.format.fill.solid_fill_color.color = drawing.Color.green

                presentation.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
