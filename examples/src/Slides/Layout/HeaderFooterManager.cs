﻿using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Layout
{
    class HeaderFooterManager
    {
        public static void Run()
        {
            #ExStart:HeaderFooterManager
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Layout()
            using (Presentation presentation = new Presentation(dataDir+"presentation.ppt"))
            {
                IBaseSlideHeaderFooterManager headerFooterManager = presentation.slides[0].HeaderFooterManager
                if (!headerFooterManager.IsFooterVisible) # Property IsFooterVisible is used for indicating that a slide footer placeholder is not present.
                {
                    headerFooterManager.SetFooterVisibility(True) # Method SetFooterVisibility is used for making a slide footer placeholder visible.
                }
                if (!headerFooterManager.IsSlideNumberVisible) # Property IsSlideNumberVisible is used for indicating that a slide page number placeholder is not present.
                {
                    headerFooterManager.SetSlideNumberVisibility(True) # Method SetSlideNumberVisibility is used for making a slide page number placeholder visible.
                }
                if (!headerFooterManager.IsDateTimeVisible) # Property IsDateTimeVisible is used for indicating that a slide date-time placeholder is not present.
                {
                    headerFooterManager.SetDateTimeVisibility(True) # Method SetFooterVisibility is used for making a slide date-time placeholder visible.
                }
                headerFooterManager.SetFooterText("Footer text") # Method SetFooterText is used for setting text to slide footer placeholder.
                headerFooterManager.SetDateTimeText("Date and time text") # Method SetDateTimeText is used for setting text to slide date-time placeholder.



                presentation.save(dataDir + "Presentation.ppt", SaveFormat.Ppt)
            }
            
            #ExEnd:HeaderFooterManager
        }
    }
}