## Interlude / Side B — Kerangka Layar Antarmuka (Fase 1: Fondasi)
## Resolusi: 1920x1080 · Semua teks antarmuka WAJIB melalui `ui_tr(...)`.
## Tidak menggunakan aset gambar di luar `aset_manifest.json`.

init offset = -1

################################################################################
## Gaya dasar (Styles)
################################################################################

style default:
    font gui.text_font
    size gui.interface_text_size
    color gui.text_color
    language "unicode"

style frame:
    background Solid(UI_BG_PANEL)
    padding (20, 20)

style window:
    background Solid("#16100ce8")

style say_window is window:
    background Solid("#16100cba")

style say_label:
    bold True
    color gui.accent_color

style say_dialogue:
    color gui.text_color
    line_spacing 6
    adjust_spacing False

style bar:
    ysize 24
    left_bar Solid("#d49a58")
    right_bar Solid("#45352a")

style vbar:
    xsize 24
    top_bar Solid("#d49a58")
    bottom_bar Solid("#45352a")

style scrollbar:
    ysize 14
    base_bar Solid("#2b2019")
    thumb Solid("#9e7448")
    hover_thumb Solid("#d49a58")

style vscrollbar:
    xsize 14
    base_bar Solid("#2b2019")
    thumb Solid("#9e7448")
    hover_thumb Solid("#d49a58")

style game_menu_vscrollbar is vscrollbar

style slider:
    ysize 28
    left_bar Solid("#d49a58")
    right_bar Solid("#45352a")
    thumb Solid("#fff3df", xsize=18, ysize=28)
    thumb_offset 9

style vslider:
    xsize 28
    top_bar Solid("#d49a58")
    bottom_bar Solid("#45352a")
    thumb Solid("#fff3df", xsize=28, ysize=18)
    thumb_offset 9

style button:
    background Solid(UI_BG_CARD)
    hover_background Solid(UI_BG_CARD_HOVER)
    selected_background Solid("#5c3f26f5")
    insensitive_background Solid("#1d1612b0")
    padding (24, 14)

style button_text:
    font gui.interface_text_font
    size gui.interface_text_size
    color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color

style nav_button is button:
    xfill True
    yminimum 60
    padding (28, 12)
    background Solid("#00000000")
    hover_background Solid("#4a3424cc")
    selected_background Solid("#63442acc")
    insensitive_background Solid("#00000000")

style nav_button_text is button_text:
    size 30
    xalign 0.0

style main_menu_button is button:
    xfill True
    yminimum 64
    padding (32, 12)
    background Solid("#2b1f18cc")
    hover_background Solid("#5e4128ee")
    insensitive_background Solid("#1c141088")

style main_menu_button_text is button_text:
    size 32
    xalign 0.0

style pill_button is button:
    yminimum 54
    xminimum 150
    padding (22, 10)
    background Solid("#2a1f18e6")
    hover_background Solid("#473324f2")
    selected_background Solid("#8a5c2ef5")
    insensitive_background Solid("#1b141099")

style pill_button_text is button_text:
    size 26
    xalign 0.5
    color gui.idle_color
    hover_color gui.hover_color
    selected_color "#fff8ed"

style tab_button is pill_button:
    xminimum 240
    yminimum 58

style tab_button_text is pill_button_text:
    size 28

style quick_button is button:
    padding (16, 8)
    yminimum 44
    background Solid("#00000000")
    hover_background Solid("#4a3424aa")
    selected_background Solid("#7c5328cc")

style quick_button_text is button_text:
    size 22
    color "#cbbca8"
    hover_color "#fff5e6"
    selected_color "#f6c987"

style section_title:
    font gui.interface_text_font
    size 32
    bold True
    color gui.accent_color

style pref_label:
    font gui.interface_text_font
    size 26
    color gui.text_color

style pref_note:
    font gui.interface_text_font
    size 22
    color UI_TEXT_MUTED

style custom_slider is slider:
    xsize 420
    ysize 28
    left_bar Solid("#d49a58")
    right_bar Solid("#45352a")
    thumb Solid("#fff3df", xsize=18, ysize=28)
    thumb_offset 9

style choice_button is button:
    xsize 1160
    yminimum 72
    padding (36, 18)
    background Solid("#241b15e8")
    hover_background Solid("#593d25f5")

style choice_button_text is button_text:
    size 30
    xalign 0.5
    color gui.text_color
    hover_color "#fff8ed"

style namebox:
    background Solid("#261c15c8")
    padding (30, 10, 34, 10)

style choice_card_button is button:
    padding (6, 6)
    background Solid("#4f3b2ce8")
    hover_background Solid("#e0a55ef8")

style choice_card_caption:
    font gui.interface_text_font
    size 24
    color gui.text_color
    line_spacing 4

transform choice_card_motion:
    yoffset 0
    on hover:
        easein 0.14 yoffset -8
    on idle:
        easeout 0.14 yoffset 0

transform choice_sprite_crop:
    xalign 0.5
    yalign 0.04
    zoom 0.46

transform chapter_banner_anim:
    alpha 0.0
    xoffset -24
    easein 0.35 alpha 1.0 xoffset 0
    pause 2.4
    easeout 0.45 alpha 0.0 xoffset -16

################################################################################
## Layar Dialog (Say), Pilihan Bergambar (Choice), Input, Quick Menu
################################################################################

screen say(who, what):
    style_prefix "say"

    ## Penanda status AUTO & Mode 2x di sudut kanan atas (PRD §4.4).
    if persistent.read_speed_2x or _preferences.afm_enable:
        hbox:
            align (0.98, 0.03)
            spacing 10

            if _preferences.afm_enable:
                frame:
                    background Solid("#3b2d22e6")
                    padding (16, 8)
                    text ui_tr("badge_auto_active") size 21 bold True color gui.selected_color

            if persistent.read_speed_2x:
                frame:
                    background Solid("#7c5328e6")
                    padding (18, 8)
                    text ui_tr("badge_2x_active") size 21 bold True color "#fff8ed"

    ## Kotak dialog bawah + nameplate nama penutur di bagian atas agar dialog Kai
    ## (lisan maupun batin) tidak pernah rancu dengan narasi.
    vbox:
        xfill True
        yalign 1.0
        spacing 0

        if who is not None:
            frame:
                id "namebox"
                style "namebox"
                xpos 112
                vbox:
                    spacing 4
                    add Solid("#e0a55e") xsize 54 ysize 3
                    text who id "who" style "say_label" size scaled_font_size(gui.name_text_size)

        add Solid("#d49a5899") xsize 1920 ysize 2

        window:
            id "window"
            style "say_window"
            xfill True
            yminimum gui.textbox_height
            padding (110, 26, 110, 82)

            text what id "what" style "say_dialogue" size scaled_font_size(gui.text_size)

    ## Zona sentuh/klik sisi kiri (~20% layar, di atas quick_menu) = Kembali (Rollback);
    ## klik tengah atau kanan layar otomatis melanjutkan cerita.
    button:
        xpos 0
        ypos 0
        xsize 380
        ysize 990
        background None
        hover_background None
        action Rollback()


screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            xalign 0.5
            yalign 0.992
            spacing 8

            textbutton ui_tr("qm_back") style "quick_button" action Rollback()
            textbutton ui_tr("qm_history") style "quick_button" action ShowMenu("history")
            textbutton ui_tr("qm_skip") style "quick_button" action Skip() alternate Skip(fast=True, confirm=True)
            textbutton ui_tr("qm_auto") style "quick_button" action ToggleAutoForward()
            textbutton (ui_tr("qm_speed_2x") if persistent.read_speed_2x else ui_tr("qm_speed_1x")) style "quick_button" action ToggleSpeed2x()
            textbutton ui_tr("qm_qsave") style "quick_button" action QuickSave(message=ui_tr("notify_quick_saved"))
            textbutton ui_tr("qm_qload") style "quick_button" action QuickLoad()
            textbutton ui_tr("qm_save") style "quick_button" action ShowMenu("save")
            textbutton ui_tr("qm_glossary") style "quick_button" action ShowMenu("glossary")
            textbutton ui_tr("qm_hide") style "quick_button" action HideInterface()
            textbutton ui_tr("qm_settings") style "quick_button" action ShowMenu("preferences")


init python:
    if "quick_menu" not in config.overlay_screens:
        config.overlay_screens.append("quick_menu")

default quick_menu = True


screen choice(items):
    ## Wajib hentikan skip & auto-play serta tutup popup item di setiap menu pilihan (PRD §4.4).
    on "show" action [Function(stop_skip_and_auto), Function(hide_item)]

    $ _banner_text, _banner_accent = get_menu_gate_banner(items)
    $ _count = len(items)
    $ _art_w = 556 if _count <= 2 else 486
    $ _card_w = _art_w + 12
    $ _art_h = 282
    $ _cap_h = 200
    $ _inner_h = _art_h + 3 + _cap_h
    $ _card_h = _inner_h + 12
    $ _card_gap = 48 if _count <= 2 else 30

    ## Lapisan gelap halus agar kartu pilihan bergambar menonjol tanpa menutup prompt di bawah.
    add Solid("#0d090794")

    ## Tajuk Gerbang / Pilihan di bagian atas.
    vbox:
        xalign 0.5
        ypos 42
        spacing 8

        frame:
            xalign 0.5
            background Solid("#1e1510ee")
            padding (30, 10)
            hbox:
                spacing 14
                add "images/ui/ui_ikon_kaset.png" xysize (28, 28) fit "contain" yalign 0.5
                text _banner_text size 24 bold True color _banner_accent yalign 0.5 substitute False

        text ui_tr("choice_hint") size 21 color UI_TEXT_MUTED xalign 0.5

    ## Baris kartu pilihan bergambar (2 atau 3 kartu sejajar).
    hbox:
        xalign 0.5
        ypos 148
        spacing _card_gap

        for idx, i in enumerate(items):
            $ _meta = get_choice_card_meta(i.caption, idx)
            $ _card_accent = "#d96252" if _meta["gate_type"] == "climax" else ("#e0a55e" if _meta["gate_type"] in ("major", "cond") else "#c9a275")

            button:
                style "choice_card_button"
                xsize _card_w
                ysize _card_h
                hover_background Solid(_card_accent)
                at choice_card_motion
                action i.action

                frame:
                    xsize _art_w
                    ysize _inner_h
                    background Solid("#1f1712fa")
                    padding (0, 0)

                    vbox:
                        spacing 0

                        ## Area ilustrasi kartu pilihan (dipotong rapi via viewport).
                        fixed:
                            xsize _art_w
                            ysize _art_h

                            viewport:
                                xsize _art_w
                                ysize _art_h
                                clipping True
                                draggable False
                                mousewheel False

                                if _meta["kind"] == "bg":
                                    add _meta["img"] xysize (_art_w, _art_h) fit "cover"
                                elif _meta["kind"] == "sprite":
                                    fixed:
                                        xsize _art_w
                                        ysize _art_h
                                        add Solid("#2d2119")
                                        add _meta["img"] at choice_sprite_crop
                                else:
                                    fixed:
                                        xsize _art_w
                                        ysize _art_h
                                        add Solid("#1a130f")
                                        add _meta["img"] xysize (148, 148) fit "contain" align (0.5, 0.5)

                            ## Pita label atas kartu (ID gerbang + huruf opsi).
                            frame:
                                xsize _art_w
                                ysize 46
                                background Solid("#140e0bb8")
                                padding (16, 6)

                                hbox:
                                    xfill True
                                    yalign 0.5

                                    if _meta["gate_id"]:
                                        text _meta["gate_id"] size 20 bold True color _card_accent yalign 0.5 substitute False
                                    else:
                                        null width 1

                                    if _meta["letter"]:
                                        frame:
                                            xalign 1.0
                                            yalign 0.5
                                            background Solid(_card_accent)
                                            padding (12, 2)
                                            text _meta["letter"] size 19 bold True color "#1a120d" substitute False

                        ## Garis aksen pemisah gambar & teks pilihan.
                        add Solid(_card_accent) xsize _art_w ysize 3

                        ## Area teks pilihan di bagian bawah kartu.
                        frame:
                            xsize _art_w
                            ysize _cap_h
                            background None
                            padding (22, 16)

                            text i.caption:
                                style "choice_card_caption"
                                align (0.5, 0.5)
                                text_align 0.5
                                size scaled_font_size(24)
                                substitute False


screen chapter_banner(title_id, title_en):
    zorder 140

    $ _ch_title = title_en if (persistent.story_lang == "en" and title_en) else title_id

    frame at chapter_banner_anim:
        xpos 44
        ypos 34
        background Solid("#1d1510e8")
        padding (26, 16)

        hbox:
            spacing 16
            add Solid("#e0a55e") xsize 4 ysize 54 yalign 0.5
            vbox:
                spacing 4
                text ui_tr("chapter_banner_tag") size 17 bold True color gui.accent_color
                text _ch_title size 26 bold True color gui.selected_color substitute False

    timer 3.3 action Hide("chapter_banner")


