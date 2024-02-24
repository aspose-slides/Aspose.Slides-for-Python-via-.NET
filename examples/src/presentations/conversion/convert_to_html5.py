import aspose.slides as slides


def convert_to_html5(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Export a presentation containing slides transitions, animations, and shapes animations to HTML5
        html5_options = slides.export.Html5Options()
        html5_options.animate_shapes = True
        html5_options.animate_transitions = True

        # Save presentation
        pres.save(global_opts.out_dir + "convert_to_html5_out.html", slides.export.SaveFormat.HTML5, html5_options)
