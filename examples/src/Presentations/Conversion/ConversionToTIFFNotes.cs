﻿using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Presentations.Conversion
{
    class ConversionToTIFFNotes
    {
        public static void Run()
        {
            #ExStart:ConversionToTIFFNotes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Conversion()

            # Instantiate a Presentation object that represents a presentation file
            using (Presentation presentation = new Presentation(dataDir + "NotesFile.pptx"))
            {
                # Saving the presentation to TIFF notes
                presentation.save(dataDir + "Notes_In_Tiff_out.tiff", SaveFormat.Tiff)
            }
            #ExEnd:ConversionToTIFFNotes
        } 
    }
}

 