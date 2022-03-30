import aspose.pydrawing as drawing
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    class SetAlternativeText
    {
        public static void Run()
        {
            #ExStart:SetAlternativeText
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Instantiate Presentation class that represents the PPTX
            with slides.Presentation() as pres:

            # Get the first slide
            sld = pres.slides[0]

            # Add autoshape of rectangle type
            IShape shp1 = sld.shapes.add_auto_shape(ShapeType.Rectangle, 50, 40, 150, 50)
            IShape shp2 = sld.shapes.add_auto_shape(ShapeType.Moon, 160, 40, 150, 50)
            shp2.fill_format.fill_type = slides.FillType.SOLID
            shp2.fill_format.solid_fill_color.color = drawing.Color.gray

            for (i = 0 i < sld.shapes.Count i++)
            {
                shape = sld.shapes[i] as AutoShape
                if (shape != None)
                {
                    AutoShape ashp = shape
                    ashp.AlternativeText = "User Defined"
                }
            }

            # Save presentation to disk
            pres.save(dataDir + "Set_AlternativeText_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:SetAlternativeText
        }
    }
}


