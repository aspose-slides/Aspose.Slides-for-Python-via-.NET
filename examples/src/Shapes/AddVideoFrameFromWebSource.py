import aspose.slides as slides
from urllib.request import urlopen

def add_video_from_youyube(pres, videoId):
    #add videoFrame
    videoFrame = pres.slides[0].shapes.add_video_frame(10, 10, 427, 240, "https://www.youtube.com/embed/" + videoId)
    videoFrame.play_mode = slides.VideoPlayModePreset.AUTO

    # load thumbnail
    thumbnail_uri = "http://img.youtube.com/vi/" + videoId + "/hqdefault.jpg"
    f = urlopen(thumbnail_uri)
    videoFrame.picture_format.picture.image = pres.images.add_image(f.read())


with slides.Presentation() as pres:
    outDir = "./examples/out/"

    add_video_from_youyube(pres, "s5JbfQZ5Cc0")
    pres.save(outDir + "shapes_add_video_frame_from_web_out.pptx", slides.export.SaveFormat.PPTX)