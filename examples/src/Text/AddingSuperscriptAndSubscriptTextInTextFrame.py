import aspose.slides as slides


#ExStart:AddingSuperscriptAndSubscriptTextInTextFrame
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:
    # Get slide
    slide = presentation.slides[0]

    # Create text box
    shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 200, 100)
    textFrame = shape.text_frame
    textFrame.paragraphs.clear()

    # Create paragraph for superscript text
    superPar = slides.Paragraph()

    # Create portion with usual text
    portion1 = slides.Portion()
    portion1.text = "SlideTitle"
    superPar.portions.add(portion1)

    # Create portion with superscript text
    superPortion = slides.Portion()
    superPortion.portion_format.escapement = 30
    superPortion.text = "TM"
    superPar.portions.add(superPortion)

    # Create paragraph for subscript text
    paragraph2 = slides.Paragraph()

    # Create portion with usual text
    portion2 = slides.Portion()
    portion2.text = "a"
    paragraph2.portions.add(portion2)

    # Create portion with subscript text
    subPortion = slides.Portion()
    subPortion.portion_format.escapement = -25
    subPortion.text = "i"
    paragraph2.portions.add(subPortion)

    # Add paragraphs to text box
    textFrame.paragraphs.add(superPar)
    textFrame.paragraphs.add(paragraph2)

    presentation.save(outDir + "text_add_superscript_and_subscript_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddingSuperscriptAndSubscriptTextInTextFrame