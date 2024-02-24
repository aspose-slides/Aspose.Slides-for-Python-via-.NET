import aspose.slides as slides


def clone_to_another_presentation_with_master(global_opts):
    # Instantiate Presentation class to load the source presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as source_pres:
        # Instantiate Presentation class for destination presentation (where slide is to be cloned)
        with slides.Presentation() as dest_pres:
            # Instantiate from the collection of slides in source presentation along with
            # Master slide
            source_slide = source_pres.slides[0]
            source_master = source_slide.layout_slide.master_slide

            # Clone the desired master slide from the source presentation to the collection of masters in the
            # Destination presentation
            masters = dest_pres.masters
            dest_master = source_slide.layout_slide.master_slide

            # Clone the desired master slide from the source presentation to the collection of masters in the
            # Destination presentation
            cloned_slide = masters.add_clone(source_master)

            # Clone the desired slide from the source presentation with the desired master to the end of the
            # Collection of slides in the destination presentation
            dest_slides = dest_pres.slides
            dest_slides.add_clone(source_slide, cloned_slide, True)
        
            # Clone the desired master slide from the source presentation to the collection of masters in the
            # Destination presentation
            # Save the destination presentation to disk
            dest_pres.save(global_opts.out_dir + "crud_clone_with_master_out.pptx", slides.export.SaveFormat.PPTX)
