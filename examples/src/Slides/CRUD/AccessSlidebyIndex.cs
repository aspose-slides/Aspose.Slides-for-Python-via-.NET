﻿import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.CRUD
{
    class AccessSlidebyIndex
    {
        public static void Run()
        {
            #ExStart:AccessSlidebyIndex
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_CRUD()

            # Create an instance of Presentation class
            Presentation presentation = new Presentation(dataDir + "AccessSlides.pptx")

            # Obtain a slide's reference by its index
            slide = presentation.slides[0]
            #ExEnd:AccessSlidebyIndex           
        }
    }
}