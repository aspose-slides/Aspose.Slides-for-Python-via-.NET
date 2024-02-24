import aspose.slides as slides


def header_and_footer_in_notes_slide(global_opts):
	with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
		# Change Header and Footer settings for notes master and all notes slides
		master_notes_slide = presentation.master_notes_slide_manager.master_notes_slide
		if master_notes_slide is not None:
			header_footer_manager = master_notes_slide.header_footer_manager

			header_footer_manager.set_header_and_child_headers_visibility(True)
			# make the master notes slide and all child Footer placeholders visible
			header_footer_manager.set_footer_and_child_footers_visibility(True)
			# make the master notes slide and all child Header placeholders visible
			header_footer_manager.set_slide_number_and_child_slide_numbers_visibility(True)
			# make the master notes slide and all child SlideNumber placeholders visible
			header_footer_manager.set_date_time_and_child_date_times_visibility(True)
			# make the master notes slide and all child Date and time placeholders visible

			header_footer_manager.set_header_and_child_headers_text("Header text")
			# set text to master notes slide and all child Header placeholders
			header_footer_manager.set_footer_and_child_footers_text("Footer text")
			# set text to master notes slide and all child Footer placeholders
			header_footer_manager.set_date_time_and_child_date_times_text("Date and time text")
			# set text to master notes slide and all child Date and time placeholders

		# Change Header and Footer settings for first notes slide only
		notes_slide = presentation.slides[0].notes_slide_manager.notes_slide
		if notes_slide is not None:
			header_footer_manager = notes_slide.header_footer_manager
			if not header_footer_manager.is_header_visible:
				header_footer_manager.set_header_visibility(True)
				# make this notes slide Header placeholder visible

			if not header_footer_manager.is_footer_visible:
				header_footer_manager.set_footer_visibility(True)
				# make this notes slide Footer placeholder visible

			if not header_footer_manager.is_slide_number_visible:
				header_footer_manager.set_slide_number_visibility(True)
				# make this notes slide SlideNumber placeholder visible

			if header_footer_manager.is_date_time_visible:
				header_footer_manager.set_date_time_visibility(True)
				# make this notes slide Date-time placeholder visible

			header_footer_manager.set_header_text("New header text")
			# set text to notes slide Header placeholder
			header_footer_manager.set_footer_text("New footer text")
			# set text to notes slide Footer placeholder
			header_footer_manager.set_date_time_text("New date and time text")
			# set text to notes slide Date-time placeholder

		presentation.save(global_opts.out_dir + "notes_HeaderAndFooterInNotesSlide_out.pptx",slides.export.SaveFormat.PPTX)
