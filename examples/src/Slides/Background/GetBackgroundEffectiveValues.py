import aspose.slides as slides

#ExStart:GetBackgroundEffectiveValues
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate the Presentation class that represents the presentation file
with slides.Presentation(dataDir + "background.pptx") as pres:

    effBackground = pres.slides[0].background.get_effective()

    if effBackground.fill_format.fill_type == slides.FillType.SOLID:
        print("Fill color: " + str(effBackground.fill_format.solid_fill_color))
    else:
        print("Fill type: " + str(effBackground.fill_format.fill_type))

#ExEnd:GetBackgroundEffectiveValues