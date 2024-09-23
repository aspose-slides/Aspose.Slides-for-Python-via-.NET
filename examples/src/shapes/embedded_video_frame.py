import aspose.slides as slides


def embedded_video_frame(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Embed video inside presentation
        with open(global_opts.data_dir + "video.mp4", "rb") as in_file:
            video = pres.videos.add_video(in_file, slides.LoadingStreamBehavior.READ_STREAM_AND_RELEASE)

            # Add Video Frame
            vf = slide.shapes.add_video_frame(50, 150, 300, 350, video)

            # Set video to Video Frame
            vf.embedded_video = video

            # Set Play Mode and Volume of the Video
            vf.play_mode = slides.VideoPlayModePreset.AUTO
            vf.volume = slides.AudioVolumeMode.LOUD

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_embed_video_frame_out.pptx", slides.export.SaveFormat.PPTX)
