import aspose.pydrawing as drawing
import aspose.slides as slides
import aspose.slides as slides

"""
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
"""

namespace Aspose.slides.Examples.CSharp.shapes
{
    class FillShapeswithSolidColor
    {
        public static void Run()
        {
            #ExStart:FillShapeswithSolidColor
            # The path to the documents directory.                    
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create an instance of Presentation class
            with slides.Presentation() as presentation:

            # Get the first slide
            slide = presentation.slides[0]

            # Add autoshape of rectangle type
            shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)

            # Set the fill type to Solid
            shape.fill_format.fill_type = slides.FillType.SOLID

            # Set the color of the rectangle
            shape.fill_format.solid_fill_color.color = drawing.Color.yellow

            #Write the PPTX file to disk
            presentation.save(dataDir + "RectShpSolid_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:FillShapeswithSolidColor
        }
    }
}

