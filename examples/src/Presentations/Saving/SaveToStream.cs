using System.IO
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Presentations.Saving
{
    class SaveToStream
    {
        public static void Run()
        {
            #ExStart:SaveToStream
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationSaving()

            # Instantiate a Presentation object that represents a PPT file
            with slides.Presentation() as presentation:
            {

                shape = presentation.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 200, 200, 200, 200)

                # Add text to shape
                shape.text_frame.text = "This demo shows how to Create PowerPoint file and save it to Stream."

                FileStream toStream = new FileStream(dataDir + "Save_As_Stream_out.pptx", FileMode.Create)
                presentation.save(toStream, slides.export.SaveFormat.PPTX)
                toStream.Close()
            }
            #ExEnd:SaveToStream
        }
    }
}
