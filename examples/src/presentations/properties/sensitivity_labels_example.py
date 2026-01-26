import aspose.slides as slides
import uuid


def sensitivity_labels_example(global_opts):
    label1 = "{0372a796-4aa3-4c41-9a98-8232cac474f6}"
    label2 = "{c0c0bc41-48d8-4bf2-a038-8ec8c93813b5}"
    site_id = uuid.UUID("{c336d4c6-89ce-480c-beb0-3bfa5538f186}")

    with slides.Presentation(global_opts.data_dir + "OldSensitivitiLabels.pptx") as pres:
        # Get sensitivity labels from the custom document properties
        mip_sensitivity_labels = pres.document_properties.get_sensitivity_labels()
        sensitivity_labels = pres.sensitivity_labels
        for sensitivity_label in mip_sensitivity_labels:
            # Add label to the collection
            sensitivity_labels.add(sensitivity_label)

        # Add sensitivity labels
        label1 = sensitivity_labels.add(label1, site_id, True, slides.SensitivityLabelAssignmentType.STANDARD)
        label1.content_mark_types.append(slides.SensitivityLabelContentType.HEADER)
        label1.is_removed = True

        label2 = sensitivity_labels.add(label2, site_id, True, slides.SensitivityLabelAssignmentType.PRIVILEGED)
        label2.content_mark_types.append(slides.SensitivityLabelContentType.FOOTER)
        label2.content_mark_types.append(slides.SensitivityLabelContentType.WATERMARK)

        # Print sensitivity labels
        for sensitivity_label in sensitivity_labels:
            print("Label ID", sensitivity_label.id, "from site", sensitivity_label.site_id)

        pres.save(global_opts.out_dir + "SensitivityLabels_out.pptx", slides.export.SaveFormat.PPTX)
