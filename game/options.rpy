## Interlude / Side B — Konfigurasi Proyek Ren'Py (Fase 1: Fondasi)
## Resolusi: 1920x1080 · Platform: Windows & Android

define config.name = "Interlude / Side B"
define gui.show_name = False
define config.version = "1.0.4"

## Direktori penyimpanan khusus proyek ini.
define config.save_directory = "interlude-side-b-2026"

## Ikon jendela memakai aset manifest (tidak ada aset di luar aset_manifest.json).
define config.window_icon = "images/ui/ui_ikon_kaset.png"

## Kanal & mixer audio: Master (main), Musik (music), SFX (sfx), Kaset/VO (voice).
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.main_menu_music = "audio/bgm/bgm_toko.ogg"

init -1 python:
    ## Kanal khusus untuk pemutaran rekaman kaset dari game/audio/kaset/.
    ## Terikat ke mixer "voice" agar dikendalikan langsung oleh slider Kaset / VO.
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

## Bahasa sumber naskah adalah Indonesia (None = bahasa default script).
## Terjemahan cerita Bahasa Inggris berada di game/tl/en/.
define config.default_language = None
define config.clear_history_on_language_change = False

## History / backlog: PRD §4.3 mensyaratkan minimal 200 baris terakhir + rollback klik riwayat.
define config.history_length = 250
define config.hard_rollback_limit = 256

## Autosave & thumbnail slot save (16:9).
define config.has_autosave = True
define config.autosave_on_quit = True
define config.autosave_on_choice = True
define config.autosave_slots = 6
define config.quicksave_slots = 6
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Transisi antarmuka & kotak dialog.
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)
define config.gl_clear_color = "#16100c"

## Preferensi bawaan sesuai PRD §4.4 & visual-novel best practices:
## - Skip hanya melewati teks yang sudah dibaca (skip_unseen = False).
## - Skip selalu berhenti di setiap pilihan / gerbang (skip_after_choices = False).
## - Auto-Forward (AFM) disetel responsif (~2–4 detik per baris pada 1x, ~1–2 detik pada 2x).
define config.afm_characters = 200
define config.afm_bonus = 15
default preferences.text_cps = 45
default preferences.afm_enable = False
default preferences.afm_time = 5
default preferences.skip_unseen = False
default preferences.skip_after_choices = False

## Konfigurasi paket distribusi (Windows & Android).
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
