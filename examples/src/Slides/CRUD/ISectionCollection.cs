import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Slides
{
    public class ISectionCollection
    {
        public static void Run()
        {
            #ExStart:ISectionCollection
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_CRUD()

            Presentation pres = new Presentation(dataDir + "Presentation1.pptx")
            ISection section = pres.Sections[2]
            pres.Sections.ReorderSectionWithSlides(section, 0)
            pres.Sections.RemoveSectionWithSlides(pres.Sections[0])
            pres.Sections.AppendEmptySection("Last empty section")
            pres.Sections.AddSection("First empty", pres.slides[0])
            pres.Sections[0].Name = "New section name"
            pres.save(dataDir + "resultsection1.pptx", slides.export.SaveFormat.PPTX)
        }

        #ExEnd:ISectionCollection
    }
}
