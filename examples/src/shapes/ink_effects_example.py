import aspose.slides as slides
from aspose.slides.ink import Ink


def ink_effects_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "InkEffects.pptx") as pres:
        # Get Ink object
        ink = pres.slides[0].shapes[0]
        brush = ink.traces[0].brush

        # Show InkEffects of the brush
        print("InkEffects =", brush.ink_effect)

        # Set image for InkEffects
        image = slides.Images.from_file(global_opts.data_dir + "Effect.png")
        Ink.register_ink_effect_image(brush.ink_effect, image)

        # Save result
        pres.slides[0].get_image(2, 2).save(global_opts.out_dir + "InkEffects.png", slides.ImageFormat.PNG)
