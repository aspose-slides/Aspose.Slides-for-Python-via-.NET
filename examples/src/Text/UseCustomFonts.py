import aspose.slides as slides

#ExStart:UseCustomFonts
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# folders to seek fonts
folders =  [dataDir ]

# Load the custom font directory fonts
slides.FontsLoader.load_external_fonts(folders)

# Do Some work and perform presentation/slides rendering
with slides.Presentation(dataDir + "text_default_fonts.pptx") as presentation:
    presentation.save(outDir + "text_load_external_fonts_out.pptx", slides.export.SaveFormat.PPTX)

# Clear Font Cachce
slides.FontsLoader.clear_cache()
#ExEnd:UseCustomFonts
