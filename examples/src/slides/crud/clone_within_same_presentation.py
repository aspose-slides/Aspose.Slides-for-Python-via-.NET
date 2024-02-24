import aspose.slides as slides


def clone_within_same_presentation(global_opts):
    # Instantiate Presentation class that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Clone the desired slide to the end of the collection of slides in the same presentation
        all_slides = pres.slides

        # Clone the desired slide to the specified index in the same presentation
        all_slides.insert_clone(2, pres.slides[1])

        # Write the modified presentation to disk
        pres.save(global_opts.out_dir + "crud_add_clone2_out.pptx", slides.export.SaveFormat.PPTX)
