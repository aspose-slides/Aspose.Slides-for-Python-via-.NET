import aspose.slides as slides


def save_to_file(global_opts):
    # Instantiate a Presentation object that represents a PPT file
    with slides.Presentation() as presentation:
        # ...do some work here...

        # Save your presentation to a file
        presentation.save(global_opts.out_dir + "save_to_file_out.pptx", slides.export.SaveFormat.PPTX)
