import aspose.slides as slides


def layout_placeholder_manager_example(global_opts):
    with slides.Presentation() as pres:
        # Getting the Blank layout slide.
        layout = pres.layout_slides.get_by_type(slides.SlideLayoutType.BLANK)

        # Getting the placeholder manager of the layout slide.
        placeholder_manager = layout.placeholder_manager

        # Adding different placeholders to the Blank layout slide.
        placeholder_manager.add_content_placeholder(10, 10, 300, 200)
        placeholder_manager.add_vertical_text_placeholder(350, 10, 200, 300)
        placeholder_manager.add_chart_placeholder(10, 350, 300, 300)
        placeholder_manager.add_table_placeholder(350, 350, 300, 200)

        # Adding the new slide with Blank layout.
        new_slide = pres.slides.add_empty_slide(layout)

        pres.save(global_opts.out_dir + "placeholders.pptx", slides.export.SaveFormat.PPTX)
