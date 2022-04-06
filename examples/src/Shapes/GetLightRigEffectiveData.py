import aspose.slides as slides
            
#ExStart:GetLightRigEffectiveData

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "shapes_3d_effective.pptx") as pres:
    threeDEffectiveData = pres.slides[0].shapes[0].three_dformat.get_effective()

    print("= Effective light rig properties =")
    print("Type: " + str(threeDEffectiveData.light_rig.light_type))
    print("Direction: " + str(threeDEffectiveData.light_rig.direction))

#ExEnd:GetLightRigEffectiveData
