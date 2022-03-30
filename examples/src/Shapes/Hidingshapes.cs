using System
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
    class Hidingshapes
    {
        public static void Run()
        {
            #ExStart:Hidingshapes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Instantiate Presentation class that represents the PPTX
            with slides.Presentation() as pres:

            # Get the first slide
            sld = pres.slides[0]

            # Add autoshape of rectangle type
            IShape shp1 = sld.shapes.add_auto_shape(ShapeType.Rectangle, 50, 40, 150, 50)
            IShape shp2 = sld.shapes.add_auto_shape(ShapeType.Moon, 160, 40, 150, 50)
            alttext = "User Defined"
            iCount = sld.shapes.Count
            for (i = 0 i < iCount i++)
            {
                    AutoShape ashp = (AutoShape)sld.shapes[i]
                    if (String.Compare(ashp.AlternativeText, alttext, StringComparison.Ordinal) == 0)
                    {
                        ashp.Hidden = True
                    }
            }

            # Save presentation to disk
            pres.save(dataDir + "Hiding_Shapes_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:Hidingshapes
        }
    }
}


