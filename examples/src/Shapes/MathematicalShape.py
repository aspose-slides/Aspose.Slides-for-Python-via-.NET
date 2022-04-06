import aspose.slides as slides

"""
This example demonstrates of using API for creation a mathematical expression for Pythagorean theorem.
"""
#Path for output presentation
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    # Create a new AutoShape of the type Rectangle to host mathematical content inside and adds it to the end of the collection.
    mathShape = pres.slides[0].shapes.add_math_shape(10, 10, 100, 25)

    # Cteate mathematical paragraph that is a container for mathematical blocks.
    mathParagraph = mathShape.text_frame.paragraphs[0].portions[0].math_paragraph

    # Create mathematical expression as an instance of mathematical text that contained within a MathParagraph.
    mathBlock = slides.mathtext.MathematicalText("c").set_superscript("2") \
            .join("=") \
            .join(slides.mathtext.MathematicalText("a").set_superscript("2")) \
            .join("+") \
            .join(slides.mathtext.MathematicalText("b").set_superscript("2"))

    # Add mathematical expression to the mathematical paragraph.
    mathParagraph.add(mathBlock)

    pres.save(outDir + "shapes_add_math_text_out.pptx", slides.export.SaveFormat.PPTX) 
