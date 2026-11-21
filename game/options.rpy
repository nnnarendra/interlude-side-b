define config.name = "Interlude / Side B"
define gui.show_name = False
define config.version = "1.0.5"

define config.save_directory = "interlude-side-b-2026"

define config.window_icon = "images/ui/ui_ikon_kaset.png"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.main_menu_music = "audio/bgm/bgm_toko.ogg"

init -1 python:

    renpy.music.register_channel(
        "kaset",
        mixer="voice",
        loop=False,
        stop_on_mute=True,
        tight=False,
        file_prefix="",
        file_suffix="",
        buffer_queue=True,
    )
    if "kaset" not in config.main_menu_stop_channels:
        config.main_menu_stop_channels.append("kaset")

define config.default_language = None
define config.clear_history_on_language_change = False

define config.history_length = 250
define config.hard_rollback_limit = 256

define config.has_autosave = True
define config.autosave_on_quit = True
define config.autosave_on_choice = True
define config.autosave_slots = 6
define config.quicksave_slots = 6
define config.thumbnail_width = 384
define config.thumbnail_height = 216

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)
define config.gl_clear_color = "#16100c"

define config.afm_characters = 200
define config.afm_bonus = 15
default preferences.text_cps = 45
default preferences.afm_enable = False
default preferences.afm_time = 5
default preferences.skip_unseen = False
default preferences.skip_after_choices = False

init python:
    build.name = "interlude-side-b"
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("README.md", "all")
    build.classify("game/**.rpy", "archive")
    build.classify("game/**.rpyc", "archive")
    build.classify("game/images/**", "archive")
    build.classify("game/audio/**", "archive")
