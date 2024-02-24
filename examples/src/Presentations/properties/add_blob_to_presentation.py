import aspose.slides as slides


def props_add_blob_to_presentation(global_opts):
    # create a new presentation which will contain this video
    with slides.Presentation() as pres, open(global_opts.data_dir + "video.mp4", "rb") as file_stream:
        # let's add the video to the presentation - we choose KeepLocked behavior, because we not
        # have an intent to access the "veryLargeVideo.avi" file.
        video = pres.videos.add_video(file_stream, slides.LoadingStreamBehavior.KEEP_LOCKED)
        pres.slides[0].shapes.add_video_frame(0, 0, 480, 270, video)

        # save the presentation. Despite that the output presentation will be very large, the memory
        # consumption will be low the whole lifetime of the pres object
        pres.save(global_opts.out_dir + "props_add_blob_to_presentation_out.pptx", slides.export.SaveFormat.PPTX)
