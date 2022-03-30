using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Layout
{
    class SetChildFooter
    {
        public static void Run()
        {
            #ExStart:SetChildFooter
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Layout()
            using (Presentation presentation = new Presentation(dataDir+"presentation.ppt"))
            {
                IMasterSlideHeaderFooterManager headerFooterManager = presentation.Masters[0].HeaderFooterManager
                headerFooterManager.SetFooterAndChildFootersVisibility(True) # Method SetFooterAndChildFootersVisibility is used for making a master slide and all child footer placeholders visible.
                headerFooterManager.SetSlideNumberAndChildSlideNumbersVisibility(True) # Method SetSlideNumberAndChildSlideNumbersVisibility is used for making a master slide and all child page number placeholders visible.
                headerFooterManager.SetDateTimeAndChildDateTimesVisibility(True) # Method SetDateTimeAndChildDateTimesVisibility is used for making a master slide and all child date-time placeholders visible.

                headerFooterManager.SetFooterAndChildFootersText("Footer text") # Method SetFooterAndChildFootersText is used for setting text to master slide and all child footer placeholders.
                headerFooterManager.SetDateTimeAndChildDateTimesText("Date and time text") # Method SetDateTimeAndChildDateTimesText is used for setting text to master slide and all child date-time placeholders.
            }

            #ExEnd:SetChildFooter
        }
    }
}