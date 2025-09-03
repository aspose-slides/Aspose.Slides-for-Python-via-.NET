import aspose.slides as slides


def audio_captions_example(global_opts):
    media_file = global_opts.data_dir + "audio.mp3"
    track_file = global_opts.data_dir + "bunny.vtt"
    out_caption_file = global_opts.out_dir + "AudioCaption_out.vtt"
    out_add_path = global_opts.out_dir + "AudioCaptionAdd_out.vtt"
    out_remove_path = global_opts.out_dir + "AudioCaptionRemove_out.vtt"

    # Add captions to a VideoFrame
    with slides.Presentation() as pres:
        with open(media_file, "rb") as f:
            audio = pres.audios.add_audio(f)
        audio_frame = pres.slides[0].shapes.add_audio_frame_embedded(10, 10, 50, 50, audio)

        # Adds the new captions track from file
        audio_frame.caption_tracks.add("New track", track_file)

        pres.save(out_add_path, slides.export.SaveFormat.PPTX)

    # Extract captions from a VideoFrame
    with slides.Presentation(out_add_path) as pres:
        audio_frame = pres.slides[0].shapes[0]
        if audio_frame is not None:
            for caption_track in audio_frame.caption_tracks:
                # Extracts the captions binary data and saves theme to the file
                with open(out_caption_file, "wb") as f:
                    f.write(caption_track.binary_data)

            # Removes all captions from the VideoFrame
            audio_frame.caption_tracks.clear()

            pres.save(out_remove_path, slides.export.SaveFormat.PPTX)
