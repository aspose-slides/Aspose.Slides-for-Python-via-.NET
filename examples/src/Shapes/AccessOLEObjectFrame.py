import aspose.slides as slides


def shapes_accessing_ole_object_frame():
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Load the PPTX to Presentation object
    with slides.Presentation(dataDir + "shapes_accessing_ole_object_frame.pptx") as pres:
        # Access the first slide
        sld = pres.slides[0]

        # Cast the shape to OleObjectFrame
        oleObjectFrame = sld.shapes[0]

        # Read the OLE Object and write it to disk
        if type(oleObjectFrame) is slides.OleObjectFrame:
            # Get embedded file data
            data = oleObjectFrame.embedded_data.embedded_file_data

            # Get embedded file extention
            fileExtention = oleObjectFrame.embedded_data.embedded_file_extension

            # Create a path to save the extracted file
            extractedPath = "excelFromOLE_out" + fileExtention

            # Save extracted data
            with open(outDir + "shapes_accessing_ole_object_frame_out.xlsx", "wb") as fs:
                fs.write(data)