import aspose.slides as slides


def refresh_thumbnail_presentation(global_opts):
    with slides.Presentation(global_opts.data_dir + "Image.pptx") as pres:
        # Remove all shapes from the slide
        pres.slides[0].shapes.clear()

        # Save presentation
        pptx_options = slides.export.PptxOptions()
        pptx_options.refresh_thumbnail = False
        pres.save(global_opts.out_dir + "result_with_old_thumbnail.pptx", slides.export.SaveFormat.PPTX, pptx_options)
