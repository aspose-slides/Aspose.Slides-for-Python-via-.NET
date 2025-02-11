import aspose.slides as slides


def disable_font_ligatures_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "TextLigatures.pptx") as pres:
        # Save with enabled ligatures
        pres.save(global_opts.out_dir + "EnableLigatures-out.html", slides.export.SaveFormat.HTML)

        # Configure export options
        options = slides.export.HtmlOptions()
        options.disable_font_ligatures = True

        # Export presentation to HTML with disabled ligatures
        pres.save(global_opts.out_dir + "DisableLigatures-out.html", slides.export.SaveFormat.HTML, options)
