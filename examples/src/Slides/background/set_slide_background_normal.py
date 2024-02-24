import aspose.pydrawing as drawing
import aspose.slides as slides


def set_slide_background_normal(global_opts):
    # Instantiate the Presentation class that represents the presentation file
    with slides.Presentation() as pres:
        # Set the background color of the first to Blue
        pres.slides[0].background.type = slides.BackgroundType.OWN_BACKGROUND
        pres.slides[0].background.fill_format.fill_type = slides.FillType.SOLID
        pres.slides[0].background.fill_format.solid_fill_color.color = drawing.Color.blue
        pres.save(global_opts.out_dir + "background_solid_out.pptx", slides.export.SaveFormat.PPTX)
