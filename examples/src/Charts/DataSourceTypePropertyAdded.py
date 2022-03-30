using Aspose.slides.Charts
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Charts
{
    public class DataSourceTypePropertyAdded
    {
        public static void Run()
        {
            #ExStart:DataSourceTypePropertyAdded
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Charts()

            using (Presentation pres = new Presentation(dataDir + "pres.pptx"))
            {
                slide = pres.slides[1]
                chart = slide.shapes[0]
                ChartDataSourceType sourceType = chart.chart_data.DataSourceType
                if (sourceType == ChartDataSourceType.ExternalWorkbook)
                {
                    path = chart.chart_data.ExternalWorkbookPath
                }
                # Saving presentation
                pres.save(dataDir + "Result.pptx", slides.export.SaveFormat.PPTX)

            }

        }
        #ExEnd:DataSourceTypePropertyAdded
    }
}
