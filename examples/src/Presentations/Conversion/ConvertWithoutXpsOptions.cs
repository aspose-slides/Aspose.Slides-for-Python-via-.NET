using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Conversion
{
    public class ConvertWithoutXpsOptions
    {
        public static void Run()
        {
            #ExStart:ConvertWithoutXpsOptions
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Conversion()

            # Instantiate a Presentation object that represents a presentation file
            using (Presentation pres = new Presentation(dataDir + "Convert_XPS.pptx"))
            {
                # Saving the presentation to XPS document
                pres.save(dataDir + "XPS_Output_Without_XPSOption_out.xps", SaveFormat.Xps)
            }
            #ExEnd:ConvertWithoutXpsOptions
        }
    }
}