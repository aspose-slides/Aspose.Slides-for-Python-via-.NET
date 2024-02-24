import aspose.slides as slides


def add_slides(global_opts):
    # Instantiate Presentation class that represents the presentation file
    with slides.Presentation() as pres:
        # Instantiate SlideCollection class
        for layout in pres.layout_slides:
            pres.slides.add_empty_slide(layout)

        # Save the PPTX file to the Disk
        pres.save(global_opts.out_dir + "crud_add_empty_slide_out.pptx", slides.export.SaveFormat.PPTX)
