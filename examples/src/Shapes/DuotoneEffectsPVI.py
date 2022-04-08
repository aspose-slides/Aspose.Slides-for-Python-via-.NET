import aspose.pydrawing as drawing
import aspose.slides as slides

"""
This code demonstrates an operation where we added a picture for a slide background, added Duotone effect with styled colors, 
and then we got the effective duotone colors with which the background will be rendered.
"""
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:
    # Add image to presentation
    backgroundImage = presentation.images.add_image(drawing.Image.from_file(dataDir + "image1.jpg"))

    # Set background in first slide
    presentation.slides[0].background.type = slides.BackgroundType.OWN_BACKGROUND
    presentation.slides[0].background.fill_format.fill_type = slides.FillType.PICTURE
    presentation.slides[0].background.fill_format.picture_fill_format.picture.image = backgroundImage

    # Add Duotone effect to background
    duotone = presentation.slides[0].background.fill_format.picture_fill_format.picture.image_transform.add_duotone_effect()

    # Set Doutone properties
    duotone.color1.color_type = slides.ColorType.SCHEME
    duotone.color1.scheme_color = slides.SchemeColor.ACCENT1
    duotone.color2.color_type = slides.ColorType.SCHEME
    duotone.color2.scheme_color = slides.SchemeColor.DARK2

    # Get Effective values of the Duotone effect
    duotoneEffective = duotone.get_effective()

    # Show effective values
    print("Duotone effective color1: " + str(duotoneEffective.color1))
    print("Duotone effective color2: " + str(duotoneEffective.color2))
