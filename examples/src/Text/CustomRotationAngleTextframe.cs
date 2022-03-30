using Aspose.slides.Export
using Aspose.slides.Charts
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.text
{
    class CustomRotationAngleTextframe
    {
        public static void Run()
        {
            #ExStart:CustomRotationAngleTextframe

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create an instance of Presentation class
            with slides.Presentation() as presentation:

            chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 500, 300)

            series = chart.chart_data.series[0]

            series.labels.default_data_label_format.show_value = True
            series.labels.default_data_label_format.text_format.text_block_format.RotationAngle = 65

            chart.has_title = True
            chart.chart_title.add_text_frame_for_overriding("Custom title").TextFrameFormat.RotationAngle = -30

            # Save Presentation
            presentation.save(dataDir + "textframe-rotation_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:CustomRotationAngleTextframe
        }
    }
}