using Aspose.slides.Charts
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class DisplayChartLabels
    {
        public static void Run()
        {
            #ExStart:DisplayChartLabels
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            with slides.Presentation() as presentation:
            {
                chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 500, 400)
                chart.chart_data.series[0].labels.default_data_label_format.show_value = True
                chart.chart_data.series[0].labels.default_data_label_format.show_label_as_data_callout = True
                chart.chart_data.series[0].labels[2].data_label_format.show_label_as_data_callout = False
                presentation.save(dataDir + "DisplayChartLabels_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:DisplayChartLabels
        }
    }
}