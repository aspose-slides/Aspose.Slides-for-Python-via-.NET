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
    public class SetDataRange
    {
        public static void Run()
        {
            #ExStart:SetDataRange
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            # Instantiate Presentation class that represents PPTX file
            Presentation presentation = new Presentation(dataDir + "ExistingChart.pptx")

            # Access first slideMarker and add chart with default data
            slide = presentation.slides[0]
            chart = slide.shapes[0]
            chart.chart_data.SetRange("Sheet1!A1:B4")
            presentation.save(dataDir + "SetDataRange_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:SetDataRange
        }
    }
}