import aspose.slides as slides


def section_collection(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        section = pres.sections[2]
        pres.sections.reorder_section_with_slides(section, 0)
        pres.sections.remove_section_with_slides(pres.sections[0])
        pres.sections.append_empty_section("Last empty section")
        pres.sections.add_section("First empty", pres.slides[7])
        pres.sections[0].name = "New section name"
        pres.save(global_opts.out_dir + "crud_sections_out.pptx", slides.export.SaveFormat.PPTX)
