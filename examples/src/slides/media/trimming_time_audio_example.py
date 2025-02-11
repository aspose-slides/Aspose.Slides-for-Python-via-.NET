import aspose.slides as slides


def trimming_time_audio_example(global_opts):
    with slides.Presentation() as pres:
        # Add Audio Frame
        with open(global_opts.data_dir + "audio.m4a", "rb") as in_file:
            audio = pres.audios.add_audio(in_file)

        audio_frame = pres.slides[0].shapes.add_audio_frame_embedded(50, 50, 100, 100, audio)

        # Set the start trimming time 0.5 seconds
        audio_frame.trim_from_start = 500
        # Set the end trimming time 1 seconds
        audio_frame.trim_from_end = 1000

        pres.save(global_opts.out_dir + "AudioFrameTrim_out.pptx", slides.export.SaveFormat.PPTX)
