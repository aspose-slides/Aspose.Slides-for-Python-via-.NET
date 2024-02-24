import aspose.slides as slides


def clone_within_same_presentation_to_end(global_opts):
    # Instantiate Presentation class that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Clone the desired slide to the end of the collection of slides in the same presentation
        all_slides = pres.slides

        all_slides.add_clone(pres.slides[0])

        # Write the modified presentation to disk
        pres.save(global_opts.out_dir + "crud_add_clone3_out.pptx", slides.export.SaveFormat.PPTX)
