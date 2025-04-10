import aspose.slides as slides


def apply_metered_licensing():
    # Create an instance of Metered class
    metered = slides.Metered()

    # Access the setMeteredKey property and pass public and private keys as parameters
    metered.set_metered_key("*****", "*****")

    # Get metered data amount before calling API
    amount_before = slides.Metered.get_consumption_quantity()

    # Display information
    print("Amount Consumed Before: " + str(amount_before))
    # Get metered data amount After calling API
    amount_after = slides.Metered.get_consumption_quantity()

    # Display information
    print("Amount Consumed After: " + str(amount_after))

    # Print status of a Metered license.
    print("Is metered license accepted: " + str(metered.is_metered_licensed()))
