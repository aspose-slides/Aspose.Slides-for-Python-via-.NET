import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Presentations.properties
{
    public class AccessModifyingProperties
    {
        public static void Run()
        {
            #ExStart:AccessModifyingProperties
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationProperties()

            # Instanciate the Presentation class that represents the PPTX
            Presentation presentation = new Presentation(dataDir + "AccessModifyingProperties.pptx")

            # Create a reference to DocumentProperties object associated with Prsentation
            IDocumentProperties documentProperties = presentation.DocumentProperties

            # Access and modify custom properties
            for (i = 0 i < documentProperties.CountOfCustomProperties i++)
            {
                # Display names and values of custom properties
                print("Custom Property Name : " + documentProperties.GetCustomPropertyName(i))
                print("Custom Property Value : " + documentProperties[documentProperties.GetCustomPropertyName(i)])

                # Modify values of custom properties
                documentProperties[documentProperties.GetCustomPropertyName(i)] = "New Value " + (i + 1)
            }

            # Save your presentation to a file
            presentation.save(dataDir + "CustomDemoModified_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:AccessModifyingProperties
        }
    }
}