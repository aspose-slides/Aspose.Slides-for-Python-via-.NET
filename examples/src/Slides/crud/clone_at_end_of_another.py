import aspose.slides as slides


def clone_at_end_of_another(global_opts):
    # Instantiate Presentation class to load the source presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as source_pres:
        # Instantiate Presentation class for destination PPTX (where slide is to be cloned)
        with slides.Presentation() as dest_pres:
            # Clone the desired slide from the source presentation to the end
            # of the collection of slides in destination presentation
            all_slides = dest_pres.slides

            all_slides.add_clone(source_pres.slides[0])

            # Write the destination presentation to disk
            dest_pres.save(global_opts.out_dir + "crud_add_clone_out.pptx", slides.export.SaveFormat.PPTX)
