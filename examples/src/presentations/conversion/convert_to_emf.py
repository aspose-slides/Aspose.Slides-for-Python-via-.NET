import aspose.slides as slides


def convert_to_emf(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "HelloWorld.pptx") as pres, \
        open(global_opts.out_dir + "Result.emf", "wb") as fs:
        # Saves the first slide as a metafile
        pres.slides[0].write_as_emf(fs)
