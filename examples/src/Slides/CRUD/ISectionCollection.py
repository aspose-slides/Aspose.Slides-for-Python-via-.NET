import aspose.slides as slides


#ExStart:ISectionCollection
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    section = pres.sections[2]
    pres.sections.reorder_section_with_slides(section, 0)
    pres.sections.remove_section_with_slides(pres.sections[0])
    pres.sections.append_empty_section("Last empty section")
    pres.sections.add_section("First empty", pres.slides[7])
    pres.sections[0].name = "New section name"
    pres.save(outDir + "crud_sections_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ISectionCollection
