import aspose.slides as slides


#ExStart:CustomChildNodesInSmartArt
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Load the desired the presentation
with slides.Presentation(dataDir + "smart_art_access.pptx") as pres:
	smart = pres.slides[0].shapes.add_smart_art(20, 20, 600, 500, slides.smartart.SmartArtLayoutType.ORGANIZATION_CHART)

	# Move SmartArt shape to new position
	node = smart.all_nodes[1]
	shape = node.shapes[1]
	shape.x += (shape.width * 2)
	shape.y -= (shape.height / 2)

	# Change SmartArt shape's widths
	node = smart.all_nodes[2]
	shape = node.shapes[1]
	shape.width += (shape.width / 2)

	# Change SmartArt shape's height
	node = smart.all_nodes[3]
	shape = node.shapes[1]
	shape.height += (shape.height / 2)

	# Change SmartArt shape's rotation
	node = smart.all_nodes[4]
	shape = node.shapes[1]
	shape.rotation = 90

	pres.save(outDir + "smart_art_custom_child_nodes_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:CustomChildNodesInSmartArt
		
	
