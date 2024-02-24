import aspose.slides as slides


def lock_aspect_ratio(global_opts):
    with slides.Presentation(global_opts.data_dir + "tables.pptx") as pres:
        table = pres.slides[0].shapes[0]
        print("Lock aspect ratio set: {0}".format(table.shape_lock.aspect_ratio_locked))

        table.shape_lock.aspect_ratio_locked = not table.shape_lock.aspect_ratio_locked  # invert

        print("Lock aspect ratio set: {0}".format(table.shape_lock.aspect_ratio_locked))

        pres.save(global_opts.out_dir + "tables_pres_lock_aspect_ratio_out.pptx", slides.export.SaveFormat.PPTX)
