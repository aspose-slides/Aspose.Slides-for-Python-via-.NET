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
    public class GetValuesAndUnitScaleFromAxis
    {
        public static void Run()
        {
            #ExStart:GetValuesAndUnitScaleFromAxis
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            with slides.Presentation() as pres:
            {
                Chart chart = (Chart)pres.slides[0].shapes.add_chart(slides.charts.ChartType.Area, 100, 100, 500, 350)
                chart.validate_chart_layout()

                double maxValue = chart.axes.vertical_axis.ActualMaxValue
                double minValue = chart.axes.vertical_axis.ActualMinValue

                double majorUnit = chart.axes.horizontal_axis.ActualMajorUnit
                double minorUnit = chart.axes.horizontal_axis.ActualMinorUnit

                # Saving presentation
                pres.save(dataDir + "ErrorBars_out.pptx", slides.export.SaveFormat.PPTX)
            }


        }
        #ExEnd:GetValuesAndUnitScaleFromAxis
    }
}
