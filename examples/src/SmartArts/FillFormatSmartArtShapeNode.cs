import aspose.pydrawing as drawing
using Aspose.slides.SmartArt
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    class FillFormatSmartArtShapeNode
    {
        public static void Run()
        {
            #ExStart:FillFormatSmartArtShapeNode
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            with slides.Presentation() as presentation:
            {
                # Accessing the slide
                slide = presentation.slides[0]

                # Adding SmartArt shape and nodes
                chevron = slide.shapes.AddSmartArt(10, 10, 800, 60, SmartArtLayoutType.ClosedChevronProcess)
                node = chevron.AllNodes.AddNode()
                node.text_frame.text = "Some text"

                # Setting node fill color
                foreach (item in node.shapes)
                {
                    item.fill_format.fill_type = slides.FillType.SOLID
                    item.fill_format.solid_fill_color.color = drawing.Color.red
                }

                # Saving Presentation
                presentation.save(dataDir + "FillFormat_SmartArt_ShapeNode_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:FillFormatSmartArtShapeNode
        }
    }
}