screen input(prompt):
    window:
        align (0.5, 0.5)
        xsize 1100
        background Solid(UI_BG_PANEL)
        padding (48, 40)

        vbox:
            spacing 24
            xalign 0.5
            text prompt size 30 color gui.text_color xalign 0.5
            input id "input" size 30 color gui.accent_color xalign 0.5


################################################################################
## Menu Utama / Homepage (PRD §4.1)
################################################################################

screen main_menu():
    tag menu

    ## Latar placeholder dari aset_manifest.json.
    add "images/ui/ui_latar_menu.jpg" xysize (1920, 1080) fit "cover"

    ## Panel kiri: 8 tombol wajib persis urutan PRD §4.1 (opacity diturunkan 40% agar BG terlihat lega).
    frame:
        xpos 0
        ypos 0
        xsize 540
        ysize 1080
        background Solid("#18110d7a")
        padding (56, 84, 56, 64)

        vbox:
            xfill True
            yfill True
            spacing 14

            vbox:
                spacing 14
                yalign 0.5
                xfill True

                textbutton ui_tr("menu_new_game") style "main_menu_button" action Start()
                textbutton ui_tr("menu_continue") style "main_menu_button" action Continue(confirm=False)
                textbutton ui_tr("menu_load") style "main_menu_button" action ShowMenu("load")
                textbutton ui_tr("menu_gallery") style "main_menu_button" action ShowMenu("gallery")
                textbutton ui_tr("menu_achievements") style "main_menu_button" action ShowMenu("achievements")
                textbutton ui_tr("menu_settings") style "main_menu_button" action ShowMenu("preferences")
                textbutton ui_tr("menu_credits") style "main_menu_button" action ShowMenu("credits")
                if renpy.variant("pc") or renpy.variant("android"):
                    textbutton ui_tr("menu_quit") style "main_menu_button" action Quit(confirm=True)

            ## Informasi versi ringan di bagian bawah panel kiri.
            text "v[config.version]" size 20 color UI_TEXT_DIM yalign 1.0

    ## Area kanan: Logo placeholder + 5 indikator titik kaset ending (PRD §4.1).
    frame:
        xpos 540
        ypos 0
        xsize 1380
        ysize 1080
        background None

        vbox:
            align (0.5, 0.44)
            spacing 32

            add "images/ui/ui_logo_judul.png" xalign 0.5

            ## 5 indikator titik kaset yang menyala sesuai ending yang sudah dibuka.
            vbox:
                xalign 0.5
                spacing 14

                hbox:
                    xalign 0.5
                    spacing 22

                    for entry in ENDINGS_CATALOG:
                        $ _opened = is_ending_unlocked(entry["id"])
                        frame:
                            xsize 54
                            ysize 54
                            background Solid("#d49a58" if _opened else "#2a201acc")
                            padding (6, 6)
                            add "images/ui/ui_ikon_kaset.png":
                                align (0.5, 0.5)
                                xysize (38, 38)
                                fit "contain"
                                alpha (1.0 if _opened else 0.28)

                $ _unlocked_count = len(persistent.unlocked_endings) if isinstance(persistent.unlocked_endings, dict) else 0
                text ui_tr("menu_endings_dots_label", count=_unlocked_count):
                    size 22
                    color UI_TEXT_MUTED
                    xalign 0.5

    if config.developer:
        key "shift_K_d" action ShowMenu("ending_debug")


################################################################################
## Navigasi & Kerangka Sub-Layar (Game Menu)
################################################################################

screen navigation():
    vbox:
        xfill True
        spacing 10

        if not main_menu:
            textbutton ui_tr("nav_return") style "nav_button" action Return()
            null height 10
            textbutton ui_tr("nav_save") style "nav_button" action ShowMenu("save")
            textbutton ui_tr("nav_load") style "nav_button" action ShowMenu("load")
            textbutton ui_tr("nav_history") style "nav_button" action ShowMenu("history")
            textbutton ui_tr("nav_gallery") style "nav_button" action ShowMenu("gallery")
            textbutton ui_tr("nav_achievements") style "nav_button" action ShowMenu("achievements")
            textbutton ui_tr("nav_settings") style "nav_button" action ShowMenu("preferences")
            textbutton ui_tr("nav_glossary") style "nav_button" action ShowMenu("glossary")
            textbutton ui_tr("nav_credits") style "nav_button" action ShowMenu("credits")
            textbutton ui_tr("nav_changelog") style "nav_button" action ShowMenu("changelog")
            null height 16
            textbutton ui_tr("nav_main_menu") style "nav_button" action MainMenu(confirm=True)
            if renpy.variant("pc") or renpy.variant("android"):
                textbutton ui_tr("nav_quit") style "nav_button" action Quit(confirm=True)
        else:
            textbutton ui_tr("nav_load") style "nav_button" action ShowMenu("load")
            textbutton ui_tr("nav_gallery") style "nav_button" action ShowMenu("gallery")
            textbutton ui_tr("nav_achievements") style "nav_button" action ShowMenu("achievements")
            textbutton ui_tr("nav_settings") style "nav_button" action ShowMenu("preferences")
            textbutton ui_tr("nav_glossary") style "nav_button" action ShowMenu("glossary")
            textbutton ui_tr("nav_credits") style "nav_button" action ShowMenu("credits")
            textbutton ui_tr("nav_changelog") style "nav_button" action ShowMenu("changelog")
            null height 24
            textbutton ui_tr("nav_return") style "nav_button" action Return()


screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    add "images/ui/ui_latar_menu.jpg" xysize (1920, 1080) fit "cover"
    add Solid("#120d0ad9")

    ## Sidebar kiri.
    frame:
        xpos 0
        ypos 0
        xsize 380
        ysize 1080
        background Solid("#1a120ee8")
        padding (32, 48, 32, 48)

        vbox:
            xfill True
            yfill True
            spacing 24

            hbox:
                spacing 14
                add "images/ui/ui_ikon_kaset.png" xysize (42, 42) fit "contain" yalign 0.5
                text "Interlude / Side B" size 26 bold True color gui.accent_color yalign 0.5

            frame:
                xfill True
                ysize 2
                padding (0, 0)
                background Solid(UI_BORDER_SUBTLE)

            use navigation

    ## Area konten kanan.
    frame:
        xpos 380
        ypos 0
        xsize 1540
        ysize 1080
        background None
        padding (56, 48, 56, 48)

        vbox:
            xfill True
            yfill True
            spacing 24

            ## Header judul layar.
            vbox:
                spacing 12
                xfill True
                text title size 44 bold True color gui.text_color
                add Solid(UI_BORDER_ACCENT) ysize 3 xsize 140

            ## Badan konten (scrollable atau fixed).
            if scroll == "viewport":
                viewport:
                    id "vp"
                    xfill True
                    yfill True
                    yinitial yinitial
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    mousewheel True
                    draggable True
                    pagekeys True

                    vbox:
                        xfill True
                        spacing 24
                        transclude
            else:
                frame:
                    background None
                    xfill True
                    yfill True
                    transclude

    key "game_menu" action Return()


################################################################################
## Layar Save & Load (PRD §4.2)
## 3 halaman x 6 slot manual + Autosave + Quick Save/Load, thumbnail,
## tanggal-jam, nama bab, 12-huruf string pilihan, konfirmasi timpa & hapus.
################################################################################

screen save():
    tag menu
    on "show" action If(FileCurrentPage() in ("auto", "quick"), FilePage(1), NullAction())
    use file_slots(title=ui_tr("save_title"), is_save=True)


screen load():
    tag menu
    use file_slots(title=ui_tr("load_title"), is_save=False)


screen file_slots(title, is_save=False):
    use game_menu(title):
        vbox:
            xfill True
            yfill True
            spacing 22

            ## Bar pilih halaman: 3 halaman manual + Autosave + Cepat (pada Muat).
            hbox:
                spacing 14

                if not is_save:
                    textbutton ui_tr("page_auto") style "pill_button" action FilePage("auto")
                    textbutton ui_tr("page_quick") style "pill_button" action FilePage("quick")

                for page_num in range(1, 4):
                    textbutton ui_tr("page_num", n=page_num) style "pill_button" action FilePage(page_num)

            if is_save:
                text ui_tr("save_quick_hint") style "pref_note"
            elif FileCurrentPage() == "auto":
                text ui_tr("save_auto_readonly") style "pref_note"

            ## Grid 3 kolom x 2 baris = 6 slot per halaman.
            grid gui.file_slot_cols gui.file_slot_rows:
                xfill True
                spacing 24

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    $ _has_file = FileLoadable(slot)
                    $ _ch_key = "chapter_name_en" if (persistent.ui_lang == "en") else "chapter_name_id"
                    $ _ch_fallback_key = "chapter_name_id" if (persistent.ui_lang == "en") else "chapter_name_en"
                    $ _chapter_text = (FileJson(slot, _ch_key, empty="", missing="") or FileJson(slot, _ch_fallback_key, empty="", missing="")) if _has_file else ""
                    $ _choice_code = FileJson(slot, "choice_string", empty="", missing="") if _has_file else ""

                    frame:
                        xsize 456
                        ysize 368
                        background Solid(UI_BG_CARD if _has_file else UI_BG_CARD_LOCKED)
                        padding (16, 16)

                        vbox:
                            xfill True
                            yfill True
                            spacing 10

                            ## Area klik utama (Simpan / Muat).
                            button:
                                xfill True
                                ysize 286
                                padding (0, 0)
                                background Solid("#00000000")
                                hover_background Solid("#ffffff14")
                                action (FileSave(slot, confirm=True) if is_save else FileLoad(slot, confirm=True))

                                vbox:
                                    xfill True
                                    spacing 8

                                    ## Thumbnail 16:9.
                                    frame:
                                        xsize 384
                                        ysize 216
                                        xalign 0.5
                                        background Solid("#120d0a")
                                        padding (0, 0)

                                        if _has_file:
                                            add FileScreenshot(slot) xysize (384, 216) fit "cover"
                                        else:
                                            text ui_tr("slot_empty") size 24 color UI_TEXT_DIM align (0.5, 0.5)

                                    ## Tanggal-jam.
                                    text FileTime(slot, format="%d/%m/%Y  %H:%M", empty=ui_tr("slot_empty")):
                                        size 20
                                        color (gui.accent_color if _has_file else UI_TEXT_DIM)

                                    ## Nama bab.
                                    if _has_file:
                                        text (_chapter_text if _chapter_text else ui_tr("slot_chapter_none")):
                                            size 21
                                            color gui.text_color
                                            substitute False

                            ## Baris bawah: 12-huruf pilihan + tombol Hapus.
                            hbox:
                                xfill True
                                yalign 1.0

                                if _has_file:
                                    text ui_tr("slot_choices_label", code=(_choice_code if _choice_code else "------------")):
                                        size 18
                                        color UI_TEXT_MUTED
                                        yalign 0.5
                                else:
                                    null width 1

                                if _has_file:
                                    textbutton ui_tr("slot_delete"):
                                        xalign 1.0
                                        padding (14, 4)
                                        background Solid("#5c2620cc")
                                        hover_background Solid("#8a342af0")
                                        text_size 18
                                        text_color "#ffded8"
                                        action FileDelete(slot, confirm=True)


################################################################################
## Layar Pengaturan / Settings (PRD §4.4 & §4.5)
################################################################################

