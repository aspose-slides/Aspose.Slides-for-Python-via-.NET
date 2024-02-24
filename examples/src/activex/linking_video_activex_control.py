import aspose.slides as slides


def linking_video_activex_control(global_opts):
    # Instantiate Presentation class that represents PPTX file and empty presentation instance
    with slides.Presentation(global_opts.data_dir + "activex_template.pptx") as pres, slides.Presentation() as new_pres:
        # Remove default slide
        new_pres.slides.remove_at(0)

        # Clone slide with Media Player ActiveX Control
        new_pres.slides.insert_clone(0, pres.slides[0])

        # Access the Media Player ActiveX control and set the video path
        control = new_pres.slides[0].controls[0]

        control.properties.remove("URL")
        control.properties.add("URL", global_opts.data_dir + "video.mp4")

        # Save the Presentation
        new_pres.save(global_opts.out_dir + "activex_linking_video_activex_control_out.pptx", slides.export.SaveFormat.PPTX)
