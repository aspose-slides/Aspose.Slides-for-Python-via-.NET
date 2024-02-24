import aspose.slides as slides
import aspose.slides.mathtext as mathtext


def mathematical_shape(global_opts):
    """This example demonstrates of using API for creation a mathematical expression for Pythagorean theorem."""
    with slides.Presentation() as pres:
        # Create a new AutoShape of the type Rectangle to host mathematical content inside
        # and adds it to the end of the collection.
        math_shape = pres.slides[0].shapes.add_math_shape(10, 10, 100, 25)

        # Create mathematical paragraph that is a container for mathematical blocks.
        math_paragraph = math_shape.text_frame.paragraphs[0].portions[0].math_paragraph

        # Create mathematical expression as an instance of mathematical text that contained within a MathParagraph.
        math_block = mathtext.MathematicalText("c").set_superscript("2") \
            .join("=") \
            .join(mathtext.MathematicalText("a").set_superscript("2")) \
            .join("+") \
            .join(mathtext.MathematicalText("b").set_superscript("2"))

        # Add mathematical expression to the mathematical paragraph.
        math_paragraph.add(math_block)

        pres.save(global_opts.out_dir + "shapes_add_math_text_out.pptx", slides.export.SaveFormat.PPTX)
