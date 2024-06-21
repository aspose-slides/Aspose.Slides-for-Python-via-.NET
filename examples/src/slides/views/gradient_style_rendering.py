import aspose.slides as slides


def gradient_style_rendering(global_opts):
    with slides.Presentation(global_opts.data_dir + "GradientStyleExample.pptx") as pres:
        options = slides.export.RenderingOptions()
        # Set rendering the two-color gradient according to its appearance in the PowerPoint user interface.
        options.gradient_style = slides.GradientStyle.POWER_POINT_UI
        # Get the image.
        img = pres.slides[0].get_image(options, 2, 2)
        # Save image.
        img.save(global_opts.out_dir + "GradientStyleExample-out.png", slides.ImageFormat.PNG)
