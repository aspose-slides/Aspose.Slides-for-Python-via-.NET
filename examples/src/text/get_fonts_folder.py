import aspose.slides as slides


def get_fonts_folder():
    # The following line shall return folders where font files are searched.
    # Those are folders that have been added with LoadExternalFonts method as well as system font folders.
    font_folders = slides.FontsLoader.get_font_folders()

    print("Font folders:")
    for font_folder in font_folders:
        print(font_folder)
