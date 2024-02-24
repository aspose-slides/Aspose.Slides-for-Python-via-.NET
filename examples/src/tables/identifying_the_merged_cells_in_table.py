import aspose.slides as slides


def dump_merged_cell(i, j, current_cell):
    print("Cell {0}{1} is a part of merged cell with row_span={2} and col_span={3} starting from Cell {4}{5}.".format(
        i, j, current_cell.row_span, current_cell.col_span, current_cell.first_row_index,
        current_cell.first_column_index))


def identifying_the_merged_cells_in_table(global_opts):
    with slides.Presentation(global_opts.data_dir + "tables.pptx") as pres:
        table = pres.slides[0].shapes[0]  # assuming that Slide#0.Shape#0 is a table
        for i in range(len(table.rows)):
            for j in range(len(table.rows[i])):
                current_cell = table.rows[i][j]
                if current_cell.is_merged_cell:
                    dump_merged_cell(i, j, current_cell)
