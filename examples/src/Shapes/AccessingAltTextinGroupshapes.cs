using System
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    class AccessingAltTextinGroupshapes
    {
        public static void Run()
        {
            #ExStart:AccessingAltTextinGroupshapes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Instantiate Presentation class that represents PPTX file
            Presentation pres = new Presentation(dataDir + "AltText.pptx")

            # Get the first slide
            sld = pres.slides[0]

            for (i = 0 i < sld.shapes.Count i++)
            {
                # Accessing the shape collection of slides
                IShape shape = sld.shapes[i]

                if (shape is GroupShape)
                {
                    # Accessing the group shape.
                    IGroupShape grphShape = (IGroupShape)shape
                    for (j = 0 j < grphShape.shapes.Count j++)
                    {
                        IShape shape2 = grphShape.shapes[j]
                        # Accessing the AltText property
                        print(shape2.AlternativeText)
                    }
                }
            }
            #ExEnd:AccessingAltTextinGroupshapes
        }
    }
}



