import aspose.slides as slides
import aspose.slides.mathtext as mathtext


def math_phantom_example(global_opts):
    # Path for output presentation
    with slides.Presentation() as pres:
        auto_shape = pres.slides[0].shapes.add_math_shape(0, 0, 500, 30)
        math_paragraph = auto_shape.text_frame.paragraphs[0].portions[0].math_paragraph

        eq1 = mathtext.MathematicalText("eq1")
        eq2 = mathtext.MathematicalText("eq2")

        phant = mathtext.MathPhantom(
            mathtext.MathFraction(mathtext.MathematicalText("1"), mathtext.MathematicalText("2")))
        phant.show = False
        phant.zero_asc = True

        first = mathtext.MathematicalText("    (1)")
        sect = mathtext.MathematicalText("    (2)")
        second = mathtext.MathematicalText().join(phant).join(sect)
        nums = mathtext.MathArray([first, second])
        eqs = mathtext.MathDelimiter(mathtext.MathArray([eq1, eq2]))
        eqs.beginning_character = '{'
        eqs.ending_character = '}'
        whole_block = mathtext.MathematicalText().join(eqs).join(" ").join(nums)
        math_paragraph.add(whole_block)

        pres.save(global_opts.out_dir + "math_phantom_example_out.pptx", slides.export.SaveFormat.PPTX)
