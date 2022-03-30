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
    class ChangeShapeOrder
    {
        public static void Run()
        {
            #ExStart:ChangeShapeOrder
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            Presentation presentation1 = new Presentation(dataDir + "HelloWorld.pptx")
            slide = presentation1.slides[0]
            shp3 = slide.shapes.add_auto_shape(ShapeType.Rectangle, 200, 365, 400, 150)
            shp3.fill_format.fill_type = slides.FillType.NO_FILL
            shp3.AddTextFrame(" ")

            ITextFrame txtFrame = shp3.text_frame
            para = txtFrame.paragraphs[0]
            portion = para.portions[0]
            portion.text="Watermark Text Watermark Text Watermark Text"
            shp3 = slide.shapes.add_auto_shape(ShapeType.Triangle, 200, 365, 400, 150)
            slide.shapes.Reorder(2, shp3)
            presentation1.save(dataDir + "Reshape_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:ChangeShapeOrder
        }
    }
}


