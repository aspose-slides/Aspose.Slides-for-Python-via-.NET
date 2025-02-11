import aspose.slides as slides


def fade_in_out_duration_audio_example(global_opts):
    with slides.Presentation() as pres:
        # Add Audio Frame
        with open(global_opts.data_dir + "audio.m4a", "rb") as in_file:
            audio = pres.audios.add_audio(in_file)

        audio_frame = pres.slides[0].shapes.add_audio_frame_embedded(50, 50, 100, 100, audio)

        # Set the duration of the starting fade for 200ms
        audio_frame.fade_in_duration = 200
        # Set the duration of the ending fade for 500ms
        audio_frame.fade_out_duration = 500

        pres.save(global_opts.out_dir + "AudioFrameFade_out.pptx", slides.export.SaveFormat.PPTX)
