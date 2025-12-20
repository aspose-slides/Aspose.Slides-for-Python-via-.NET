import aspose.slides as slides


def spell_check_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "SpellChecksExample.pptx") as pres:
        # Access the first portion of text inside the first shape on the first slide
        portion = pres.slides[0].shapes[0].text_frame.paragraphs[0].portions[0]

        # Read spell checking property
        print("SpellCheck is", portion.portion_format.spell_check)

        # Disable spell checking for this text portion
        portion.portion_format.spell_check = False

        # Save the modified presentation
        pres.save(global_opts.out_dir + "SpellChecksExample-out.pptx", slides.export.SaveFormat.PPTX)
