import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Presentations
{
    public class AccessProperties
    {
        public static void Run()
        {
            #ExStart:AccessProperties
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationProperties()

            # Accessing the Document Properties of a Password Protected Presentation without Password
            # creating instance of load options to set the presentation access password
            loadOptions = slides.LoadOptions()

            # Setting the access password to None
            loadOptions.Password = None

            # Setting the access to document properties
            loadOptions.OnlyLoadDocumentProperties = True

            # Opening the presentation file by passing the file path and load options to the constructor of Presentation class
            Presentation pres = new Presentation(dataDir + "AccessProperties.pptx", loadOptions)

            # Getting Document Properties
            IDocumentProperties docProps = pres.DocumentProperties

            print("Name of Application : " + docProps.NameOfApplication)
            #ExEnd:AccessProperties
        }
    }
}