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
    class ApplyInnerShadow
    {
        public static void Run()
        {
            #ExStart:ApplyInnerShadow
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate PresentationEx# Instantiate PresentationEx
            with slides.Presentation() as pres:
            {
                # Get the first slide
                sld = pres.slides[0]

                # Add an AutoShape of Rectangle type
                ashp = sld.shapes.add_auto_shape(ShapeType.Rectangle, 150, 75, 150, 50)

                # Add TextFrame to the Rectangle
                ashp.AddTextFrame(" ")

                # Accessing the text frame
                ITextFrame txtFrame = ashp.text_frame

                # Create the Paragraph object for text frame
                para = txtFrame.paragraphs[0]

                # Create Portion object for paragraph
                portion = para.portions[0]

                # Set Text
                portion.text = "Aspose TextBox"

                # Save the presentation to disk
                pres.save(dataDir + "ApplyInnerShadow_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ApplyInnerShadow
        }
    }
}
