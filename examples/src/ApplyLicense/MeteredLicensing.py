import aspose.slides as slides

def apply_metered_licensing():
    #ExStart:MeteredLicensing

    # Create an instance of Metered class
    metered = slides.Metered()

    # Access the setMeteredKey property and pass public and private keys as parameters
    metered.set_metered_key("*****", "*****")

    # Get metered data amount before calling API
    amountbefore = slides.Metered.get_consumption_quantity()

    # Display information
    print("Amount Consumed Before: " + str(amountbefore))
    # Get metered data amount After calling API
    amountafter = slides.Metered.get_consumption_quantity()

    # Display information
    print("Amount Consumed After: " + str(amountafter))

    #ExEnd:MeteredLicensing
