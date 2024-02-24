import aspose.slides as slides


def convert_to_markdown(global_opts):
    with slides.Presentation(global_opts.data_dir + "PresentationDemo.pptx") as pres:
        # Create Markdown creation options
        md_options = slides.export.MarkdownSaveOptions()
        # Set parameter for render all items (items that are grouped will be rendered together).
        md_options.export_type = slides.export.MarkdownExportType.VISUAL
        # Set folder name for saving images
        md_options.images_save_folder_name = "md-images"
        # Set path for folder images
        md_options.base_path = global_opts.out_dir

        # Save presentation in Markdown format
        pres.save(global_opts.out_dir + "pres.md", slides.export.SaveFormat.MD, md_options)
