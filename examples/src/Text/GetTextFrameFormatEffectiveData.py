import aspose.slides as slides


#ExStart:GetTextFrameFormatEffectiveData

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "text_add_animation_effect.pptx") as pres:
    shape = pres.slides[0].shapes[0]

    textFrameFormat = shape.text_frame.text_frame_format
    effectiveTextFrameFormat = textFrameFormat.get_effective()


    print("Anchoring type: " + str(effectiveTextFrameFormat.anchoring_type))
    print("Autofit type: " + str(effectiveTextFrameFormat.autofit_type))
    print("Text vertical type: " + str(effectiveTextFrameFormat.text_vertical_type))
    print("Margins")
    print("   Left: " + str(effectiveTextFrameFormat.margin_left))
    print("   Top: " + str(effectiveTextFrameFormat.margin_top))
    print("   Right: " + str(effectiveTextFrameFormat.margin_right))
    print("   Bottom: " + str(effectiveTextFrameFormat.margin_bottom))
#ExEnd:GetTextFrameFormatEffectiveData
