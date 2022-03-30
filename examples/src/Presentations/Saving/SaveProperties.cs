import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Presentations.Saving
{
    public class SaveProperties
    {
        public static void Run()
        {
            #ExStart:SaveProperties
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationSaving()

            # Instantiate a Presentation object that represents a PPT file
            with slides.Presentation() as presentation:

            #....do some work here.....

            # Setting access to document properties in password protected mode
            presentation.ProtectionManager.EncryptDocumentProperties = False

            # Setting Password
            presentation.ProtectionManager.Encrypt("pass")

            # Save your presentation to a file
            presentation.save(dataDir + "Password Protected Presentation_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:SaveProperties
        }
    }
}