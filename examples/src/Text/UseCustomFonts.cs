using System
using Aspose.slides.Export
using Aspose.slides.Charts
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.text
{
    class UseCustomFonts
    {
        public static void Run()
        {
            #ExStart:UseCustomFonts
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # folders to seek fonts
            String[] folders = new String[] { dataDir }

            # Load the custom font directory fonts
            FontsLoader.LoadExternalFonts(folders)

            # Do Some work and perform presentation/slides rendering
            using (Presentation presentation = new Presentation(dataDir + "DefaultFonts.pptx"))
                presentation.save(dataDir + "NewFonts_out.pptx", slides.export.SaveFormat.PPTX)

            # Clear Font Cachce
            FontsLoader.ClearCache()
            #ExEnd:UseCustomFonts
        }
    }
}
