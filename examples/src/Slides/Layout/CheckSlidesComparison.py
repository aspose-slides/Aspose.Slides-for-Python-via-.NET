import aspose.slides as slides


#ExStart:CheckSlidesComparison
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation1:
    with slides.Presentation(dataDir + "background.pptx") as presentation2:
        
        for i in range(len(presentation1.masters)):
            for j in range(len(presentation2.masters)):
                if (presentation1.masters[i] == presentation2.masters[j]):
                    print("SomePresentation1 MasterSlide#{0} is equal to SomePresentation2 MasterSlide#{1}".format(i, j))
#ExEnd:CheckSlidesComparison