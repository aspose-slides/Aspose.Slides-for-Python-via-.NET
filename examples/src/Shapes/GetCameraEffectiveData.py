import aspose.slides as slides

#ExStart:GetCameraEffectiveData

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "shapes_3d_effective.pptx") as pres:
    threeDEffectiveData = pres.slides[0].shapes[0].three_dformat.get_effective()

    print("= Effective camera properties =")
    print("Type: " + str(threeDEffectiveData.camera.camera_type))
    print("Field of view: " + str(threeDEffectiveData.camera.field_of_view_angle))
    print("Zoom: " + str(threeDEffectiveData.camera.zoom))

#ExEnd:GetCameraEffectiveData
