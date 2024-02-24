import aspose.slides as slides


def get_effective_values_of_table(global_opts):
    with slides.Presentation(global_opts.data_dir + "tables.pptx") as pres:
        table = pres.slides[0].shapes[0]
        table_format_effective = table.table_format.get_effective()
        row_format_effective = table.rows[0].row_format.get_effective()
        column_format_effective = table.columns[0].column_format.get_effective()
        cell_format_effective = table.rows[0][0].cell_format.get_effective()

        table_fill_format_effective = table_format_effective.fill_format
        row_fill_format_effective = row_format_effective.fill_format
        column_fill_format_effective = column_format_effective.fill_format
        cell_fill_format_effective = cell_format_effective.fill_format
