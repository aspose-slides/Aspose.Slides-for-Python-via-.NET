import aspose.slides as slides


def convert_to_html5_handout(global_opts):
    with slides.Presentation(global_opts.data_dir + "HandoutExample.pptx") as pres:
        # Set convertion options
        slides_layout_options = slides.export.HandoutLayoutingOptions()
        slides_layout_options.handout = slides.export.HandoutType.HANDOUTS_4_HORIZONTAL
        options = slides.export.Html5Options()
        options.slides_layout_options = slides_layout_options

        # Save presentation
        pres.save(global_opts.out_dir + "HandoutExample.html", slides.export.SaveFormat.HTML5, options)
