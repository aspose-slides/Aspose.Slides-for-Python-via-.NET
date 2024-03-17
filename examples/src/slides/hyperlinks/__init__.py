from .add_hyperlink import add_hyperlink
from .external_url_original import external_url_original
from .macro_hyperlink import macro_hyperlink
from .remove_hyperlinks import remove_hyperlinks
from .set_hyperlink_color import set_hyperlink_color


def run_slides_hyperlinks_examples(global_opts):
    add_hyperlink(global_opts)
    external_url_original(global_opts)
    macro_hyperlink()
    remove_hyperlinks(global_opts)
    set_hyperlink_color(global_opts)
