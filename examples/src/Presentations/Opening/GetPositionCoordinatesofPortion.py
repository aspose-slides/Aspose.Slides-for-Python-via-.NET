import aspose.pydrawing as drawing
import aspose.slides as slides

def get_position_coordinates_of_portion():
    
    #ExStart:GetPositionCoordinatesofPortion
    # The path to the documents directory.
    dataDir = "./examples/data/"
    
    with slides.Presentation(dataDir + "open_shapes.pptx") as presentation:
        shape = presentation.slides[0].shapes[0]
        textFrame = shape.text_frame

        for paragraph in textFrame.paragraphs:
            for portion in paragraph.portions:
                point = portion.get_coordinates()
                print("Corrdinates X ={0} Corrdinates Y ={1}".format(point.x, point.y))
    #ExEnd:GetPositionCoordinatesofPortion

