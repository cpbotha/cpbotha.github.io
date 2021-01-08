---
title: Dvorak remapping with Karabiner-Elements on macOS Sierra works!
author: cpbotha
type: post
date: 2016-12-16T09:46:38+00:00
url: /2016/12/16/dvorak-remapping-with-karabiner-elements-on-macos-sierra-works/
categories:
  - howto
tags:
  - dvorak
  - karabiner
  - mac
  - osx
  - sierra

---

<figure>
<a href="https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM.png">
<img
src="https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-1024x646.png"
srcset="https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-1024x646.png
1024w,
https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-300x189.png
300w,
https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-768x484.png
768w,
https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-1200x757.png
1200w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width:
1362px) 62vw, 840px" />
</a>
<figcaption>With some config file elbow grease,
Karabiner-Elements works wonderfully on macOS Sierra to remap your keyboard to
Dvorak.
</figcaption>
</figure>

I have been using [Karabiner][1] for a while now to remap my keyboard to
Dvorak, as the OSX system Dvorak keyboard mapping exposes [a bug in many Java
apps][2], including all of the JetBrains development environment tools I use
intensively, whereby the keyboard is in fact Dvorak, but all shortcut keys are
Qwerty, which is of course tremendously confusing. You can read more about the
issue in [this StackOverflow answer][3].

I was postponing the upgrade to macOS Sierra, because Karabiner, fantastic
keyboard remapping tool, is unable to function on the new OS due to changed
APIs and whatnot.

Fortunately [Takayama Fumihiko][4], awesome hacker behind Karabiner, has been
re-implementing his work in a new tool called [Karabiner-Elements][5]. The GUI
is not up to pre-Sierra level yet, but the tool works perfectly to solve my
Dvorak-remapping (and other) issues!

After upgrading to Sierra, install from the dmg file, start Karabiner-Elements,
then copy [`qwerty_to_dvorak.json` from the examples][6] into your
`~/.karabiner.d/configuration/` directory and name it `karabiner.json`. It will
be immediately picked up, so you're typing in Dvorak. **NB: Since 2016, this
has changed. See new instructions in the update below!**

Personally I have also added the relevant lines from the
`change_caps_lock_to_left_control.json` and
`change_section_key_to_accent_key.json` examples to the `simple_modifications`
clause of my `karabiner.json` file. Using caps-lock as control is essential for
efficient Emacs use, and that section key at the top-left of the MBP 2015
keyboards should have been backtick / tilde to start with.

## Update on 2021-01-06: `qwerty_to_dvorak.json` missing :(

Andrei in the comments has let me know that `qwerty_to_dvorak.json` is not
available on the karabiner elements github anymore.

I've searched in the [karabiner
docs](https://karabiner-elements.pqrs.org/docs/), but could find no mention of
Dvorak.

So, in case it helps anyone, my old `karabiner.json` is shown below. Yours
should be at `~/.config/karabiner/karabiner.json`. You should be able to copy
over the `simple_modifications` clause from the example below.

``` json
{
    "global": {
        "check_for_updates_on_startup": true,
        "show_in_menu_bar": true,
        "show_profile_name_in_menu_bar": false
    },
    "profiles": [
        {
            "devices": [],
            "fn_function_keys": {
                "f1": "display_brightness_decrement",
                "f10": "mute",
                "f11": "volume_decrement",
                "f12": "volume_increment",
                "f2": "display_brightness_increment",
                "f3": "mission_control",
                "f4": "launchpad",
                "f5": "illumination_decrement",
                "f6": "illumination_increment",
                "f7": "rewind",
                "f8": "play_or_pause",
                "f9": "fastforward"
            },
            "name": "Default profile",
            "selected": true,
            "simple_modifications": {
                "a": "a",
                "b": "x",
                "backslash": "backslash",
                "c": "j",
                "caps_lock": "left_control",
                "close_bracket": "equal_sign",
                "comma": "w",
                "d": "e",
                "e": "period",
                "equal_sign": "close_bracket",
                "f": "u",
                "g": "i",
                "h": "d",
                "hyphen": "open_bracket",
                "i": "c",
                "j": "h",
                "k": "t",
                "l": "n",
                "m": "m",
                "n": "b",
                "non_us_backslash": "grave_accent_and_tilde",
                "o": "r",
                "open_bracket": "slash",
                "p": "l",
                "period": "v",
                "q": "quote",
                "quote": "hyphen",
                "r": "p",
                "s": "o",
                "semicolon": "s",
                "slash": "z",
                "t": "y",
                "u": "g",
                "v": "k",
                "w": "comma",
                "x": "q",
                "y": "f",
                "z": "semicolon"
            },
            "virtual_hid_keyboard": {
                "caps_lock_delay_milliseconds": 0,
                "keyboard_type": "ansi"
            }
        }
    ]
}

```

 [1]: https://pqrs.org/osx/karabiner/
 [2]: https://bugs.openjdk.java.net/browse/JDK-8022079
 [3]: http://stackoverflow.com/a/31119280/532513
 [4]: https://github.com/tekezo
 [5]: https://github.com/tekezo/Karabiner-Elements
 [6]: https://github.com/tekezo/Karabiner-Elements/blob/master/examples/qwerty_to_dvorak.json
