import aspose.slides as slides


def extended_presentation_properties(global_opts):
    result_path = global_opts.out_dir + "ExtendDocumentProperies-out1.pptx"
    with slides.Presentation(global_opts.data_dir + "ExtendDocumentProperies.pptx") as presentation:
        document_properties = presentation.document_properties

        # Print the read-only properties
        print("Slides:", document_properties.slides)
        print("HiddenSlides:", document_properties.hidden_slides)
        print("Notes:", document_properties.notes)
        print("Paragraphs:", document_properties.paragraphs)
        print("MultimediaClips:", document_properties.multimedia_clips)
        print("TitlesOfParts:", '; '.join(document_properties.titles_of_parts))
        print("HeadingPairs:")
        heading_pairs = document_properties.heading_pairs
        if len(heading_pairs) > 0:
            for heading_pair in heading_pairs:
                print(heading_pair.name + " " + str(heading_pair.count))

        # Change several boolean properties
        document_properties.scale_crop = True
        document_properties.links_up_to_date = True

        # Save the presentation with changed properties
        presentation.save(result_path, slides.export.SaveFormat.PPTX)

        # Use the IPresentationInfo interface to read and change the document properties
        print("\nProperties obtained by IPresentationInfo:\n")

        document_info = slides.PresentationFactory.instance.get_presentation_info(result_path)
        document_properties = document_info.read_document_properties()

        # Print the read-only properties
        print("Slides:", document_properties.slides)
        print("HiddenSlides:", document_properties.hidden_slides)
        print("Notes:", document_properties.notes)
        print("Paragraphs:", document_properties.paragraphs)
        print("MultimediaClips:", document_properties.multimedia_clips)
        print("TitlesOfParts:", '; '.join(document_properties.titles_of_parts))
        print("HeadingPairs:")
        heading_pairs = document_properties.heading_pairs
        if len(heading_pairs) > 0:
            for heading_pair in heading_pairs:
                print(heading_pair.name + " " + str(heading_pair.count))

        # Change boolean property
        document_properties.hyperlinks_changed = True

        # Save the presentation with changed properties
        document_info.update_document_properties(document_properties)
        document_info.write_binded_presentation(result_path)
