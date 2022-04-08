import aspose.slides as slides


#ExStart:ManageHeaderFooterText

def update_header_footer_text(master):
    for shape in master.shapes:
        if shape.placeholder is not None:
            if shape.placeholder.type == slides.PlaceholderType.HEADER:
                shape.text_frame.text = "HI there new header"

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Load Presentation
with slides.Presentation(dataDir + "layout_presentation.ppt") as pres:

    # Setting Footer
    pres.header_footer_manager.set_all_footers_text("My Footer text")
    pres.header_footer_manager.set_all_footers_visibility(True)

    # Access and Update Header
    masterNotesSlide = pres.master_notes_slide_manager.master_notes_slide
    if masterNotesSlide is not None:
        update_header_footer_text(masterNotesSlide)

    # Save presentation
    pres.save(outDir + "layout_update_header_footer_text_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:ManageHeaderFooterText
