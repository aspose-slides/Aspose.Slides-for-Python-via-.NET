import aspose.slides as slides


def remove_hyperlinks(global_opts):
    # Instantiate Presentation class
    with slides.Presentation(global_opts.data_dir + "hyperlink.pptx") as presentation:
        # Removing the hyperlinks from presentation
        presentation.hyperlink_queries.remove_all_hyperlinks()

        # Writing the presentation as a PPTX file
        presentation.save(global_opts.out_dir + "hyperlink_remove_all_hyperlinks_out.pptx",
                          slides.export.SaveFormat.PPTX)
