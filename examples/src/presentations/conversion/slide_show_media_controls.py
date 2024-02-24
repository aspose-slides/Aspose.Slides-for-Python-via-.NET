import aspose.slides as slides


def slide_show_media_controls(global_opts):
    with slides.Presentation() as pres:
        # Еnable media control display in slideshow mode. 
        pres.slide_show_settings.show_media_controls = True

        # Save presentation.
        pres.save(global_opts.out_dir + "SlideShowMediaControl.pptx", slides.export.SaveFormat.PPTX)
