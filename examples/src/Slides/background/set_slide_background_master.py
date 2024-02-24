import aspose.pydrawing as drawing
import aspose.slides as slides


def set_slide_background_master(global_opts):
    # Instantiate the Presentation class that represents the presentation file
    with slides.Presentation() as pres:
        # Set the background color of the Master to Forest Green
        pres.masters[0].background.type = slides.BackgroundType.OWN_BACKGROUND
        pres.masters[0].background.fill_format.fill_type = slides.FillType.SOLID
        pres.masters[0].background.fill_format.solid_fill_color.color = drawing.Color.forest_green

        # Write the presentation to disk
        pres.save(global_opts.out_dir + "background_for_master_out.pptx", slides.export.SaveFormat.PPTX)
