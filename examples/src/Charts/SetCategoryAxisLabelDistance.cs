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
    public class SetCategoryAxisLabelDistance
    {
        public static void Run()
        {
            #ExStart:SetCategoryAxisLabelDistance
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            with slides.Presentation() as presentation:

            # Get reference of the slide
            sld = presentation.slides[0]

            # Adding a chart on slide
            ch = sld.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 20, 20, 500, 300)

            # Setting the position of label from axis
            ch.axes.horizontal_axis.LabelOffset = 500

            # Write the presentation file to disk
            presentation.save(dataDir + "SetCategoryAxisLabelDistance_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:SetCategoryAxisLabelDistance
        }
    }
}