import aspose.slides as slides


#ExStart:GetFontsFolders

#The following line shall return folders where font files are searched.
#Those are folders that have been added with LoadExternalFonts method as well as system font folders.
fontFolders = slides.FontsLoader.get_font_folders()

#ExEnd:GetFontsFolders
