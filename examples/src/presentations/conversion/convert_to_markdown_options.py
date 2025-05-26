import aspose.slides as slides


def convert_to_markdown_options(global_opts):
    with slides.Presentation(global_opts.data_dir + "PresentationDemo.pptx") as pres:
        options = slides.export.MarkdownSaveOptions()
        options.remove_empty_lines = True
        options.handle_repeated_spaces = slides.export.HandleRepeatedSpaces.ALTERNATE_SPACES_TO_NBSP
        options.slide_number_format = "## Slide {0} -"
        options.show_slide_number = True
        options.export_type = slides.export.MarkdownExportType.TEXT_ONLY
        options.flavor = slides.export.Flavor.DEFAULT

        # Save presentation in Markdown format
        pres.save(global_opts.out_dir + "pres-out.md", slides.export.SaveFormat.MD, options)
