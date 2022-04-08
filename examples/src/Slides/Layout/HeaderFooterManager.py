import aspose.slides as slides


#ExStart:HeaderFooterManager
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"
with slides.Presentation(dataDir + "layout_presentation.ppt") as presentation:
    headerFooterManager = presentation.slides[0].header_footer_manager
    if not headerFooterManager.is_footer_visible: # Property is_footer_visible is used for indicating that a slide footer placeholder is not present.
        headerFooterManager.set_footer_visibility(True) # Method set_footer_visibility is used for making a slide footer placeholder visible.
    if not headerFooterManager.is_slide_number_visible: # Property is_slide_number_visible is used for indicating that a slide page number placeholder is not present.
        headerFooterManager.set_slide_number_visibility(True) # Method set_slide_number_visibility is used for making a slide page number placeholder visible.
    if not headerFooterManager.is_date_time_visible: # Property is_date_time_visible is used for indicating that a slide date-time placeholder is not present.
        headerFooterManager.set_date_time_visibility(True) # Method set_footer_visibility is used for making a slide date-time placeholder visible.
    headerFooterManager.set_footer_text("Footer text") # Method set_footer_text is used for setting text to slide footer placeholder.
    headerFooterManager.set_date_time_text("Date and time text") # Method set_date_time_text is used for setting text to slide date-time placeholder.



    presentation.save(outDir + "layout_header_footer_manager_out.ppt", slides.export.SaveFormat.PPT)
#ExEnd:HeaderFooterManager