using System
using System.Collections.Generic
using System.Linq
using System.text
using System.IO

import aspose.slides as slides
using Aspose.slides.Charts
import aspose.pydrawing as drawing
using Aspose.slides.Export
using Aspose.Cells
using Aspose.slides.Examples.CSharp


namespace CSharp.Charts
{
    class SetChartDataFromWorkBook
    {

        public static void Run()
        {
            dataDir = RunExamples.GetDataDir_Charts()

            using (Presentation pres = new Presentation(/*dataDir + "Test.pptx"*/))
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 500, 400)
                chart.chart_data.chart_data_workbook.clear(0)

                Workbook workbook = None
                try
                {
                    workbook = new Aspose.Cells.Workbook(dataDir + "book1.xlsx")
                }
                catch (Exception ex)
                {
                    Console.Write(ex)
                }

                MemoryStream mem = new MemoryStream()
                workbook.save(mem, Aspose.Cells.SaveFormat.Xlsx)

                mem.Position = 0
                chart.chart_data.WriteWorkbookStream(mem)

                chart.chart_data.SetRange("Sheet2!$A$1:$B$3")
                series = chart.chart_data.series[0]
                series.parent_series_group.IsColorVaried = True
                pres.save(Path.Combine(RunExamples.OutPath, "response2.pptx"), slides.export.SaveFormat.PPTX)
            }
        }
    }
}