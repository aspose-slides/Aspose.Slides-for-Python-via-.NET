import aspose.slides as slides


def shapes_add_audio_frame(global_opts):
    with open(global_opts.data_dir + "audio.wav", "rb") as in_file:
        # Instantiate Presentation class that represents the PPTX
        with slides.Presentation() as pres:
            # Get the first slide
            slide = pres.slides[0]

            # Add Audio Frame
            audio_frame = slide.shapes.add_audio_frame_embedded(50, 150, 100, 100, in_file)

            # Set Audio to play across the slides
            audio_frame.play_across_slides = True

            # Set Audio to automatically rewind to start after playing
            audio_frame.rewind_audio = True
            
            # Set Play Mode and Volume of the Audio
            audio_frame.play_mode = slides.AudioPlayModePreset.AUTO
            audio_frame.volume = slides.AudioVolumeMode.LOUD

            # Write the PPTX file to disk
            pres.save(global_opts.out_dir + "shapes_add_audio_frame_out.pptx", slides.export.SaveFormat.PPTX)
