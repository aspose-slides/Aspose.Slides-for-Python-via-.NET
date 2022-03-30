import aspose.slides as slides
using Aspose.slides.Charts
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.Net
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
    class SetExternalWorkbookFromNetwork
    {
        public static void Run() {
            #ExStart:SetExternalWorkbookFromNetwork

            externalWbPath = @"http:#606178d2.ngrok.io/webgrind/styles/2.xlsx"
            opts = slides.LoadOptions()
            opts.ResourceLoadingCallback = new WorkbookLoadingHandler()

            using (Presentation pres = new Presentation(opts))
            {
                chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 400, 600, False)
                IChartData chartData = chart.chart_data

                (chartData as ChartData).set_external_workbook(externalWbPath)
            }

            #ExEnd:SetExternalWorkbookFromNetwork

        }
    }


    class WorkbookLoadingHandler : IResourceLoadingCallback
    {
        public ResourceLoadingAction ResourceLoading(IResourceLoadingArgs args)
        {
            workbookPath = args.OriginalUri

            if (workbookPath.IndexOf(':') > 1 && !workbookPath.StartsWith("file:#/")) # schemed path
            {
                try
                {
                    WebRequest request = WebRequest.Create(workbookPath)
                    request.Credentials = new System.Net.NetworkCredential("testuser", "testuser")
                    using (WebResponse response = request.GetResponse())
                    using (Stream responseStream = response.GetResponseStream())
                    {
                        #byte[] buffer = BlobDownloadManager.Download(responseStream)
                        # args.SetData(buffer)
                        return ResourceLoadingAction.UserProvided
                    }
                }
                catch (Exception ex)
                {
                    throw new InvalidOperationException(ex.ToString())
                }
            }
            else
            {
                return ResourceLoadingAction.Default
            }
        }
    }
}
