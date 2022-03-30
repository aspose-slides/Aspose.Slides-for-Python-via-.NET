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
    public class IActualLayoutadded
    {
        public static void Run()
        {
            #ExStart:IActualLayoutadded
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Creating empty presentation
                 with slides.Presentation() as pres:
{
               chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 350)
               chart.validate_chart_layout()

               x = chart.plot_area.actual_x
               y = chart.plot_area.actual_y
               w = chart.plot_area.actual_width
               h = chart.plot_area.actual_height
}
            }
            #ExEnd:IActualLayoutadded
        }
    }
