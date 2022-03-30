using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Presentations.Conversion
{
    public class SavingHTMLAndCSSFileWhenExportingIntoHTML
    {
        public static void Run()
        {
            #ExStart:SavingHTMLAndCSSFileWhenExportingIntoHTML
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Conversion()
            using (Presentation pres = new Presentation("pres.pptx"))
         {
            CustomHeaderAndFontsController htmlController = new CustomHeaderAndFontsController("styles.css")
            HtmlOptions options = new HtmlOptions
          {
            HtmlFormatter = HtmlFormatter.CreateCustomFormatter(htmlController),
           }

    pres.save("pres.html", SaveFormat.Html, options)
            }
            }
            #ExEnd:SavingHTMLAndCSSFileWhenExportingIntoHTML

     }
    }
