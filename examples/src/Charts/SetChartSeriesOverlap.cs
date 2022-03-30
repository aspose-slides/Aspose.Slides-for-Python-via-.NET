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
    public class SetChartSeriesOverlap
    {
        public static void Run()
        {
            #ExStart:SetChartSeriesOverlap
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            with slides.Presentation() as presentation:
            {
                # Adding chart
                chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400, True)
                IChartSeriesCollection series = chart.chart_data.series
                if (series[0].Overlap == 0)
                {
                    # Setting series overlap
                    series[0].parent_series_group.Overlap = -30
                }

                # Write the presentation file to disk
                presentation.save(dataDir + "SetChartSeriesOverlap_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SetChartSeriesOverlap
        }
    }
}