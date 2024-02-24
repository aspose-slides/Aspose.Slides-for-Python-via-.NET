import aspose.pydrawing as drawing
import aspose.slides as slides


def vertically_align_text(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:
        # Get the first slide
        slide = presentation.slides[0]

        # Define columns with widths and rows with heights
        dbl_cols = [120, 120, 120, 120]
        dbl_rows = [100, 100, 100, 100]

        # Add table shape to slide
        tbl = slide.shapes.add_table(100, 50, dbl_cols, dbl_rows)
        tbl.rows[1][0].text_frame.text = "10"
        tbl.rows[2][0].text_frame.text = "20"
        tbl.rows[3][0].text_frame.text = "30"

        # Accessing the text frame
        text_frame = tbl.rows[0][0].text_frame

        # Create the Paragraph object for text frame
        paragraph = text_frame.paragraphs[0]

        # Create Portion object for paragraph
        portion = paragraph.portions[0]
        portion.text = "Text here"
        portion.portion_format.fill_format.fill_type = slides.FillType.SOLID
        portion.portion_format.fill_format.solid_fill_color.color = drawing.Color.black

        # Aligning the text vertically
        cell = tbl.rows[0][0]
        cell.text_anchor_type = slides.TextAnchorType.CENTER
        cell.text_vertical_type = slides.TextVerticalType.VERTICAL270

        # Save Presentation
        presentation.save(global_opts.out_dir + "tables_vertical_align_text_out.pptx", slides.export.SaveFormat.PPTX)
