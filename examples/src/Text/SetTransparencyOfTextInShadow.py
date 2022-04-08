import aspose.slides as slides
import aspose.pydrawing as drawing
#ExStart:SetTransparencyOfTextInShadow
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "text_transparency.pptx") as pres:
    shape = pres.slides[0].shapes[0]
    effects = shape.text_frame.paragraphs[0].portions[0].portion_format.effect_format

    outerShadowEffect = effects.outer_shadow_effect

    shadowColor = outerShadowEffect.shadow_color.color
    print("{0} - transparency is: {1}".format(shadowColor, (shadowColor.a / 255) * 100))

    # set transparency to zero percent
    outerShadowEffect.shadow_color.color = drawing.Color.from_argb(255, shadowColor)

    pres.save(outDir + "text_transparency_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SetTransparencyOfTextInShadow
