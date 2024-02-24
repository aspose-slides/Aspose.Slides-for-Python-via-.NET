import aspose.slides as slides


def organize_chart_layout_type(global_opts):
    with slides.Presentation() as presentation:
        # Add SmartArt BasicProcess
        smart = presentation.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.ORGANIZATION_CHART)

        # Get or Set the organization chart type
        smart.nodes[0].organization_chart_layout = slides.smartart.OrganizationChartLayoutType.LEFT_HANGING

        # Saving Presentation
        presentation.save(global_opts.out_dir + "smart_art_organization_chart_layout_out.pptx", slides.export.SaveFormat.PPTX)

