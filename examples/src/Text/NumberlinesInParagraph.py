import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def numberlines_in_paragraph():
    with slides.Presentation() as presentation:
        sld = presentation.slides[0]
        ashp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 75, 150, 50)
        para = ashp.text_frame.paragraphs[0]
        portion = para.portions[0]
        portion.text = "Aspose Paragraph GetLinesCount() Example"
        
        print("Lines Count =", para.get_lines_count())
        
        # Change shape width
        ashp.width = 250
        print("Lines Count after changing shape width =", para.get_lines_count())
