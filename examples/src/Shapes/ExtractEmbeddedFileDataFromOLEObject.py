import aspose.slides as slides


#ExStart:ExtractEmbeddedFileDataFromOLEObject
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "shapes_ole_objects.pptx") as pres:
    objectnum = 0
    for slide in pres.slides:
        for shape in slide.shapes:
            if type(shape) is slides.OleObjectFrame:
                objectnum += 1
                data = shape.embedded_data.embedded_file_data
                extension = shape.embedded_data.embedded_file_extension
                
                with open(outDir + "shapes_ole_objects{idx}_out{ex}".format(idx = str(objectnum), ex = extension), "wb") as fs:
                    fs.write(data)

#ExEnd:ExtractEmbeddedFileDataFromOLEObject