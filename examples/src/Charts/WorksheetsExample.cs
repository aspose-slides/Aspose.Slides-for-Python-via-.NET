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
This example demonstrates using the IChartDataWorksheetCollection interface, ChartDataWorksheetCollection class, and IChartDataWorkbook.Worksheets property.
*/

namespace CSharp.Charts
{
    public class WorksheetsExample
    {
        public static void Run()
        {
            #resultPath = Path.Combine(RunExamples.OutPath, "WorksheetExample.pptx")

            with slides.Presentation() as pres:
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 400, 500)

                workbook = chart.chart_data.chart_data_workbook
                for (i = 0 i < workbook.Worksheets.Count i++)
                {
                    print(workbook.Worksheets[i].Name)
                }
            }
        }
    }
}
