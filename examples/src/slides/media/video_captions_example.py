import aspose.slides as slides


def video_captions_example(global_opts):
    with slides.Presentation() as pres:
        # Add captions to a VideoFrame
        with open(global_opts.data_dir + "NewVideo.mp4", "rb") as f:
            video = pres.videos.add_video(f.read())
        video_frame = pres.slides[0].shapes.add_video_frame(0, 0, 100, 100, video)

        # Adds the new captions track from file
        video_frame.caption_tracks.add("New track", global_opts.data_dir + "bunny.vtt")

        pres.save(global_opts.out_dir + "VideoCaptionsAdd_out.pptx", slides.export.SaveFormat.PPTX)

    with slides.Presentation(global_opts.out_dir + "VideoCaptionsAdd_out.pptx") as pres:
        video_frame = pres.slides[0].shapes[0]
        if video_frame is not None:
            for idx, caption_track in enumerate(video_frame.caption_tracks):
                # Extracts the captions binary data and saves theme to the file
                with open(global_opts.out_dir + "VideoCaption_out_" + str(idx) + ".vtt", "wb") as f:
                    f.write(caption_track.binary_data)

            # Removes all captions from the VideoFrame
            video_frame.caption_tracks.clear()

            pres.save(global_opts.out_dir + "VideoCaptionsRemove_out.pptx", slides.export.SaveFormat.PPTX)
