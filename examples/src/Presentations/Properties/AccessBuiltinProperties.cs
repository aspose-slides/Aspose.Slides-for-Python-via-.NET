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
    public class AccessBuiltinProperties
    {
        public static void Run()
        {
            #ExStart:AccessBuiltinProperties

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationProperties()

            # Instantiate the Presentation class that represents the presentation
            Presentation pres = new Presentation(dataDir + "AccessBuiltin Properties.pptx")

            # Create a reference to IDocumentProperties object associated with Presentation
            IDocumentProperties documentProperties = pres.DocumentProperties

            # Display the builtin properties
            print("Category : " + documentProperties.Category)
            print("Current Status : " + documentProperties.ContentStatus)
            print("Creation Date : " + documentProperties.CreatedTime)
            print("Author : " + documentProperties.Author)
            print("Description : " + documentProperties.Comments)
            print("KeyWords : " + documentProperties.Keywords)
            print("Last Modified By : " + documentProperties.LastSavedBy)
            print("Supervisor : " + documentProperties.Manager)
            print("Modified Date : " + documentProperties.LastSavedTime)
            print("Presentation Format : " + documentProperties.PresentationFormat)
            print("Last Print Date : " + documentProperties.LastPrinted)
            print("Is Shared between producers : " + documentProperties.SharedDoc)
            print("Subject : " + documentProperties.Subject)
            print("Title : " + documentProperties.Title)
            #ExEnd:AccessBuiltinProperties            
        }
    }
}