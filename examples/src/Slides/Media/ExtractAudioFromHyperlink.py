import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def extract_audio_from_hyper_link():
    pptx_file = dataDir + "HyperlinkSound.pptx"
    out_media_path = outDir + "HyperlinkSound.mpg"

    with slides.Presentation(pptx_file) as pres:
        # Gets the first shape hyperlink
        link = pres.slides[0].shapes[0].hyperlink_click

        if link.sound is not None:
            # Extracts the hyperlink sound in byte array
            audio_data = link.sound.binary_data

            # Saves effect sound to media file
            open(out_media_path, "wb").write(audio_data)
