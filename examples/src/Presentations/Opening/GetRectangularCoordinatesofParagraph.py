import aspose.pydrawing as drawing
import aspose.slides as slides

def get_rectangular_coordinates_of_paragraph():
    #ExStart:GetRectangularCoordinatesofParagraph
    # The path to the documents directory.
    dataDir = "./examples/data/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "Shapes.pptx") as presentation:
        shape = presentation.slides[0].shapes[0]
        textFrame = shape.text_frame
        rect = textFrame.paragraphs[0].get_rect()
    #ExEnd:GetRectangularCoordinatesofParagraph
    return rect


 