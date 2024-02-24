from .extract_audio import extract_audio
from .extract_audio_from_hyperlink import extract_audio_from_hyperlink
from .extract_video import extract_video
from .stop_previous_sound_example import stop_previous_sound_example


def run_slides_media_examples(global_opts):
    extract_audio(global_opts)
    extract_audio_from_hyperlink(global_opts)
    extract_video(global_opts)
    stop_previous_sound_example(global_opts)
