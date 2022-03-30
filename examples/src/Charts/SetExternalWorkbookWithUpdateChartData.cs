import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.Net
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
    class SetExternalWorkbookWithUpdateChartData
    {
        public static void Run() {

            #ExStart:SetExternalWorkbookWithUpdateChartData

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            with slides.Presentation() as pres:
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 400, 600, True)
                IChartData chartData = chart.chart_data

                (chartData as ChartData).set_external_workbook("http:#path/doesnt/exists", False)


                pres.save(dataDir + "SetExternalWorkbookWithUpdateChartData.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:SetExternalWorkbookWithUpdateChartData
        }
    }        
}
