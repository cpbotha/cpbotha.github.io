# %% imports
import html
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

from bs4 import BeautifulSoup

# top level hugo path, i.e. the one containing both static and content
tl_path = Path(__file__).resolve().parent.parent
posts_path = tl_path / "content" /  "posts"
static_path = tl_path / "static"

# %%

if False:
    test_fn = posts_path / "2018-12-19-weekly-head-voices-159-extreme.md"

    with open(test_fn, 'r') as f:
        text = ''.join(f.readlines())
        soup = BeautifulSoup(text, features="html.parser")


# %%
def rewrite_to_figure_shortcode(orig_ifn, large_ifn, caption, f) -> bool:
    handled = False
    # we can only convert if we've found both data-orig-file / data-large-file
    if orig_ifn and large_ifn:
        cap_token = f'caption="{html.escape(caption)}"' if caption else ""
        f.write(f'{{{{< figure src="{large_ifn}" link="{orig_ifn}" {cap_token}>}}}}')
        handled = True

        # we should remove images that are not orig or large
        # relative_to('/') essentially removes leading / from orig_ifn
        img_relpath = Path(orig_ifn).relative_to('/')
        orig_path = static_path / img_relpath
        img_subdir = orig_path.parent
        for i in img_subdir.glob(f"{orig_path.stem}-*{orig_path.suffix}"):
            if not (str(i).endswith(orig_ifn) or str(i).endswith(large_ifn)):
                i.unlink()
                print(f"DELETED {i}")

    return handled


def handle_post(filename: Path):
    print(filename)

    # to write this code, I had this body on top-level so I could cell-execute through it
    # as I progressively did the implementation. Only after it worked on the first file
    # did I bring it back here.
    with open(filename, 'r') as f:
        text = ''.join(f.readlines())
        soup = BeautifulSoup(text, features="html.parser")

    # format string here so we can easily change output name during dev
    with open(f"{filename}", 'w') as f:
        for c in soup.contents:
            fig_and_handled = False
            if c.name == 'figure':
                # when we start with new figure, assume we have nothing
                caption = orig_ifn = large_ifn = backup_ifn = None

                # we use findAll, because img could be further nested, sometimes inside <a href=... />
                imgs = c.findAll('img', recursive=True)
                if len(imgs) > 0:
                    img = imgs[0]

                    # data-orig-file and data-large-file
                    # the path is usually e.g. /wp-content/uploads/2018/12/waterkloof_perfect_evening-1024x768.jpg
                    # if data variable is None, path will be ''
                    orig_ifn = urlparse(img.get('data-orig-file', None)).path
                    large_ifn = urlparse(img.get('data-large-file', None)).path

                    # if there are images in this element, we now go through all other elements
                    # we are interested in the caption
                    for cc in c.contents:
                        if cc.name == 'figcaption':
                            caption = cc.text

                        elif cc.name == 'a':
                            href = cc.get('href', '')
                            if href.find('cpbotha.net/wp-content/uploads') >= 0:
                                backup_ifn = urlparse(href).path

                        elif cc.name in [None, 'img', 'a']:
                            pass

                        else:
                            raise RuntimeError(f"unexpected figure subtag {cc.name}")

                    # some figures DON'T have data-orig-file and friends
                    if not orig_ifn:
                        if backup_ifn:
                            orig_ifn = large_ifn = backup_ifn

                    fig_and_handled = rewrite_to_figure_shortcode(orig_ifn, large_ifn, caption, f)

                # end of len(imgs) > 0

            elif c.name == 'div' and 'figure' in c.get('class', []): # same as "c.attrs['class']" ?
                # div.figure -> p -> a -> img
                # no captions that I could see
                try:
                    a = c.findAll('a')[0]
                except IndexError:
                    pass
                else:
                    href = a.attrs['href']
                    if href.find('cpbotha.net/wp-content/uploads') >= 0:
                        orig_ifn = large_ifn = urlparse(href).path
                        fig_and_handled = rewrite_to_figure_shortcode(orig_ifn, large_ifn, "", f)

            elif c.name == 'a' and c.get('data-rel', '').startswith('lightbox') and c.get('href').find('cpbotha.net/wp-content/uploads') >= 0:
                try:
                    img = c.findAll('img')[0]
                except IndexError:
                    pass
                else:
                    large_ifn = urlparse(img.get('data-large-file', None)).path
                    orig_ifn = urlparse(img.get('data-orig-file', None)).path
                    fig_and_handled = rewrite_to_figure_shortcode(orig_ifn, large_ifn, "", f)

            if not fig_and_handled:
                # just output any unhandled figures, and everything else
                f.write(str(c))

    
def main():
    # iterate over every md file in posts_path
    for fn in sys.argv[1:]:
        handle_post(fn)

    #handle_post(posts_path / "2014-07-31-weekly-head-voices-79-remote-controlled-mushrooms.md")

    #handle_post(posts_path / "2018-10-12-weekly-head-voices-155-lush.md")

if __name__ == "__main__":
    main()