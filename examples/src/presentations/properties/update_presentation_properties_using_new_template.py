import aspose.slides as slides


def update_by_template(path, template):
    to_update = slides.PresentationFactory.instance.get_presentation_info(path)
    to_update.update_document_properties(template)
    to_update.write_binded_presentation(path)


def props_update_properties_using_template(global_opts):
    template = slides.DocumentProperties()
    template.author = "Template Author"
    template.title = "Template Title"
    template.category = "Template Category"
    template.keywords = "Keyword1, Keyword2, Keyword3"
    template.company = "Our Company"
    template.comments = "Created from template"
    template.content_type = "Template Content"
    template.subject = "Template Subject"

    update_by_template(global_opts.data_dir + "doc1.pptx", template)
    update_by_template(global_opts.data_dir + "doc2.odp", template)
    update_by_template(global_opts.data_dir + "doc3.ppt", template)