screen preferences():
    tag menu

    use game_menu(ui_tr("settings_title"), scroll="viewport"):

        ## 1. BAHASA GANDA INDEPENDEN (Bahasa UI vs Bahasa Cerita)
        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (32, 26)

            vbox:
                xfill True
                spacing 18

                text ui_tr("sec_language") style "section_title"

                hbox:
                    spacing 80

                    vbox:
                        spacing 10
                        text ui_tr("lbl_ui_lang") style "pref_label"
                        hbox:
                            spacing 12
                            textbutton ui_tr("lang_id") style "pill_button" action SetUILanguage("id")
                            textbutton ui_tr("lang_en") style "pill_button" action SetUILanguage("en")

                    vbox:
                        spacing 10
                        text ui_tr("lbl_story_lang") style "pref_label"
                        hbox:
                            spacing 12
                            textbutton ui_tr("lang_id") style "pill_button" action SetStoryLanguage("id")
                            textbutton ui_tr("lang_en") style "pill_button" action SetStoryLanguage("en")

                $ _ui_code = (persistent.ui_lang or "id").upper()
                $ _story_code = (persistent.story_lang or "id").upper()
                text ui_tr("lang_status_note", ui=_ui_code, story=_story_code) style "pref_note" substitute False

        ## 2. AUDIO (Master, Musik, SFX, Kaset / VO + Bisukan Semua)
        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (32, 26)

            vbox:
                xfill True
                spacing 18

                text ui_tr("sec_audio") style "section_title"

                grid 2 2:
                    xfill True
                    spacing 28

                    vbox:
                        spacing 8
                        text ui_tr("lbl_vol_master") style "pref_label"
                        bar value Preference("main volume") style "custom_slider"

                    vbox:
                        spacing 8
                        text ui_tr("lbl_vol_music") style "pref_label"
                        bar value Preference("music volume") style "custom_slider"

                    vbox:
                        spacing 8
                        text ui_tr("lbl_vol_sfx") style "pref_label"
                        bar value Preference("sound volume") style "custom_slider"

                    vbox:
                        spacing 8
                        text ui_tr("lbl_vol_kaset") style "pref_label"
                        bar value Preference("voice volume") style "custom_slider"

                hbox:
                    spacing 16
                    textbutton ui_tr("lbl_mute_all") style "pill_button" action Preference("all mute", "toggle")

        ## 3. MODE BACA & TEKS (Kecepatan, Instan, Auto, 1x/2x, Skip, Ukuran Huruf)
        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (32, 26)

            vbox:
                xfill True
                spacing 20

                text ui_tr("sec_reading") style "section_title"

                hbox:
                    spacing 64

                    vbox:
                        spacing 10
                        hbox:
                            spacing 16
                            text ui_tr("lbl_text_speed") style "pref_label"
                            if persistent.base_text_cps == 0:
                                text ui_tr("lbl_text_instant") size 22 color gui.accent_color yalign 0.5
                            else:
                                text ui_tr("lbl_text_speed_val", cps=persistent.base_text_cps) size 22 color gui.accent_color yalign 0.5
                        bar value BaseTextCPSBarValue() style "custom_slider"
                        hbox:
                            spacing 12
                            textbutton ui_tr("lbl_text_normal") style "pill_button" action SetInstantText(False)
                            textbutton ui_tr("lbl_text_instant") style "pill_button" action SetInstantText(True)

                    vbox:
                        spacing 10
                        hbox:
                            spacing 16
                            text ui_tr("lbl_auto_delay") style "pref_label"
                            text ui_tr("lbl_auto_delay_val", sec=persistent.base_afm_time) size 22 color gui.accent_color yalign 0.5
                        bar value BaseAFMTimeBarValue() style "custom_slider"

                hbox:
                    spacing 64

                    vbox:
                        spacing 10
                        text ui_tr("lbl_speed_mode") style "pref_label"
                        hbox:
                            spacing 12
                            textbutton ui_tr("qm_speed_1x") style "pill_button" action SetSpeed2x(False)
                            textbutton ui_tr("qm_speed_2x") style "pill_button" action SetSpeed2x(True)

                    vbox:
                        spacing 10
                        text ui_tr("lbl_skip_mode") style "pref_label"
                        hbox:
                            spacing 12
                            textbutton ui_tr("skip_read_only") style "pill_button" action Preference("skip", "seen")
                            textbutton ui_tr("skip_all_text") style "pill_button" action Preference("skip", "all")

                ## Ukuran huruf + pratinjau langsung.
                vbox:
                    spacing 10
                    $ _font_pct = int(round((persistent.font_size_scale or 1.0) * 100))
                    hbox:
                        spacing 16
                        text ui_tr("lbl_font_size") style "pref_label"
                        text "[_font_pct]%" size 22 color gui.accent_color yalign 0.5
                    bar value FontSizeScaleBarValue() style "custom_slider"
                    frame:
                        xfill True
                        background Solid("#16100ccc")
                        padding (20, 14)
                        text ui_tr("font_preview_sample") size scaled_font_size(gui.text_size) color gui.text_color

        ## 4. TAMPILAN & PERANGKAT (Mode Layar & Getar Android)
        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (32, 26)

            vbox:
                xfill True
                spacing 18

                text ui_tr("sec_display") style "section_title"

                hbox:
                    spacing 80

                    if renpy.variant("pc"):
                        vbox:
                            spacing 10
                            text ui_tr("lbl_display_mode") style "pref_label"
                            hbox:
                                spacing 12
                                textbutton ui_tr("display_fullscreen") style "pill_button" action Preference("display", "fullscreen")
                                textbutton ui_tr("display_window") style "pill_button" action Preference("display", "window")

                    vbox:
                        spacing 10
                        text ui_tr("lbl_vibration") style "pref_label"
                        hbox:
                            spacing 12
                            textbutton ui_tr("state_off") style "pill_button" action SetAndroidVibration(False)
                            textbutton ui_tr("state_on") style "pill_button" action SetAndroidVibration(True)


################################################################################
## Layar Riwayat / History (PRD §4.3)
################################################################################

screen history():
    tag menu
    predict False

    use game_menu(ui_tr("history_title"), scroll="viewport", yinitial=1.0):
        if not _history_list:
            frame:
                xfill True
                background Solid(UI_BG_CARD)
                padding (36, 40)
                text ui_tr("history_empty") size 28 color UI_TEXT_MUTED xalign 0.5
        else:
            for h in _history_list:
                frame:
                    xfill True
                    background Solid(UI_BG_CARD)
                    padding (28, 18)

                    vbox:
                        spacing 8
                        if h.who:
                            text h.who size scaled_font_size(28) bold True color gui.accent_color substitute False
                        $ _what_text = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags) if hasattr(gui, "history_allow_tags") else h.what
                        text _what_text size scaled_font_size(gui.text_size - 2) color gui.text_color substitute False


################################################################################
## Layar Galeri (Kerangka Kosong terhubung Persisten — PRD §4.7)
## 3 tab: Galeri Ending (5 kartu), Galeri CG (6 CG + 1 bonus), Ruang Musik (6 BGM).
################################################################################

