import aspose.slides as slides

def props_check_presentation_protection():
    #Path for source presentation
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Check the Write Protection Password via IPresentationInfo Interface
    presentationInfo = slides.PresentationFactory.instance.get_presentation_info(dataDir + "props_check_presentation_protection.pptx")
    isWriteProtectedByPassword = presentationInfo.is_write_protected == 1 and presentationInfo.check_write_protection("pass2")
    print("Is presentation write protected by password = " + str(isWriteProtectedByPassword))

    # Check the Write Protection Password via IProtectionManager Interface
    with slides.Presentation(dataDir + "props_check_presentation_protection.pptx") as presentation:
        isWriteProtected = presentation.protection_manager.check_write_protection("pass2")
        print("Is presentation write protected = " + str(isWriteProtected))

    # Check Presentation Open Protection via IPresentationInfo Interface
    presentationInfo = slides.PresentationFactory.instance.get_presentation_info(dataDir + "props_ppt_with_password.ppt")
    if presentationInfo.is_password_protected:
        print("The presentation 'props_ppt_with_password.ppt' is protected by password to open.")
