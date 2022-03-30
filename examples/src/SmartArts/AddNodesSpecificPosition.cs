
using System.IO

import aspose.slides as slides
using Aspose.slides.SmartArt

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    public class AddNodesSpecificPosition
    {
        public static void Run()
        {
            #ExStart:AddNodesSpecificPosition
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Creating a presentation instance
            with slides.Presentation() as pres:

            # Access the presentation slide
            slide = pres.slides[0]

            # Add Smart Art IShape
            ISmartArt smart = slide.shapes.AddSmartArt(0, 0, 400, 400, SmartArtLayoutType.StackedList)

            # Accessing the SmartArt node at index 0
            ISmartArtNode node = smart.AllNodes[0]

            # Adding new child node at position 2 in parent node
            SmartArtNode chNode = (SmartArtNode)((SmartArtNodeCollection)node.ChildNodes).AddNodeByPosition(2)

            # Add Text
            chNode.text_frame.text = "Sample Text Added"

            # Save Presentation
            pres.save(dataDir + "AddSmartArtNodeByPosition_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:AddNodesSpecificPosition
        }
    }
}