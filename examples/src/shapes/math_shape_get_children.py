import aspose.slides as slides
import aspose.slides.mathtext as mathtext


def foreach_math_element(root):
    for child in root.get_children():
        print("{0} {1}".format(type(child),
                               ": " + str(child.value) if type(child) is slides.mathtext.MathematicalText else ""))
        foreach_math_element(child)


def math_shape_get_children(global_opts):
    """This example demonstrates a using of get_children() method of the IMathElement interface."""
    with slides.Presentation() as presentation:
        # Get first slide
        slide = presentation.slides[0]

        # Create MathShape in the first slide
        math_shape = slide.shapes.add_math_shape(10, 10, 500, 500)
        # Create MathParagraph
        math_paragraph = math_shape.text_frame.paragraphs[0].portions[0].math_paragraph

        # Create MathBlock
        math_block = mathtext.MathBlock(
            mathtext.MathematicalText("F").join("+").join(mathtext.MathematicalText("1").divide("y")).underbar())

        # Add MathBlock to the MathParagraph
        math_paragraph.add(math_block)

        # Print all elements of the mathBlock
        foreach_math_element(math_block)

        presentation.save(global_opts.out_dir + "shapes_mathtext_get_children_out.pptx", slides.export.SaveFormat.PPTX)