screen gallery():
    tag menu
    default gallery_tab = "endings"

    use game_menu(ui_tr("gallery_title"), scroll="viewport"):

        ## Tab switcher.
        hbox:
            spacing 16
            textbutton ui_tr("tab_endings") style "tab_button" action SetScreenVariable("gallery_tab", "endings") selected (gallery_tab == "endings")
            textbutton ui_tr("tab_cg") style "tab_button" action SetScreenVariable("gallery_tab", "cg") selected (gallery_tab == "cg")
            textbutton ui_tr("tab_music") style "tab_button" action SetScreenVariable("gallery_tab", "music") selected (gallery_tab == "music")

        ## TAB 1: Galeri Ending (5 kartu kanonik)
        if gallery_tab == "endings":
            hbox:
                xfill True
                spacing 20
                text ui_tr("gallery_endings_hint") style "pref_note" yalign 0.5
                if config.developer:
                    textbutton ui_tr("gallery_open_debug") style "pill_button" xalign 1.0 action ShowMenu("ending_debug")

            vbox:
                xfill True
                spacing 18

                for entry in ENDINGS_CATALOG:
                    $ _rec = get_ending_record(entry["id"])
                    $ _unlocked = _rec is not None

                    frame:
                        xfill True
                        background Solid(UI_BG_CARD if _unlocked else UI_BG_CARD_LOCKED)
                        padding (28, 22)

                        hbox:
                            spacing 24
                            xfill True

                            add "images/ui/ui_ikon_kaset.png":
                                xysize (64, 64)
                                fit "contain"
                                yalign 0.5
                                alpha (1.0 if _unlocked else 0.30)

                            vbox:
                                spacing 6
                                xfill True
                                yalign 0.5

                                if _unlocked:
                                    hbox:
                                        spacing 14
                                        text ui_tr(entry["title_key"]) size 30 bold True color gui.selected_color
                                        text ("[" + ui_tr(entry["tag_key"]) + "]") size 22 color gui.accent_color yalign 0.5 substitute False
                                    text ui_tr("ending_unlocked_date", date=_rec.get("unlocked_at", "—")) size 22 color UI_TEXT_MUTED
                                    text ui_tr("ending_sample_choices", code=(_rec.get("sample_choices") or "------------")) size 22 color gui.text_color
                                else:
                                    text ui_tr("unknown_title") size 30 bold True color UI_TEXT_DIM
                                    text ui_tr("locked") size 22 color UI_TEXT_DIM

        ## TAB 2: Galeri CG (12 CG kanonik + 1 slot bonus Bab 48)
        elif gallery_tab == "cg":
            text ui_tr("gallery_cg_hint") style "pref_note"

            grid 3 6:
                allow_underfull True
                xfill True
                spacing 24

                for entry in CG_CATALOG:
                    $ _seen = is_cg_seen(entry["id"])

                    frame:
                        xsize 450
                        ysize 316
                        background Solid(UI_BG_CARD if _seen else UI_BG_CARD_LOCKED)
                        padding (14, 14)

                        vbox:
                            spacing 10
                            xfill True

                            if _seen:
                                button:
                                    xsize 422
                                    ysize 237
                                    padding (0, 0)
                                    background Solid("#120d0a")
                                    action Show("cg_viewer", cg_file=entry["file"], cg_title_key=entry["title_key"])
                                    add entry["file"] xysize (422, 237) fit "cover"
                                text ui_tr(entry["title_key"]) size 22 color gui.text_color
                            else:
                                frame:
                                    xsize 422
                                    ysize 237
                                    background Solid("#15100d")
                                    add "images/ui/ui_ikon_kaset.png" xysize (64, 64) fit "contain" align (0.5, 0.5) alpha 0.25
                                text ui_tr("unknown_title") size 22 color UI_TEXT_DIM

            ## Slot Bonus Bab 48 (PRD §4.7 — terbuka bila K2=B di Happy-True; dapat diputar ulang dari galeri).
            frame:
                xfill True
                background Solid(UI_BG_CARD if persistent.bonus_ch48_unlocked else UI_BG_CARD_LOCKED)
                padding (28, 22)

                hbox:
                    xfill True
                    spacing 20
                    add "images/ui/ui_ikon_kaset.png" xysize (52, 52) fit "contain" yalign 0.5 alpha (1.0 if persistent.bonus_ch48_unlocked else 0.28)
                    vbox:
                        spacing 6
                        yalign 0.5
                        text (ui_tr("cg_bonus_ch48") if persistent.bonus_ch48_unlocked else ui_tr("unknown_title")) size 26 bold True color (gui.selected_color if persistent.bonus_ch48_unlocked else UI_TEXT_DIM)
                        text (ui_tr("unlocked") if persistent.bonus_ch48_unlocked else ui_tr("cg_bonus_locked_hint")) size 22 color UI_TEXT_MUTED
                    if persistent.bonus_ch48_unlocked:
                        textbutton ui_tr("cg_bonus_play"):
                            style "pill_button"
                            xalign 1.0
                            yalign 0.5
                            action (Start("bab_48_bonus") if main_menu else Confirm(ui_tr("cg_bonus_confirm_start"), Start("bab_48_bonus")))

        ## TAB 3: Ruang Musik (6 BGM sesuai aset_manifest.json)
        else:
            python:
                _playing_file = renpy.music.get_playing(channel="music")
                _playing_title = None
                for _t in BGM_CATALOG:
                    if _t["file"] == _playing_file:
                        _playing_title = ui_tr(_t["title_key"])
                        break

            frame:
                xfill True
                background Solid("#1a130fe0")
                padding (24, 16)
                if _playing_title:
                    text ui_tr("music_now_playing", title=_playing_title) size 24 color gui.selected_color
                else:
                    text ui_tr("music_idle") size 24 color UI_TEXT_MUTED

            vbox:
                xfill True
                spacing 14

                for track in BGM_CATALOG:
                    $ _is_playing = (_playing_file == track["file"])

                    frame:
                        xfill True
                        background Solid("#3d2c1ff5" if _is_playing else UI_BG_CARD)
                        padding (26, 18)

                        hbox:
                            xfill True
                            spacing 20

                            add "images/ui/ui_ikon_kaset.png" xysize (44, 44) fit "contain" yalign 0.5 alpha (1.0 if _is_playing else 0.65)
                            text ui_tr(track["title_key"]) size 28 color (gui.selected_color if _is_playing else gui.text_color) yalign 0.5

                            textbutton (ui_tr("music_stop") if _is_playing else ui_tr("music_play")):
                                style "pill_button"
                                xalign 1.0
                                action PlayGalleryBGM(track["file"], loop=track["loop"])


screen cg_viewer(cg_file, cg_title_key):
    modal True
    zorder 200

    add Solid("#0c0907f2")
    add cg_file xysize (1920, 1080) fit "contain" align (0.5, 0.5)

    frame:
        align (0.5, 0.96)
        background Solid("#1a120ee6")
        padding (28, 12)

        hbox:
            spacing 32
            text ui_tr(cg_title_key) size 26 color gui.text_color yalign 0.5
            textbutton ui_tr("btn_close") style "pill_button" action Hide("cg_viewer")

    key "game_menu" action Hide("cg_viewer")


