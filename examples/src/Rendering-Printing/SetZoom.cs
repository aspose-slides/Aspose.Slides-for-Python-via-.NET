﻿using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Rendering.Printing
{
    class SetZoom
    {
        public static void Run()
        {
            #ExStart:SetZoom
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Rendering()

            # Instantiate a Presentation object that represents a presentation file
            with slides.Presentation() as presentation:
            {
                # Setting View Properties of Presentation

                presentation.ViewProperties.SlideViewProperties.Scale = 100 # Zoom value in percentages for slide view
                presentation.ViewProperties.NotesViewProperties.Scale = 100 # Zoom value in percentages for notes view 

                presentation.save(dataDir + "Zoom_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SetZoom
        }
    }
}

