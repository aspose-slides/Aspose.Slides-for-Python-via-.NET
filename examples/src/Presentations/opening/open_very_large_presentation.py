import aspose.slides as slides


def open_very_large_presentation(global_opts):
    load_options = slides.LoadOptions()
    load_options.blob_management_options = slides.BlobManagementOptions()
    load_options.blob_management_options.presentation_locking_behavior = slides.PresentationLockingBehavior.KEEP_LOCKED

    with slides.Presentation(global_opts.data_dir + "large_presentation.pptx", load_options) as pres:
        # the huge presentation is loaded and ready to use, but the memory consumption is still low.

        # make any changes to the presentation.
        pres.slides[0].name = "Very large presentation"

        # presentation will be saved to the other file, the memory consumptions still low during saving.
        pres.save(global_opts.out_dir + "veryLargePresentation-copy.pptx", slides.export.SaveFormat.PPTX)
