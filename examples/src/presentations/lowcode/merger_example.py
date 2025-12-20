import aspose.slides as slides


def merger_example(global_opts):
    slides.lowcode.Merger.process([
        global_opts.data_dir + "ForEachPortion.pptx",
        global_opts.data_dir + "ConvertExample.pptx",
        global_opts.data_dir + "MultipleMaster.pptx",
    ], global_opts.out_dir + "Merged-out.pptx")
