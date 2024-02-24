import aspose.slides as slides


def set_video_trim_from_end(global_opts):
    # Path to source presentation
    video_file_name = global_opts.data_dir + "Wildlife.mp4"
    
    with slides.Presentation() as pres:
        slide = pres.slides[0]
        video = pres.videos.add_video(open(video_file_name, "rb").read())
        video_frame = slide.shapes.add_video_frame(0, 0, 200, 200, video)
        
        # sets the trimming start time to 12sec
        video_frame.trim_from_start = 12000
        
        # sets the trimming end time to 16sec
        video_frame.trim_from_end = 14000
        
        # Save presentation
        pres.save(global_opts.out_dir + "VideoTrimming-out.pptx", slides.export.SaveFormat.PPTX)
