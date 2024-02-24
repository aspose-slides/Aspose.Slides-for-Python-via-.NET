import aspose.slides as slides


def update_header_footer_text(master):
    for shape in master.shapes:
        if shape.placeholder is not None:
            if shape.placeholder.type == slides.PlaceholderType.HEADER:
                shape.text_frame.text = "HI there new header"


def manage_header_footer_text(global_opts):
    # Load Presentation
    with slides.Presentation(global_opts.data_dir + "layout_presentation.ppt") as pres:
        # Setting Footer
        pres.header_footer_manager.set_all_footers_text("My Footer text")
        pres.header_footer_manager.set_all_footers_visibility(True)

        # Access and Update Header
        master_notes_slide = pres.master_notes_slide_manager.master_notes_slide
        if master_notes_slide is not None:
            update_header_footer_text(master_notes_slide)

        # Save presentation
        pres.save(global_opts.out_dir + "layout_update_header_footer_text_out.pptx", slides.export.SaveFormat.PPTX)
