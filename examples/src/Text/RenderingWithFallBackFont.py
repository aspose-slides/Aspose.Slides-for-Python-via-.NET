import aspose.slides as slides
import aspose.pydrawing as drawing


#ExStart:RenderingWithFallBackFont

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create new instance of a rules collection
rulesList = slides.FontFallBackRulesCollection()

# create a number of rules
rulesList.add(slides.FontFallBackRule(0x400, 0x4FF, "Times New Roman"))
#rulesList.add(slides.FontFallBackRule(...))

for fallBackRule in rulesList:
    #Trying to remove FallBack font "Tahoma" from loaded rules
    fallBackRule.remove("Tahoma")

    #And to update of rules for specified range
    if fallBackRule.range_end_index >= 0x4000 and fallBackRule.range_start_index < 0x5000:
        fallBackRule.add_fallBack_fonts("Verdana")

#Also we can remove any existing rules from list
if len(rulesList) > 0:
    rulesList.remove(rulesList[0])

with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    #Assigning a prepared rules list for using
    pres.fonts_manager.font_fall_back_rules_collection = rulesList

    # Rendering of thumbnail with using of initialized rules collection and saving to PNG
    pres.slides[0].get_thumbnail(1, 1).save(outDir + "text_font_fall_back_out.png", drawing.imaging.ImageFormat.png)
#ExEnd:RenderingWithFallBackFont