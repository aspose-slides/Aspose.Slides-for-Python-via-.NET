using Aspose.slides.Export
using System.IO

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Presentations.Conversion
{
    public class GeneratingSVGWithCustomShapeIDS
    {
        public static void Run()
        {
            #ExStart:GeneratingSVGWithCustomShapeIDS
            dataDir = RunExamples.GetDataDir_Conversion()
            using (Presentation pres = new Presentation(dataDir+ "presentation.pptx"))
            {
                using (FileStream stream = new FileStream(dataDir + "pptxFileName.svg", FileMode.OpenOrCreate))
                {
                    SVGOptions svgOptions = new SVGOptions
                    {
                        ShapeFormattingController = new CustomSvgShapeFormattingController()
                    }

                    pres.slides[0].WriteAsSvg(stream, svgOptions)
                }
            }
            #ExEnd:GeneratingSVGWithCustomShapeIDS        
        }
    }
}