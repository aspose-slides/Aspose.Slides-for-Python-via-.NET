import aspose.slides as slides


#ExStart:AddNotesSlideWithNotesStyle
# The path to the documents directory.
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create an instance of Presentation class
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
    notesMaster = presentation.master_notes_slide_manager.master_notes_slide

    if notesMaster is not None:
        # Get MasterNotesSlide text style
        notesStyle = notesMaster.notes_style

        #Set symbol bullet for the first level paragraphs
        paragraphFormat = notesStyle.get_level(0)
        paragraphFormat.bullet.type = slides.BulletType.SYMBOL

    # Save the PPTX file to the Disk
    presentation.save(outDir + "crud_AddNotesSlideWithNotesStyle_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddNotesSlideWithNotesStyle


