import aspose.slides as slides
from urllib.request import urlopen


def add_video_from_youtube(pres, video_id):
    # add videoFrame
    video_frame = pres.slides[0].shapes.add_video_frame(10, 10, 427, 240, "https://www.youtube.com/embed/" + video_id)
    video_frame.play_mode = slides.VideoPlayModePreset.AUTO

    # load thumbnail
    thumbnail_uri = "http://img.youtube.com/vi/" + video_id + "/hqdefault.jpg"
    f = urlopen(thumbnail_uri)
    video_frame.picture_format.picture.image = pres.images.add_image(f.read())


def add_video_frame_from_web_source(global_opts):
    with slides.Presentation() as pres:
        add_video_from_youtube(pres, "s5JbfQZ5Cc0")
        pres.save(global_opts.out_dir + "shapes_add_video_frame_from_web_out.pptx", slides.export.SaveFormat.PPTX)
