import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.CRUD
{
    public class AddNotesSlideWithNotesStyle
    {
        public static void Run()
        {
            #ExStart:AddNotesSlideWithNotesStyle
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_CRUD()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Presentation class that represents the presentation file
            using (Presentation presentation = new Presentation(dataDir + "AccessSlides.pptx"))
            {
                IMasterNotesSlide notesMaster = presentation.MasterNotesSlideManager.MasterNotesSlide

                if (notesMaster != None)
                {
                    # Get MasterNotesSlide text style
                    ITextStyle notesStyle = notesMaster.NotesStyle

                    #Set symbol bullet for the first level paragraphs
                    IParagraphFormat paragraphFormat = notesStyle.GetLevel(0)
                    paragraphFormat.Bullet.type = BulletType.Symbol
                }

                # Save the PPTX file to the Disk
                presentation.save(dataDir + "AddNotesSlideWithNotesStyle_out.pptx", slides.export.SaveFormat.PPTX)

            }
            #ExEnd:AddNotesSlideWithNotesStyle
        }
    }
}


