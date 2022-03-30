using Aspose.slides.Export
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
    class ConnectShapeUsingConnectionSite
    {
        public static void Run()
        {
            #ExStart:ConnectShapeUsingConnectionSite
            # The path to the documents directory.                    
            dataDir = RunExamples.GetDataDir_Shapes()

            # Instantiate Presentation class that represents the PPTX file
            with slides.Presentation() as presentation:
            {
                # Accessing shapes collection for selected slide
                IShapeCollection shapes = presentation.slides[0].shapes

                # Adding connector shape to slide shape collection
                IConnector connector = shapes.AddConnector(ShapeType.BentConnector3, 0, 0, 10, 10)

                # Add autoshape Ellipse
                ellipse = shapes.add_auto_shape(ShapeType.Ellipse, 0, 100, 100, 100)

                # Add autoshape Rectangle
                rectangle = shapes.add_auto_shape(ShapeType.Rectangle, 100, 200, 100, 100)

                # Joining Shapes to connectors
                connector.StartShapeConnectedTo = ellipse
                connector.EndShapeConnectedTo = rectangle

                # Setting the desired connection site index of Ellipse shape for connector to get connected
                uint wantedIndex = 6

                # Checking if desired index is less than maximum site index count
                if (ellipse.ConnectionSiteCount > wantedIndex)
                {
                    # Setting the desired connection site for connector on Ellipse
                    connector.StartShapeConnectionSiteIndex = wantedIndex
                }

                # Save presentation
                presentation.save(dataDir + "Connecting_Shape_on_desired_connection_site_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ConnectShapeUsingConnectionSite
        }
    }
}
