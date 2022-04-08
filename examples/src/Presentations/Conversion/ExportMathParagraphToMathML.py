import aspose.slides as slides

def export_math_paragraph_to_math_ml():
    outDir = "./examples/out/"

    outSvgFileName = outDir + "mathml.xml"

    with slides.Presentation() as pres:
        autoShape = pres.slides[0].shapes.add_math_shape(0, 0, 500, 50)
        mathParagraph = autoShape.text_frame.paragraphs[0].portions[0].math_paragraph

        mathParagraph.add(slides.mathtext.MathematicalText("a").set_superscript("2").join("+")
            .join(slides.mathtext.MathematicalText("b").set_superscript("2")).join("=")
            .join(slides.mathtext.MathematicalText("c").set_superscript("2")))

        with open(outSvgFileName, "xb") as stream:
            mathParagraph.write_as_math_ml(stream)