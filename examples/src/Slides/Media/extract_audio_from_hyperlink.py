import aspose.slides as slides


def extract_audio_from_hyperlink(global_opts):
    with slides.Presentation(global_opts.data_dir + "HyperlinkSound.pptx") as pres:
        # Gets the first shape hyperlink
        link = pres.slides[0].shapes[0].hyperlink_click

        if link.sound is not None:
            # Extracts the hyperlink sound in byte array
            audio_data = link.sound.binary_data

            # Saves effect sound to media file
            open(global_opts.out_dir + "HyperlinkSound.mpg", "wb").write(audio_data)
