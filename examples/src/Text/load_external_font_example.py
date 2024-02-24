import aspose.slides as slides


def load_external_font_example(global_opts):
    # loading presentation uses SomeFont which is not installed on the system
    with slides.Presentation() as pres:
        # load SomeFont from file into the byte array

        with open(global_opts.data_dir + "CustomFonts.ttf", "rb") as fs:
            font_data = fs.read()

        # load font represented as byte array
        slides.FontsLoader.load_external_font(font_data)
