import aspose.slides as slides


def clone_another_presentation_at_specified_position(global_opts):
    # Instantiate Presentation class to load the source presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as source_presentation:
        # Instantiate Presentation class for destination presentation (where slide is to be cloned)
        with slides.Presentation() as destination_presentation:
            # Clone the desired slide from the source presentation to the end
            # of the collection of slides in destination presentation
            slide_collection = destination_presentation.slides

            # Clone the desired slide from the source presentation to the specified position in destination presentation
            slide_collection.insert_clone(1, source_presentation.slides[1])

            # Write the destination presentation to disk
            destination_presentation.save(global_opts.out_dir + "crud_insert_clone_out.pptx",
                                          slides.export.SaveFormat.PPTX)
