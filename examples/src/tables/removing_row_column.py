import aspose.slides as slides


def removing_row_column(global_opts):
    with slides.Presentation() as pres:
        slide = pres.slides[0]
        col_width = [100, 50, 30]
        row_height = [30, 50, 30]

        table = slide.shapes.add_table(100, 100, col_width, row_height)
        table.rows.remove_at(1, False)
        table.columns.remove_at(1, False)
        pres.save(global_opts.out_dir + "tables_remove_at_out.pptx", slides.export.SaveFormat.PPTX)
