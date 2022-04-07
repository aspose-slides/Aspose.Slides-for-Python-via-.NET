import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:RuleBasedFontsReplacement
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Load presentation
with slides.Presentation(dataDir + "text_fonts.pptx") as presentation:
    # Load source font to be replaced
    sourceFont = slides.FontData("SomeRareFont")

    # Load the replacing font
    destFont = slides.FontData("Arial")

    # Add font rule for font replacement
    fontSubstRule = slides.FontSubstRule(sourceFont, destFont, slides.FontSubstCondition.WHEN_INACCESSIBLE)

    # Add rule to font substitute rules collection
    fontSubstRuleCollection = slides.FontSubstRuleCollection()
    fontSubstRuleCollection.add(fontSubstRule)

    # Add font rule collection to rule list
    presentation.fonts_manager.font_subst_rule_list = fontSubstRuleCollection

    # Arial font will be used instead of SomeRareFont when inaccessible
    bmp = presentation.slides[0].get_thumbnail(1, 1)

    # Save the image to disk in JPEG format
    bmp.save(outDir + "text_rule_based_font_replacement_out.jpg", drawing.imaging.ImageFormat.jpeg)
#ExEnd:RuleBasedFontsReplacement