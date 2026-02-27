import io
import aspose.slides as slides


def to_save_format_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "Presentation.pptm") as source_presentation:
        # Modify the presentation as you need
        source_presentation.slides.add_clone(source_presentation.slides[0])

        # Save the presentation to the stream in its original format
        with io.BytesIO() as stream:
            source_presentation.save(stream, slides.util.SlideUtil.to_save_format(source_presentation.source_format))
