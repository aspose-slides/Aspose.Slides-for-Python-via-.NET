import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Linq
using System.text
using System.Threading
using System.Threading.Tasks

namespace CSharp.Presentations.properties
{

    public class SupportForInterrupt
    {

        #ExStart:SupportForInterrupt
        public static void Run()
        {

            dataDir = RunExamples.GetDataDir_PresentationProperties()

            Action<IInterruptionToken> action = (IInterruptionToken token) =>
            {
                options = new { InterruptionToken = token }
                using (Presentation presentation = new Presentation(dataDir + "pres.pptx", options))
                {
                    presentation.save(dataDir + "pres.ppt", SaveFormat.Ppt)
                }
            }

            InterruptionTokenSource tokenSource = new InterruptionTokenSource()
            Run(action, tokenSource.Token) # run action in a separate thread
            Thread.Sleep(10000)            # timeout
            tokenSource.Interrupt()        # stop conversion


        }
        private static void Run(Action<IInterruptionToken> action, IInterruptionToken token)
        {
            Task.Run(() => { action(token) })
        }

        #ExEnd:SupportForInterrupt

    }


}
