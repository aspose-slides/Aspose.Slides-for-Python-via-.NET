import aspose.slides as slides
import aspose.slides.mathtext as mathtext


def export_math_paragraph_to_math_ml(global_opts):
    with slides.Presentation() as pres:
        auto_shape = pres.slides[0].shapes.add_math_shape(0, 0, 500, 50)
        math_paragraph = auto_shape.text_frame.paragraphs[0].portions[0].math_paragraph

        math_paragraph.add(mathtext.MathematicalText("a").set_superscript("2").join("+").join(
            mathtext.MathematicalText("b").set_superscript("2")).join("=").join(
            mathtext.MathematicalText("c").set_superscript("2")))

        with open(global_opts.out_dir + "mathml.xml", "wb") as stream:
            math_paragraph.write_as_math_ml(stream)
