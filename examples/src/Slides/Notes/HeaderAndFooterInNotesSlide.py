import aspose.slides as slides


#ExStart:HeaderAndFooterInNotesSlide
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
	# Change Header and Footer settings for notes master and all notes slides
	masterNotesSlide = presentation.master_notes_slide_manager.master_notes_slide
	if masterNotesSlide is not None:
		headerFooterManager = masterNotesSlide.header_footer_manager

		headerFooterManager.set_header_and_child_headers_visibility(True) # make the master notes slide and all child Footer placeholders visible
		headerFooterManager.set_footer_and_child_footers_visibility(True) # make the master notes slide and all child Header placeholders visible
		headerFooterManager.set_slide_number_and_child_slide_numbers_visibility(True) # make the master notes slide and all child SlideNumber placeholders visible
		headerFooterManager.set_date_time_and_child_date_times_visibility(True) # make the master notes slide and all child Date and time placeholders visible

		headerFooterManager.set_header_and_child_headers_text("Header text") # set text to master notes slide and all child Header placeholders
		headerFooterManager.set_footer_and_child_footers_text("Footer text") # set text to master notes slide and all child Footer placeholders
		headerFooterManager.set_date_time_and_child_date_times_text("Date and time text") # set text to master notes slide and all child Date and time placeholders

	# Change Header and Footer settings for first notes slide only
	notesSlide = presentation.slides[0].notes_slide_manager.notes_slide
	if notesSlide is not None:
		headerFooterManager = notesSlide.header_footer_manager
		if not headerFooterManager.is_header_visible:
			headerFooterManager.set_header_visibility(True) # make this notes slide Header placeholder visible

		if not headerFooterManager.is_footer_visible:
			headerFooterManager.set_footer_visibility(True) # make this notes slide Footer placeholder visible

		if not headerFooterManager.is_slide_number_visible:
			headerFooterManager.set_slide_number_visibility(True) # make this notes slide SlideNumber placeholder visible

		if headerFooterManager.is_date_time_visible:
			headerFooterManager.set_date_time_visibility(True) # make this notes slide Date-time placeholder visible

		headerFooterManager.set_header_text("New header text") # set text to notes slide Header placeholder
		headerFooterManager.set_footer_text("New footer text") # set text to notes slide Footer placeholder
		headerFooterManager.set_date_time_text("New date and time text") # set text to notes slide Date-time placeholder
	presentation.save(outDir + "notes_HeaderAndFooterInNotesSlide_out.pptx",slides.export.SaveFormat.PPTX)

#ExEnd:HeaderAndFooterInNotesSlide