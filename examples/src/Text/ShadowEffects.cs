using System.IO
import aspose.slides as slides
using Aspose.slides.Effects
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class ShadowEffects
    {
        public static void Run()
        {
            #ExStart:ShadowEffects
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate a PPTX class
            with slides.Presentation() as pres:
            {

                # Get reference of the slide
                sld = pres.slides[0]

                # Add an AutoShape of Rectangle type
                ashp = sld.shapes.add_auto_shape(ShapeType.Rectangle, 150, 75, 150, 50)


                # Add TextFrame to the Rectangle
                ashp.AddTextFrame("Aspose TextBox")

                # Disable shape fill in case we want to get shadow of text
                ashp.FillFormat.fill_type = FillType.NoFill

                # Add outer shadow and set all necessary parameters
                ashp.EffectFormat.EnableOuterShadowEffect()
                IOuterShadow shadow = ashp.EffectFormat.OuterShadowEffect
                shadow.BlurRadius = 4.0
                shadow.Direction = 45
                shadow.Distance = 3
                shadow.RectangleAlign = RectangleAlignment.TopLeft
                shadow.ShadowColor.PresetColor = PresetColor.Black

                #Write the presentation to disk
                pres.save(dataDir + "pres_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ShadowEffects
        }
    }
}