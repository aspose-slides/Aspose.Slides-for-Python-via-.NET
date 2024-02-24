import aspose.slides as slides


def resize_slide_with_table(global_opts):
    with slides.Presentation(global_opts.data_dir + "tables.pptx") as presentation:
        # Old slide size
        current_height = presentation.slide_size.size.height
        current_width = presentation.slide_size.size.width

        # Changing slide size
        presentation.slide_size.set_size(slides.SlideSizeType.A4_PAPER, slides.SlideSizeScaleType.DO_NOT_SCALE)

        # New slide size
        new_height = presentation.slide_size.size.height
        new_width = presentation.slide_size.size.width

        ratio_height = new_height / current_height
        ratio_width = new_width / current_width

        for master in presentation.masters:
            for shape in master.shapes:
                # Resize position
                shape.height = shape.height * ratio_height
                shape.width = shape.width * ratio_width

                # Resize shape size if required
                shape.y = shape.y * ratio_height
                shape.x = shape.x * ratio_width

            for layout_slide in master.layout_slides:
                for shape in layout_slide.shapes:
                    # Resize position
                    shape.height = shape.height * ratio_height
                    shape.width = shape.width * ratio_width

                    # Resize shape size if required
                    shape.y = shape.y * ratio_height
                    shape.x = shape.x * ratio_width

        for slide in presentation.slides:
            for shape in slide.shapes:
                # Resize position
                shape.height = shape.height * ratio_height
                shape.width = shape.width * ratio_width

                # Resize shape size if required
                shape.y = shape.y * ratio_height
                shape.x = shape.x * ratio_width
                if type(shape) is slides.Table:
                    table = shape
                    for row in table.rows:
                        row.minimal_height = row.minimal_height * ratio_height
                        # row.height = row.height * ratio_height
                    for col in table.columns:
                        col.width = col.width * ratio_width

        presentation.save(global_opts.out_dir + "tables_resize_out.pptx", slides.export.SaveFormat.PPTX)
