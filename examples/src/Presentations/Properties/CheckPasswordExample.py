import aspose.slides as slides

def props_check_password():
    # The example below demonstrates how to check a password to open a presentation
    #Path for source presentation
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Check the Password via IPresentationInfo Interface
    presentationInfo = slides.PresentationFactory.instance.get_presentation_info(dataDir + "props_ppt_with_password.ppt")
    isPasswordCorrect = presentationInfo.check_password("my_password")
    print("The password \"my_password\" for the presentation is " + str(isPasswordCorrect))
    
    isPasswordCorrect = presentationInfo.check_password("pass1")
    print("The password \"pass1\" for the presentation is " + str(isPasswordCorrect))
