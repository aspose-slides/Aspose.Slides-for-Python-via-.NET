import aspose.slides as slides
#ExStart:GetShapeBevelEffectiveData

# The path to the documents directory.
dataDir = "./examples/data/"

with slides.Presentation(dataDir + "shapes_3d_effective.pptx") as pres:
    threeDEffectiveData = pres.slides[0].shapes[0].three_dformat.get_effective()

    print("= Effective shape's top face relief properties =")
    print("Type: " + str(threeDEffectiveData.bevel_top.bevel_type))
    print("Width: " + str(threeDEffectiveData.bevel_top.width))
    print("Height: " + str(threeDEffectiveData.bevel_top.height))

#ExEnd:GetShapeBevelEffectiveData
