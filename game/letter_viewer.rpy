init -5 python:

    LETTER_LAYOUTS = {
        "cg_surat_lama": {
            "xpos": 520, "ypos": 215, "xsize": 890, "ysize": 640,
            "font_size": 27, "title_size": 24, "spacing": 24, "line_spacing": 10,
            "ink": "#2e1f14", "title_color": "#6b4423", "rule_color": "#a87e4f88",
        },
        "cg_surat_perpisahan": {
            "xpos": 655, "ypos": 350, "xsize": 705, "ysize": 540,
            "font_size": 24, "title_size": 22, "spacing": 18, "line_spacing": 8,
            "ink": "#221c18", "title_color": "#5c4330", "rule_color": "#9e867088",
        },
        "cg_surat_yara": {
            "xpos": 720, "ypos": 250, "xsize": 505, "ysize": 690,
            "font_size": 21, "title_size": 21, "spacing": 14, "line_spacing": 7,
            "ink": "#231b15", "title_color": "#6b472a", "rule_color": "#a8835a88",
        },
        "cg_surat_balasan_yara": {
            "xpos": 755, "ypos": 270, "xsize": 410, "ysize": 600,
            "font_size": 28, "title_size": 20, "spacing": 16, "line_spacing": 10,
            "ink": "#221c18", "title_color": "#5c4330", "rule_color": "#9e867088",
        },
    }

    _LETTER_DEFAULT_LAYOUT = {
        "xpos": 560, "ypos": 220, "xsize": 800, "ysize": 640,
        "font_size": 25, "title_size": 22, "spacing": 20, "line_spacing": 8,
        "ink": "#261a12", "title_color": "#6b472a", "rule_color": "#b58c5f88",
    }

    def _tr_letter(s):
        if not s:
            return s
        lang = "en" if persistent.story_lang == "en" else None
        return renpy.translate_string(str(s), language=lang)

    def _record_letter_to_history(title, paragraphs):
        t = _tr_letter(title)
        if t:
            narrator.add_history(kind="adv", who=t, what="\n".join(_tr_letter(p) for p in paragraphs if p))

screen letter_viewer(cg_id, letter_title, paragraphs, centered_mode=False, paper_bg=None):
    modal True
    zorder 90

    $ _lay = LETTER_LAYOUTS.get(cg_id, _LETTER_DEFAULT_LAYOUT)
    $ _bx = _lay["xpos"]
    $ _by = _lay["ypos"]
    $ _bw = _lay["xsize"]
    $ _bh = _lay["ysize"]
    $ _tr_title = _tr_letter(letter_title)
    $ _tr_paragraphs = [_tr_letter(p) for p in paragraphs]

    add cg_id xysize (1920, 1080) fit "cover"

    button:
        xpos 0
        ypos 0
        xsize 1920
        ysize 1080
        background None
        hover_background None
        action Return(True)

    key "K_SPACE" action Return(True)
    key "K_RETURN" action Return(True)
    key "K_KP_ENTER" action Return(True)
    key "K_ESCAPE" action Return(True)

    fixed:
        xpos _bx
        ypos _by
        xsize _bw
        ysize _bh

        viewport:
            xsize _bw
            ysize _bh
            clipping True
            mousewheel True
            draggable True

            if centered_mode:
                frame:
                    xsize _bw
                    yminimum _bh
                    background None
                    padding (12, 12)
                    vbox:
                        xfill True
                        yalign 0.5
                        spacing _lay["spacing"]
                        for p in _tr_paragraphs:
                            text p size scaled_font_size(_lay["font_size"]) italic True color _lay["ink"] xalign 0.5 text_align 0.5 line_spacing _lay["line_spacing"] substitute False
            else:
                vbox:
                    xsize _bw
                    spacing _lay["spacing"]

                    if _tr_title:
                        vbox:
                            spacing 8
                            xsize _bw
                            text _tr_title size scaled_font_size(_lay["title_size"]) bold True color _lay["title_color"] substitute False
                            add Solid(_lay["rule_color"]) xsize _bw ysize 2

                    for p in _tr_paragraphs:
                        text p size scaled_font_size(_lay["font_size"]) italic True color _lay["ink"] line_spacing _lay["line_spacing"] substitute False

    frame:
        xalign 0.5
        yalign 0.968
        background Solid("#16100cc8")
        padding (28, 10)
        text ui_tr("letter_continue_hint") size 21 color "#e6d5be"

label show_letter(cg_id, letter_title="", paragraphs=None, centered_mode=False, paper_bg=None):
    $ stop_skip_and_auto()
    $ hide_item()
    $ renpy.hide_screen("chapter_banner")
    $ mark_cg_seen(cg_id)
    $ _letter_paras = paragraphs or []
    $ _record_letter_to_history(letter_title, _letter_paras)

    $ _prev_qm = getattr(store, "quick_menu", True)
    $ store.quick_menu = False
    play sound sfx_kertas_surat
    window hide
    call screen letter_viewer(
        cg_id=cg_id,
        letter_title=letter_title,
        paragraphs=_letter_paras,
        centered_mode=centered_mode,
        paper_bg=paper_bg,
    ) with dissolve
    $ store.quick_menu = _prev_qm
    window show
    return
