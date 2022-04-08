import aspose.slides as slides


# ExStart:GetTextFromSmartArtNode
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "smart_art_access.pptx") as presentation:
    slide = presentation.slides[0]
    smartArt = slide.shapes[0]

    smartArtNodes = smartArt.all_nodes
    for smartArtNode in smartArtNodes:
        for nodeShape in smartArtNode.shapes:
            if nodeShape.text_frame is not None:
                print(nodeShape.text_frame.text)
# ExEnd:GetTextFromSmartArtNode