import aspose.slides as slides


# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

#ExStart:RemoveVBAMacros
# Instantiate Presentation
with slides.Presentation(dataDir + "VBA.pptm") as presentation:
    # Access the Vba module and remove 
    presentation.vba_project.modules.remove(presentation.vba_project.modules[0])

    # Save Presentation
    presentation.save(outDir + "vba_RemovedVBAMacros_out.pptm", slides.export.SaveFormat.PPTM)
#ExEnd:RemoveVBAMacros