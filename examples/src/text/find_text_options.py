import aspose.slides as slides


def find_text_options(global_opts):
    with slides.Presentation(global_opts.data_dir + "TextOptionsExample.pptx") as pres:
        options = slides.TextSearchOptions()
        options.include_notes = True
        options.case_sensitive = True

        pres.replace_text("old", "new", options, None)
        pres.save(global_opts.out_dir + "TextOptionsExample-out.pptx", slides.export.SaveFormat.PPTX)
