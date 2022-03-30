using System
import aspose.pydrawing as drawing
using Aspose.slides.Export
import aspose.slides as slides
using Aspose.slides.Effects

/*
This code demonstrates an operation where we added a picture for a slide background, added Duotone effect with styled colors, 
and then we got the effective duotone colors with which the background will be rendered.
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    class DuotoneEffectsPVI
    {
        public static void Run()
        {
            with slides.Presentation() as presentation:
            {
                imagePath = RunExamples.GetDataDir_Shapes() + "aspose-logo.jpg"

                # Add image to presentation
                backgroundImage = presentation.images.add_image(Image.FromFile(imagePath))

                # Set background in first slide
                presentation.slides[0].Background.type = BackgroundType.OwnBackground
                presentation.slides[0].Background.FillFormat.fill_type = slides.FillType.PICTURE
                presentation.slides[0].Background.FillFormat.picture_fill_format.picture.image = backgroundImage

                # Add Duotone effect to background
                IDuotone duotone = presentation.slides[0].Background.FillFormat.picture_fill_format.picture.ImageTransform
                    .AddDuotoneEffect()

                # Set Doutone properties
                duotone.Color1.ColorType = ColorType.Scheme
                duotone.Color1.SchemeColor = SchemeColor.Accent1
                duotone.Color2.ColorType = ColorType.Scheme
                duotone.Color2.SchemeColor = SchemeColor.Dark2

                # Get Effective values of the Duotone effect
                IDuotoneEffectiveData duotoneEffective = duotone.GetEffective()

                # Show effective values
                print("Duotone effective color1: " + duotoneEffective.Color1)
                print("Duotone effective color2: " + duotoneEffective.Color2)
            }
        }
    }
}
