import aspose.slides as slides


# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"


with slides.Presentation(dataDir + "text_add_animation_effect.pptx") as pres:
    shape = pres.slides[0].shapes[0]
    effectiveTextStyle = shape.text_frame.text_frame_format.text_style.get_effective()

    for i in range(9):
        effectiveStyleLevel = effectiveTextStyle.get_level(i)
        print("= Effective paragraph formatting for style level #" + str(i) + " =")

        print("depth: " + str(effectiveStyleLevel.depth))
        print("Indent: " + str(effectiveStyleLevel.indent))
        print("Alignment: " + str(effectiveStyleLevel.alignment))
        print("Font alignment: " + str(effectiveStyleLevel.font_alignment))