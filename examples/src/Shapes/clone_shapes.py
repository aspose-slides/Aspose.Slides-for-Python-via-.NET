import aspose.slides as slides


def clone_shapes(global_opts):
    # Instantiate Presentation class
    with slides.Presentation(global_opts.data_dir + "shapes_clone.pptx") as pres:
        source_shapes = pres.slides[0].shapes
        blank_layout = pres.masters[0].layout_slides.get_by_type(slides.SlideLayoutType.BLANK)
        dest_slide = pres.slides.add_empty_slide(blank_layout)
        dest_shapes = dest_slide.shapes
        dest_shapes.add_clone(source_shapes[1], 50, 150 + source_shapes[0].height)
        dest_shapes.add_clone(source_shapes[2])
        dest_shapes.insert_clone(0, source_shapes[0], 50, 150)

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_clone_out.pptx", slides.export.SaveFormat.PPTX)
