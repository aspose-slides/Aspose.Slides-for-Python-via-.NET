import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:CreateSmartArtChildNoteThumbnail
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the PPTX file 
with slides.Presentation() as pres:
    # Add SmartArt 
    smart = pres.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.BASIC_CYCLE)

    # Obtain the reference of a node by using its Index  
    node = smart.nodes[1]

    # Get thumbnail
    bmp = node.shapes[0].get_thumbnail()

    # Save thumbnail
    bmp.save(outDir + "shapes_create_smartart_thumbnail_out.jpeg", drawing.imaging.ImageFormat.jpeg)
#ExEnd:CreateSmartArtChildNoteThumbnail
