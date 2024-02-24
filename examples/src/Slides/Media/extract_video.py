import aspose.slides as slides


def extract_video(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "Video.pptx") as presentation:
        for shape in presentation.slides[0].shapes:
            if type(shape) is slides.VideoFrame:
                content_type = shape.embedded_video.content_type
                buffer = shape.embedded_video.binary_data
                slash_idx = content_type.rfind('/')
                with open(global_opts.out_dir + "ExtractVideo_out." + content_type[slash_idx + 1:], "wb") as stream:
                    stream.write(buffer)
