﻿import aspose.pydrawing as drawing
using System.Drawing.Imaging
using Aspose.slides.SmartArt
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    class CreateSmartArtChildNoteThumbnail
    {
        public static void Run()
        {
            #ExStart:CreateSmartArtChildNoteThumbnail
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Instantiate Presentation class that represents the PPTX file 
            with slides.Presentation() as pres:

            # Add SmartArt 
            ISmartArt smart = pres.slides[0].shapes.AddSmartArt(10, 10, 400, 300, SmartArtLayoutType.BasicCycle)

            # Obtain the reference of a node by using its Index  
            ISmartArtNode node = smart.Nodes[1]

            # Get thumbnail
            bmp = node.shapes[0].GetThumbnail()

            # Save thumbnail
            bmp.save(dataDir + "SmartArt_ChildNote_Thumbnail_out.jpeg", ImageFormat.Jpeg)
            #ExEnd:CreateSmartArtChildNoteThumbnail
        }
    }
}



