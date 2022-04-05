import aspose.slides as slides

#ExStart:UpdatePresentationPropertiesUsingNewTemplate
def update_by_template(path, template):
    toUpdate = slides.PresentationFactory.instance.get_presentation_info(path)
    toUpdate.update_document_properties(template)
    toUpdate.write_binded_presentation(path)

def props_update_properties_using_template():
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    template = slides.DocumentProperties()
    template.author = "Template Author"
    template.title = "Template Title"
    template.category = "Template Category"
    template.keywords = "Keyword1, Keyword2, Keyword3"
    template.company = "Our Company"
    template.comments = "Created from template"
    template.content_type = "Template Content"
    template.subject = "Template Subject"

    update_by_template(dataDir + "doc1.pptx", template)
    update_by_template(dataDir + "doc2.odp", template)
    update_by_template(dataDir + "doc3.ppt", template)
#ExEnd:UpdatePresentationPropertiesUsingNewTemplate