using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/


namespace Aspose.slides.Examples.CSharp.Presentations
{
    public class InsertSvgIntoPresentation
    {
        public static void Run()
        {
            #ExStart:InsertSvgIntoPresentation
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationProperties()
            using (p = new Presentation())
         {
            svgContent = File.ReadAllText(svgPath)
            emfImage = p.Images.AddFromSvg(svgContent)
            p.slides[0].shapes.AddPictureFrame(ShapeType.Rectangle, 0, 0, emfImage.width, emfImage.height, emfImage)
            p.save(outPptxPath, slides.export.SaveFormat.PPTX)

           
            }
            #ExEnd:InsertSvgIntoPresentation
        }
    }
}