################################################################################
## Layar Pencapaian / Achievements (Kerangka Kosong 17 Kanonik — PRD §4.6)
################################################################################

screen achievements():
    tag menu

    $ _ach_unlocked_count = len(persistent.achievements) if isinstance(persistent.achievements, dict) else 0

    use game_menu(ui_tr("achievements_title"), scroll="viewport"):

        frame:
            xfill True
            background Solid("#1a130fe0")
            padding (24, 16)
            text ui_tr("ach_progress", unlocked=_ach_unlocked_count, total=len(ACHIEVEMENTS_CATALOG)) size 26 bold True color gui.accent_color

        vbox:
            xfill True
            spacing 16

            for ach_id in ACHIEVEMENTS_CATALOG:
                $ _rec = get_achievement_record(ach_id)
                $ _opened = _rec is not None

                frame:
                    xfill True
                    background Solid(UI_BG_CARD if _opened else UI_BG_CARD_LOCKED)
                    padding (26, 20)

                    hbox:
                        spacing 22
                        xfill True

                        frame:
                            xsize 68
                            ysize 68
                            yalign 0.5
                            background Solid("#d49a58" if _opened else "#281e18")
                            add "images/ui/ui_ikon_kaset.png":
                                xysize (48, 48)
                                fit "contain"
                                align (0.5, 0.5)
                                alpha (1.0 if _opened else 0.25)

                        vbox:
                            spacing 6
                            xfill True
                            yalign 0.5

                            if _opened:
                                text ui_tr(ach_id + "_name") size 28 bold True color gui.selected_color
                                text ui_tr(ach_id + "_desc") size 23 color gui.text_color
                                text ui_tr("ach_unlocked_date", date=_rec.get("unlocked_at", "—")) size 20 color UI_TEXT_MUTED
                            else:
                                text ui_tr("unknown_title") size 28 bold True color UI_TEXT_DIM
                                text ui_tr(ach_id + "_hint") size 22 color UI_TEXT_MUTED


screen achievement_toast(ach_id):
    zorder 250

    frame:
        align (0.98, 0.04)
        xsize 520
        background Solid("#2a1e17f5")
        padding (22, 16)

        hbox:
            spacing 16
            add "images/ui/ui_ikon_kaset.png" xysize (48, 48) fit "contain" yalign 0.5
            vbox:
                spacing 4
                text ui_tr("ach_toast_header") size 20 bold True color gui.accent_color
                text ui_tr(ach_id + "_name") size 26 bold True color gui.text_color

    timer 4.0 action Function(_show_next_achievement_toast)


################################################################################
## Layar Kredit & Tentang (PRD §4.1 & Fase 7)
################################################################################

screen credits():
    tag menu

    use game_menu(ui_tr("credits_title"), scroll="viewport"):
        hbox:
            spacing 16
            textbutton ui_tr("credits_title") style "tab_button" selected True action NullAction()
            textbutton ui_tr("changelog_title") style "tab_button" action ShowMenu("changelog")
            textbutton ui_tr("credits_btn_about") style "tab_button" action ShowMenu("about")
            textbutton ui_tr("credits_btn_glossary") style "tab_button" action ShowMenu("glossary")

        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (40, 36)

            vbox:
                spacing 22
                xfill True

                text ui_tr("credits_subtitle") size 34 bold True color gui.selected_color
                frame:
                    xfill True
                    ysize 2
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                hbox:
                    spacing 24
                    text ui_tr("credits_story_label") size 26 bold True color gui.accent_color xminimum 280
                    text ui_tr("credits_story_val") size 26 color gui.text_color

                hbox:
                    spacing 24
                    text ui_tr("credits_studio_label") size 26 bold True color gui.accent_color xminimum 280
                    text ui_tr("credits_studio_val") size 26 bold True color gui.selected_color

                hbox:
                    spacing 24
                    text ui_tr("credits_contact_label") size 26 bold True color gui.accent_color xminimum 280
                    text ui_tr("credits_contact_val") size 25 color gui.text_color

                hbox:
                    spacing 24
                    text ui_tr("credits_engine_label") size 26 bold True color gui.accent_color xminimum 280
                    text ui_tr("credits_engine_val", ver=renpy.version_only) size 26 color gui.text_color

                hbox:
                    spacing 24
                    text ui_tr("credits_version_label") size 26 bold True color gui.accent_color xminimum 280
                    text "[config.version]" size 26 color gui.text_color

                null height 8
                frame:
                    xfill True
                    ysize 2
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                ## Daftar 5 nama ending kanonik (hanya tampilan daftar; ending TIDAK bisa dipilih manual).
                text ui_tr("credits_endings_heading") size 26 bold True color gui.accent_color

                vbox:
                    spacing 10
                    xfill True
                    for entry in ENDINGS_CATALOG:
                        hbox:
                            spacing 16
                            text entry["id"] size 23 bold True color gui.accent_color xminimum 52
                            text ui_tr(entry["title_key"]) size 24 color gui.selected_color
                            text ("(" + ui_tr(entry["tag_key"]) + ")") size 22 color UI_TEXT_MUTED yalign 0.5 substitute False

                null height 10
                text ui_tr("credits_note") style "pref_note"


screen changelog():
    tag menu

    use game_menu(ui_tr("changelog_title"), scroll="viewport"):
        hbox:
            spacing 16
            textbutton ui_tr("credits_title") style "tab_button" action ShowMenu("credits")
            textbutton ui_tr("changelog_title") style "tab_button" selected True action NullAction()
            textbutton ui_tr("credits_btn_about") style "tab_button" action ShowMenu("about")
            textbutton ui_tr("credits_btn_glossary") style "tab_button" action ShowMenu("glossary")

        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (40, 36)

            vbox:
                spacing 24
                xfill True

                text ui_tr("changelog_subtitle") size 34 bold True color gui.selected_color
                frame:
                    xfill True
                    ysize 2
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                vbox:
                    spacing 10
                    xfill True
                    text ui_tr("changelog_v104_title") size 27 bold True color gui.accent_color
                    text ui_tr("changelog_v104_body") size 24 color gui.text_color line_spacing 8

                frame:
                    xfill True
                    ysize 1
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                vbox:
                    spacing 10
                    xfill True
                    text ui_tr("changelog_v103_title") size 27 bold True color gui.accent_color
                    text ui_tr("changelog_v103_body") size 24 color gui.text_color line_spacing 8

                frame:
                    xfill True
                    ysize 1
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                vbox:
                    spacing 10
                    xfill True
                    text ui_tr("changelog_v102_title") size 27 bold True color gui.accent_color
                    text ui_tr("changelog_v102_body") size 24 color gui.text_color line_spacing 8

                frame:
                    xfill True
                    ysize 1
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                vbox:
                    spacing 10
                    xfill True
                    text ui_tr("changelog_v101_title") size 27 bold True color gui.accent_color
                    text ui_tr("changelog_v101_body") size 24 color gui.text_color line_spacing 8

                frame:
                    xfill True
                    ysize 1
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                vbox:
                    spacing 10
                    xfill True
                    text ui_tr("changelog_v100_title") size 27 bold True color gui.accent_color
                    text ui_tr("changelog_v100_body") size 24 color gui.text_color line_spacing 8


