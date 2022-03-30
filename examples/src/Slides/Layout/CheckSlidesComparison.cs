using Aspose.slides.Export
using System

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Layout
{
    class CheckSlidesComparison
    {
        public static void Run()
        {
            #ExStart:CheckSlidesComparison
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Layout()
            using (Presentation presentation1 = new Presentation(dataDir + "AccessSlides.pptx"))
            using (Presentation presentation2 = new Presentation(dataDir + "HelloWorld.pptx"))
            {
                for (i = 0 i < presentation1.Masters.Count i++)
                {
                    for (j = 0 j < presentation2.Masters.Count j++)
                    {
                        if (presentation1.Masters[i].Equals(presentation2.Masters[j]))
                            print(string.format("SomePresentation1 MasterSlide#{0} is equal to SomePresentation2 MasterSlide#{1}", i, j))
                    }

                    
                }
            }
            #ExEnd:CheckSlidesComparison
        }
    }
}