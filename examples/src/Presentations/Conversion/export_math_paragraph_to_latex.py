import aspose.slides as slides
import aspose.slides.mathtext as mathtext


def export_math_paragraph_to_latex():
    with slides.Presentation() as pres:
        # Add a math shape.
        auto_shape = pres.slides[0].shapes.add_math_shape(0, 0, 500, 50)

        # Get a math paragraph.
        math_paragraph = auto_shape.text_frame.paragraphs[0].portions[0].math_paragraph

        # Add a formula.
        math_paragraph.add(mathtext.MathematicalText("a").set_superscript("2").join("+").join(
            mathtext.MathematicalText("b").set_superscript("2")).join("=").join(
            mathtext.MathematicalText("c").set_superscript("2")))

        # Get formula string in Latex format.
        latex_string = math_paragraph.to_latex()

        # Output the resulting Latex string to the console.
        print("Latex representation of a math paragraph: \"" + latex_string + "\"")
