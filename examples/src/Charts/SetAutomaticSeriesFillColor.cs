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
    public class SetAutomaticSeriesFillColor
    {
        public static void Run()
        {
            #ExStart:SetAutomaticSeriesFillColor
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()
            with slides.Presentation() as presentation:
            {
                # Creating a clustered column chart
                chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 50, 600, 400)

                # Setting series fill format to automatic
                for (i = 0 i < chart.chart_data.series.Count i++)
                {
                    chart.chart_data.series[i].GetAutomaticSeriesColor()
                }

                # Write the presentation file to disk
                presentation.save(dataDir + "AutoFillSeries_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SetAutomaticSeriesFillColor
        }
    }
}