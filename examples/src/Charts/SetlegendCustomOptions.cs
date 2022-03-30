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

namespace  Aspose.slides.Examples.CSharp.Charts
{
    public class SetlegendCustomOptions
    {
        public static void Run()
        {
            #ExStart:SetlegendCustomOptions
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Create an instance of Presentation class
            with slides.Presentation() as presentation:

            # Get reference of the slide
            slide = presentation.slides[0]

            # Add a clustered column chart on the slide
            chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 500, 500)

            # Set Legend Properties
            chart.legend.x = 50 / chart.width
            chart.legend.y = 50 / chart.height
            chart.legend.width = 100 / chart.width
            chart.legend.height = 100 / chart.height

            # Write presentation to disk
            presentation.save(dataDir + "Legend_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:SetlegendCustomOptions
        }
    }
}