screen about():
    tag menu

    use game_menu(ui_tr("about_title"), scroll="viewport"):
        hbox:
            spacing 16
            textbutton ui_tr("about_btn_credits") style "tab_button" action ShowMenu("credits")
            textbutton ui_tr("changelog_title") style "tab_button" action ShowMenu("changelog")
            textbutton ui_tr("about_title") style "tab_button" selected True action NullAction()
            textbutton ui_tr("credits_btn_glossary") style "tab_button" action ShowMenu("glossary")

        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (40, 36)

            vbox:
                spacing 20
                xfill True

                text ui_tr("about_synopsis_title") size 32 bold True color gui.selected_color
                text ui_tr("about_synopsis_body") size 25 color gui.text_color line_spacing 8

                frame:
                    xfill True
                    ysize 2
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                text ui_tr("about_system_title") size 28 bold True color gui.accent_color
                text ui_tr("about_system_body") size 24 color gui.text_color line_spacing 8

                frame:
                    xfill True
                    ysize 2
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                text ui_tr("about_controls_title") size 28 bold True color gui.accent_color
                text ui_tr("about_controls_body") size 24 color gui.text_color line_spacing 8

                frame:
                    xfill True
                    ysize 2
                    padding (0, 0)
                    background Solid(UI_BORDER_SUBTLE)

                hbox:
                    spacing 24
                    text ui_tr("credits_story_label") size 24 bold True color gui.accent_color xminimum 240
                    text ui_tr("credits_story_val") size 24 color gui.text_color

                hbox:
                    spacing 24
                    text ui_tr("credits_version_label") size 24 bold True color gui.accent_color xminimum 240
                    text "[config.version]" size 24 color gui.text_color


screen glossary():
    tag menu

    $ _gl_lang = "en" if (persistent.ui_lang == "en") else "id"

    use game_menu(ui_tr("glossary_title"), scroll="viewport"):
        hbox:
            spacing 16
            textbutton ui_tr("about_btn_credits") style "tab_button" action ShowMenu("credits")
            textbutton ui_tr("credits_btn_about") style "tab_button" action ShowMenu("about")
            textbutton ui_tr("credits_btn_glossary") style "tab_button" selected True action NullAction()

        frame:
            xfill True
            background Solid("#1a130fe0")
            padding (28, 20)

            vbox:
                spacing 8
                xfill True
                text ui_tr("glossary_intro") size 24 color gui.text_color line_spacing 6
                text ui_tr("glossary_count_note", count=len(GLOSSARY_ENTRIES)) style "pref_note"

        vbox:
            xfill True
            spacing 14

            for item in GLOSSARY_ENTRIES:
                frame:
                    xfill True
                    background Solid(UI_BG_CARD)
                    padding (28, 18)

                    vbox:
                        spacing 6
                        xfill True
                        text item["term"] size 27 bold True color gui.selected_color substitute False
                        text item[_gl_lang] size 23 color gui.text_color line_spacing 6 substitute False


## Kartu Penutup Ending (hanya ditampilkan otomatis saat playthrough mencapai akhir cerita).
screen ending_card(ending_id, choice_code):
    modal True
    zorder 190

    $ _entry = None
    python:
        for _e in ENDINGS_CATALOG:
            if _e["id"] == ending_id:
                _entry = _e
                break

    add Solid("#0e0a08f0")

    frame:
        align (0.5, 0.5)
        xsize 980
        background Solid("#221914fa")
        padding (56, 48)

        vbox:
            xfill True
            spacing 22

            add "images/ui/ui_ikon_kaset.png":
                xysize (72, 72)
                fit "contain"
                xalign 0.5

            text ui_tr("ending_card_header") size 22 bold True color gui.accent_color xalign 0.5

            if _entry is not None:
                text ui_tr(_entry["title_key"]) size 42 bold True color gui.selected_color xalign 0.5 text_align 0.5
                text ("(" + ui_tr(_entry["tag_key"]) + ")") size 26 color gui.accent_color xalign 0.5 substitute False

            frame:
                xfill True
                ysize 2
                padding (0, 0)
                background Solid(UI_BORDER_SUBTLE)

            text ui_tr("ending_sample_choices", code=(choice_code or "------------")) size 24 color UI_TEXT_MUTED xalign 0.5 substitute False

            null height 10
            textbutton ui_tr("ending_card_return_menu"):
                style "pill_button"
                xalign 0.5
                action Return()


################################################################################
## Modal Konfirmasi, Notifikasi, & Indikator Skip
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 300

    add Solid("#0d0907cc")

    frame:
        align (0.5, 0.5)
        xsize 760
        background Solid("#261c16fa")
        padding (48, 40)

        vbox:
            xfill True
            spacing 32

            text ui_confirm_text(message):
                size 30
                color gui.text_color
                xalign 0.5
                text_align 0.5

            hbox:
                xalign 0.5
                spacing 28

                textbutton ui_tr("confirm_yes") style "pill_button" action yes_action
                textbutton ui_tr("confirm_no") style "pill_button" action no_action

    key "game_menu" action no_action


screen notify(message):
    zorder 240

    frame:
        align (0.5, 0.06)
        background Solid("#261c16eb")
        padding (28, 14)
        text ui_confirm_text(message) size 24 color gui.selected_color

    timer 3.0 action Hide("notify")


screen skip_indicator():
    zorder 150

    frame:
        align (0.02, 0.03)
        background Solid("#241a15e6")
        padding (20, 10)
        text ui_tr("skipping") size 22 bold True color gui.accent_color
