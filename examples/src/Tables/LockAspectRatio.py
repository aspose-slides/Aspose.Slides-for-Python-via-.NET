import aspose.slides as slides

#ExStart:LockAspectRatio
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "tables.pptx") as pres:
    table = pres.slides[0].shapes[0]
    print("Lock aspect ratio set: {0}".format(table.shape_lock.aspect_ratio_locked))

    table.shape_lock.aspect_ratio_locked = not table.shape_lock.aspect_ratio_locked # invert

    print("Lock aspect ratio set: {0}".format(table.shape_lock.aspect_ratio_locked))

    pres.save(outDir + "tables_pres_lock_aspect_ratio_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:LockAspectRatio
