import aspose.slides as slides

#ExStart:RemoveHyperlinks
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class
with slides.Presentation(dataDir + "hyperlink.pptx") as presentation:

    # Removing the hyperlinks from presentation
    presentation.hyperlink_queries.remove_all_hyperlinks()

    #Writing the presentation as a PPTX file
    presentation.save(outDir + "hyperlink_remove_all_hyperlinks_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:RemoveHyperlinks