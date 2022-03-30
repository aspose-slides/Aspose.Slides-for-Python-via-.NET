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
    class AddLayoutSlides
    {
        public static void Run()
        {
            #ExStart:AddLayoutSlides
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Layout()

            # Instantiate Presentation class that represents the presentation file
            using (Presentation presentation = new Presentation(dataDir + "AccessSlides.pptx"))
            {
                # Try to search by layout slide type
                IMasterLayoutSlideCollection layoutSlides = presentation.Masters[0].LayoutSlides
                ILayoutSlide layoutSlide = layoutSlides.GetByType(SlideLayoutType.TitleAndObject) ?? layoutSlides.GetByType(SlideLayoutType.Title)

                if (layoutSlide == None)
                {
                    # The situation when a presentation doesn't contain some type of layouts.
                    # presentation File only contains Blank and Custom layout types.
                    # But layout slides with Custom types has different slide names,
                    # like "Title", "Title and Content", etc. And it is possible to use these
                    # names for layout slide selection.
                    # Also it is possible to use the set of placeholder shape types. For example,
                    # Title slide should have only Title pleceholder type, etc.
                    foreach (ILayoutSlide titleAndObjectLayoutSlide in layoutSlides)
                    {
                        if (titleAndObjectLayoutSlide.Name == "Title and Object")
                        {
                            layoutSlide = titleAndObjectLayoutSlide
                            break
                        }
                    }

                    if (layoutSlide == None)
                    {
                        foreach (ILayoutSlide titleLayoutSlide in layoutSlides)
                        {
                            if (titleLayoutSlide.Name == "Title")
                            {
                                layoutSlide = titleLayoutSlide
                                break
                            }
                        }

                        if (layoutSlide == None)
                        {
                            layoutSlide = layoutSlides.GetByType(SlideLayoutType.Blank)
                            if (layoutSlide == None)
                            {
                                layoutSlide = layoutSlides.add(SlideLayoutType.TitleAndObject, "Title and Object")
                            }
                        }
                    }
                }

                # Adding empty slide with added layout slide 
                presentation.slides.InsertEmptySlide(0, layoutSlide)

                # Save presentation    
                presentation.save(dataDir + "AddLayoutSlides_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AddLayoutSlides
        }
    }
}