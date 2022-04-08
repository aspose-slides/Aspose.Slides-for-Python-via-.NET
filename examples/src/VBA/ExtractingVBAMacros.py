import aspose.slides as slides


#ExStart:ExtractingVBAMacros

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "VBA.pptm") as pres:
    if pres.vba_project is not None: # check if Presentation contains VBA Project
        for module in pres.vba_project.modules:
            print(module.name)
            print(module.source_code)

#ExEnd:ExtractingVBAMacros
