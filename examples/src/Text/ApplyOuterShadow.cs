using Aspose.slides.Export
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
    class ApplyOuterShadow
    {
        public static void Run()
        {
            #ExStart:ApplyOuterShadow
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()
            # Create an instance of Presentation class
            with slides.Presentation() as presentation:
            
            # Get reference of a slide
            slide = presentation.slides[0]

            # Add an AutoShape of Rectangle type
            ashp = slide.shapes.add_auto_shape(ShapeType.Rectangle, 150, 75, 400, 300)
            ashp.FillFormat.fill_type = FillType.NoFill

            # Add TextFrame to the Rectangle
            ashp.AddTextFrame("Aspose TextBox")
            port = ashp.text_frame.paragraphs[0].portions[0]
            IPortionFormat pf = port.portion_format
            pf.font_height = 50

            # Enable InnerShadowEffect    
            IEffectFormat ef = pf.EffectFormat
            ef.EnableInnerShadowEffect()

            # Set all necessary parameters
            ef.InnerShadowEffect.BlurRadius = 8.0
            ef.InnerShadowEffect.Direction = 90.0F
            ef.InnerShadowEffect.Distance = 6.0
            ef.InnerShadowEffect.ShadowColor.B = 189

            # Set ColorType as Scheme
            ef.InnerShadowEffect.ShadowColor.ColorType = ColorType.Scheme

            # Set Scheme Color
            ef.InnerShadowEffect.ShadowColor.SchemeColor = SchemeColor.Accent1

            # Save Presentation
            presentation.save(dataDir + "WordArt_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:ApplyOuterShadow
        }
    }
}