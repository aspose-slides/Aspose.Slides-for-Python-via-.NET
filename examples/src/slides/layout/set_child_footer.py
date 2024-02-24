import aspose.slides as slides


def set_child_footer(global_opts):
    with slides.Presentation(global_opts.data_dir + "layout_presentation.ppt") as presentation:
        header_footer_manager = presentation.masters[0].header_footer_manager
        header_footer_manager.set_footer_and_child_footers_visibility(True)
        # Method set_footer_and_child_footers_visibility is used
        # for making a master slide and all child footer placeholders visible.
        header_footer_manager.set_slide_number_and_child_slide_numbers_visibility(True)
        # Method set_slide_number_and_child_slide_numbers_visibility is used
        # for making a master slide and all child page number placeholders visible.
        header_footer_manager.set_date_time_and_child_date_times_visibility(True)
        # Method set_date_time_and_child_date_times_visibility is used
        # for making a master slide and all child date-time placeholders visible.

        header_footer_manager.set_footer_and_child_footers_text("Footer text")
        # Method set_footer_and_child_footers_text is used
        # for setting text to master slide and all child footer placeholders.
        header_footer_manager.set_date_time_and_child_date_times_text("Date and time text")
        # Method set_date_time_and_child_date_times_text is used
        # for setting text to master slide and all child date-time placeholders.
