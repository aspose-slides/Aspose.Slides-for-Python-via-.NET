import aspose.pydrawing as drawing
import aspose.slides as slides


def convert_to_gif(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        gif_options = slides.export.GifOptions()
        gif_options.frame_size = drawing.Size(540, 480)  # the size of the resulted GIF  
        gif_options.default_delay = 1500  # how long each slide will be showed until it will be changed to the next one
        gif_options.transition_fps = 60  # increase FPS to better transition animation quality

        presentation.save(global_opts.out_dir + "convert_to_gif_out.gif", slides.export.SaveFormat.GIF, gif_options)
