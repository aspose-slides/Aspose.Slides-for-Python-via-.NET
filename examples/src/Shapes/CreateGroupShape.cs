﻿using Aspose.slides.Export
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
    class CreateGroupShape
    {
        public static void Run()
        {
            #ExStart:CreateGroupShape
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Instantiate Prseetation class 
            with slides.Presentation() as pres:
            {
                # Get the first slide 
                sld = pres.slides[0]

                # Accessing the shape collection of slides 
                IShapeCollection slideShapes = sld.shapes

                # Adding a group shape to the slide 
                IGroupShape groupShape = slideShapes.AddGroupShape()

                # Adding shapes inside added group shape 
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 300, 100, 100, 100)
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 500, 100, 100, 100)
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 300, 300, 100, 100)
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 500, 300, 100, 100)

                # Adding group shape frame 
                groupShape.frame = new ShapeFrame(100, 300, 500, 40, NullableBool.False, NullableBool.False, 0)

                # Write the PPTX file to disk 
                pres.save(dataDir + "GroupShape_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:CreateGroupShape
        }
    }
}



