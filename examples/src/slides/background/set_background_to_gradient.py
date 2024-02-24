import aspose.slides as slides


def set_background_to_gradient(global_opts):
    # Instantiate the Presentation class that represents the presentation file
    with slides.Presentation() as pres:
        # Apply Gradiant effect to the Background
        pres.slides[0].background.type = slides.BackgroundType.OWN_BACKGROUND
        pres.slides[0].background.fill_format.fill_type = slides.FillType.GRADIENT
        pres.slides[0].background.fill_format.gradient_format.tile_flip = slides.TileFlip.FLIP_BOTH

        # Write the presentation to disk
        pres.save(global_opts.out_dir + "background_gradient_format_out.pptx", slides.export.SaveFormat.PPTX)
