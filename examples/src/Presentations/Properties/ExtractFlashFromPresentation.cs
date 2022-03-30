using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/


namespace Aspose.slides.Examples.CSharp.Presentations
{
    public class ExtractFlashFromPresentation
    {
        public static void Run()
        {
            #ExStart:ExtractFlashFromPresentation
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationProperties()

            using (Presentation pres = new Presentation(dataDir+"withFlash.pptm"))
            {
                IControlCollection controls = pres.slides[0].controls
                Control flashControl = None
                foreach (control in controls)
                {
                    if (control.Name == "ShockwaveFlash1")
                    {
                        flashControl = (Control)control
                    }
                }
            }
            #ExEnd:ExtractFlashFromPresentation
        }
    }
}