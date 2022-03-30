import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export

namespace CSharp.Charts
{
    class EditChartDatainExternalWorkbook
    {
        public static void Run() {

            # Pay attention the path to external workbook is hardly saved in the presentation
            # so please copy file externalWorkbook.xlsx from Data/Chart directory D:\Aspose.Slides\Aspose.Slides-for-.NET-master\Examples\Data\Charts\ before run the example

            #ExStart:EditChartDatainExternalWorkbook
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()
            using (Presentation pres = new Presentation(dataDir + "presentation.pptx"))
            {
                chart = pres.slides[0].shapes[0]
                ChartData chartData = (ChartData)chart.chart_data
                               

                chartData.series[0].data_points[0].value.as_cell.value = 100
                pres.save(RunExamples.OutPath + "presentation_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:EditChartDatainExternalWorkbook
        }
    }
}
