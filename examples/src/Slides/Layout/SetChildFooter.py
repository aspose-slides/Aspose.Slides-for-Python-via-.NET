import aspose.slides as slides


#ExStart:SetChildFooter
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"
with slides.Presentation(dataDir + "layout_presentation.ppt") as presentation:
    headerFooterManager = presentation.masters[0].header_footer_manager
    headerFooterManager.set_footer_and_child_footers_visibility(True) # Method set_footer_and_child_footers_visibility is used for making a master slide and all child footer placeholders visible.
    headerFooterManager.set_slide_number_and_child_slide_numbers_visibility(True) # Method set_slide_number_and_child_slide_numbers_visibility is used for making a master slide and all child page number placeholders visible.
    headerFooterManager.set_date_time_and_child_date_times_visibility(True) # Method set_date_time_and_child_date_times_visibility is used for making a master slide and all child date-time placeholders visible.

    headerFooterManager.set_footer_and_child_footers_text("Footer text") # Method set_footer_and_child_footers_text is used for setting text to master slide and all child footer placeholders.
    headerFooterManager.set_date_time_and_child_date_times_text("Date and time text") # Method set_date_time_and_child_date_times_text is used for setting text to master slide and all child date-time placeholders.

#ExEnd:SetChildFooter