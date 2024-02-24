import aspose.slides as slides


def add_layout_slides(global_opts):
    # Instantiate Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Try to search by layout slide type
        layout_slides = presentation.masters[0].layout_slides
        layout_slide = layout_slides.get_by_type(slides.SlideLayoutType.TITLE_AND_OBJECT) and layout_slides.get_by_type(
            slides.SlideLayoutType.TITLE)

        if layout_slide is None:
            # The situation when a presentation doesn't contain some type of layouts.
            # presentation File only contains Blank and Custom layout types.
            # But layout slides with Custom types has different slide names,
            # like "Title", "Title and Content", etc. And it is possible to use these
            # names for layout slide selection.
            # Also it is possible to use the set of placeholder shape types. For example,
            # Title slide should have only Title pleceholder type, etc.
            for title_and_object_layout_slide in layout_slides:
                if title_and_object_layout_slide.name == "Title and Object":
                    layout_slide = title_and_object_layout_slide
                    break
            if layout_slide is None:
                for titleLayoutSlide in layout_slides:
                    if titleLayoutSlide.name == "Title":
                        layout_slide = titleLayoutSlide
                        break

                if layout_slide is None:
                    layout_slide = layout_slides.get_by_type(slides.SlideLayoutType.BLANK) or layout_slides.add(slides.SlideLayoutType.TITLE_AND_OBJECT, "Title and Object")

        # Adding empty slide with added layout slide
        presentation.slides.insert_empty_slide(0, layout_slide)

        # Save presentation
        presentation.save(global_opts.out_dir + "layout_add_layout_slides_out.pptx", slides.export.SaveFormat.PPTX)
