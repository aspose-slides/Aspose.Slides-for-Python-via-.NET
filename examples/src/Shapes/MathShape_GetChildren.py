import aspose.slides as slides

"""
This example demonstrates a using of get_children() method of the IMathElement interface.
"""

def foreach_math_element(root):
    for child in root.get_children():
        print("{0} {1}".format(type(child), ": " + str(child.value) if type(child) is slides.mathtext.MathematicalText else ""))
        foreach_math_element(child)


#Path for output presentation
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:
    # Get first slide
    slide = presentation.slides[0]

    # Create MathShape in the first slide
    mathShape = slide.shapes.add_math_shape(10, 10, 500, 500)
    # Create MathParagraph
    mathParagraph = mathShape.text_frame.paragraphs[0].portions[0].math_paragraph

    # Create MathBlock
    mathBlock = slides.mathtext.MathBlock(
        slides.mathtext.MathematicalText("F").
        join("+").
        join(slides.mathtext.MathematicalText("1").divide("y")).underbar())

    # Add MathBlock to the MathParagraph
    mathParagraph.add(mathBlock)
    
    # Print all elements of the mathBlock
    foreach_math_element(mathBlock)

    presentation.save(outDir + "shapes_mathtext_get_children_out.pptx", slides.export.SaveFormat.PPTX)
