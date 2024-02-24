import aspose.pydrawing as drawing
import aspose.slides as slides


def manage_paragraph_font_properties(global_opts):
    # Instantiate Presentation
    with slides.Presentation(global_opts.data_dir + "text_default_fonts.pptx") as presentation:
        # Accessing a slide using its slide position
        slide = presentation.slides[0]
    
        # Accessing the first and second placeholder in the slide and typecasting it
        tf1 = slide.shapes[0].text_frame
        tf2 = slide.shapes[1].text_frame
    
        # Accessing the first Paragraph
        para1 = tf1.paragraphs[0]
        para2 = tf2.paragraphs[0]

        # Justify the paragraph
        para2.paragraph_format.alignment = slides.TextAlignment.JUSTIFY_LOW

        # Accessing the first portion
        port1 = para1.portions[0]
        port2 = para2.portions[0]

        # Define new fonts
        fd1 = slides.FontData("Elephant")
        fd2 = slides.FontData("Castellar")

        # Assign new fonts to portion
        port1.portion_format.latin_font = fd1
        port2.portion_format.latin_font = fd2

        # Set font to Bold
        port1.portion_format.font_bold = slides.NullableBool.TRUE
        port2.portion_format.font_bold = slides.NullableBool.TRUE

        # Set font to Italic
        port1.portion_format.font_italic = slides.NullableBool.TRUE
        port2.portion_format.font_italic = slides.NullableBool.TRUE

        # Set font color
        port1.portion_format.fill_format.fill_type = slides.FillType.SOLID
        port1.portion_format.fill_format.solid_fill_color.color = drawing.Color.purple
        port2.portion_format.fill_format.fill_type = slides.FillType.SOLID
        port2.portion_format.fill_format.solid_fill_color.color = drawing.Color.peru

        # Write the PPTX to disk
        presentation.save(global_opts.out_dir + "text_manage_paragraph_font_properties_out.pptx", slides.export.SaveFormat.PPTX)
