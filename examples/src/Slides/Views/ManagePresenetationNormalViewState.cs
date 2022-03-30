import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Views
{
    class ManagePresenetationNormalViewState
    {
        public static void Run() {

            #ExStart:ManagePresenetationNormalViewState
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Views()

            with slides.Presentation() as pres:
            {
                pres.ViewProperties.NormalViewProperties.HorizontalBarState = SplitterBarStateType.Restored
                pres.ViewProperties.NormalViewProperties.VerticalBarState = SplitterBarStateType.Maximized

                pres.ViewProperties.NormalViewProperties.RestoredTop.AutoAdjust = True
                pres.ViewProperties.NormalViewProperties.RestoredTop.DimensionSize = 80
                pres.ViewProperties.NormalViewProperties.ShowOutlineIcons = True

                pres.save(dataDir+ "presentation_normal_view_state.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:ManagePresenetationNormalViewState
        }
    }
}
