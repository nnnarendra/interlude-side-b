## Interlude / Side B — Komponen Pemutar Kaset yang Dipakai Ulang (PRD §4.8 & Fase 2)
## - Memutar berkas dari `game/audio/kaset/` sesuai `aset_manifest.json` pada kanal `"kaset"`.
## - Transkrip teks SELALU tampil di layar (audio bukan satu-satunya pembawa isi).
## - Skip dan Auto-Play WAJIB berhenti saat memasuki adegan pemutaran kaset.

## Registri 5 kaset kanonik (nama berkas persis sesuai aset_manifest.json).
define CASSETTE_CATALOG = {
    "kaset_besok_busarah": {
        "file": "audio/kaset/kaset_besok_busarah.ogg",
        "title_key": "cassette_name_busarah",
        "default_duration": 12,
        "is_silent": False,
    },
    "kaset_hening_60detik": {
        "file": "audio/kaset/kaset_hening_60detik.ogg",
        "title_key": "cassette_name_hening",
        "default_duration": 60,
        "is_silent": True,
    },
    "kaset_tangis_yara": {
        "file": "audio/kaset/kaset_tangis_yara.ogg",
        "title_key": "cassette_name_yara",
        "default_duration": 8,
        "is_silent": False,
    },
    "kaset_tawa_siti": {
        "file": "audio/kaset/kaset_tawa_siti.ogg",
        "title_key": "cassette_name_siti",
        "default_duration": 12,
        "is_silent": False,
    },
    "kaset_ultah_kai_yara": {
        "file": "audio/kaset/kaset_ultah_kai_yara.ogg",
        "title_key": "cassette_name_ultah",
        "default_duration": 18,
        "is_silent": False,
    },
    "kaset_pesan_ageng": {
        "file": "audio/kaset/kaset_pesan_ageng.ogg",
        "title_key": "cassette_name_ageng",
        "default_duration": 45,
        "is_silent": False,
    },
}

init -8 python:
    def format_tape_mmss(seconds):
        sec = max(0, int(seconds))
        return "{:02d}:{:02d}".format(sec // 60, sec % 60)

    def normalize_transcript_lines(transcript_lines, cassette_id=None):
        """Pastikan transkrip selalu berupa daftar tuple `(speaker, text)` dan tidak pernah kosong."""
        result = []
        if transcript_lines:
            for item in transcript_lines:
                if isinstance(item, (tuple, list)) and len(item) >= 2:
                    result.append((item[0], str(item[1])))
                elif item is not None:
                    result.append((None, str(item)))
        if not result:
            meta = CASSETTE_CATALOG.get(cassette_id, {})
            if meta.get("is_silent"):
                result.append((None, ui_tr("cassette_transcript_silent_default")))
            else:
                result.append((None, ui_tr("cassette_transcript_empty_default")))
        return result

    def _record_cassette_transcript_to_history(lines):
        """Catat isi transkrip kaset ke backlog/history agar pemain bisa membacanya kembali."""
        for speaker, text in lines:
            if text:
                narrator.add_history(kind="adv", who=speaker, what=text)

    def _cassette_start_playback(cassette_id, preview_only=False):
        stop_skip_and_auto()
        meta = CASSETTE_CATALOG.get(cassette_id)
        if not meta:
            return
        renpy.sound.play("audio/sfx/sfx_klik_play.ogg", channel="sound")
        renpy.music.play(meta["file"], channel="kaset", loop=False)
        if not preview_only:
            hook_cassette_played(cassette_id)

    def _cassette_stop_playback():
        renpy.music.stop(channel="kaset", fadeout=0.2)

    class CassettePlayAction(Action, DictEquality):
        def __init__(self, cassette_id, preview_only=False):
            self.cassette_id = cassette_id
            self.preview_only = preview_only

        def __call__(self):
            _cassette_start_playback(self.cassette_id, preview_only=self.preview_only)
            cs = renpy.current_screen()
            if cs is not None:
                cs.scope["is_playing"] = True
                cs.scope["has_played"] = True
                cs.scope["elapsed_sec"] = 0
                cs.scope["completed_unskipped"] = False
            renpy.restart_interaction()

    class CassetteStopAction(Action, DictEquality):
        def __call__(self):
            _cassette_stop_playback()
            cs = renpy.current_screen()
            if cs is not None:
                cs.scope["is_playing"] = False
            renpy.restart_interaction()

    class CassetteTickAction(Action, DictEquality):
        def __init__(self, cassette_id, duration_sec, preview_only=False):
            self.cassette_id = cassette_id
            self.duration_sec = max(1, int(duration_sec))
            self.preview_only = preview_only

        def __call__(self):
            cs = renpy.current_screen()
            if cs is None or not cs.scope.get("is_playing"):
                return
            nxt = cs.scope.get("elapsed_sec", 0) + 1
            if nxt >= self.duration_sec:
                cs.scope["elapsed_sec"] = self.duration_sec
                cs.scope["is_playing"] = False
                cs.scope["completed_unskipped"] = True
                _cassette_stop_playback()
                if not self.preview_only:
                    hook_cassette_finished(self.cassette_id, completed_unskipped=True)
            else:
                cs.scope["elapsed_sec"] = nxt
            renpy.restart_interaction()

    class CassetteFinishAction(Action, DictEquality):
        def __init__(self, cassette_id, lines, is_overlay_preview=False):
            self.cassette_id = cassette_id
            self.lines = lines
            self.is_overlay_preview = is_overlay_preview

        def __call__(self):
            _cassette_stop_playback()
            cs = renpy.current_screen()
            has_played = bool(cs.scope.get("has_played")) if cs is not None else False
            completed_unskipped = bool(cs.scope.get("completed_unskipped")) if cs is not None else False
            if self.is_overlay_preview:
                renpy.hide_screen("cassette_player")
                renpy.restart_interaction()
                return None
            if has_played and not completed_unskipped:
                hook_cassette_finished(self.cassette_id, completed_unskipped=False)
            _record_cassette_transcript_to_history(self.lines)
            return {
                "cassette_id": self.cassette_id,
                "played": has_played,
                "completed_unskipped": completed_unskipped,
            }


screen cassette_player(
    cassette_id,
    label_title=None,
    transcript_lines=None,
    duration_sec=None,
    allow_skip=True,
    is_overlay_preview=False,
):
    modal True
    zorder 180

    $ _meta = CASSETTE_CATALOG.get(cassette_id, {})
    $ _dur = int(duration_sec if duration_sec is not None else _meta.get("default_duration", 60))
    $ _title = label_title if label_title else ui_tr(_meta.get("title_key", "cassette_default_title"))
    $ _lines = normalize_transcript_lines(transcript_lines, cassette_id=cassette_id)

    default is_playing = False
    default has_played = False
    default elapsed_sec = 0
    default completed_unskipped = False

    ## Wajib hentikan skip & auto-play segera saat layar kaset muncul (PRD §4.4).
    on "show" action Function(stop_skip_and_auto)
    on "hide" action Function(_cassette_stop_playback)

    if is_playing:
        timer 1.0 repeat True action CassetteTickAction(cassette_id, _dur, preview_only=is_overlay_preview)

    add Solid("#0e0a08d9")

    frame:
        align (0.5, 0.5)
        xsize 1320
        ysize 840
        background Solid("#221914fa")
        padding (44, 38)

        vbox:
            xfill True
            yfill True
            spacing 24

            ## Header dek pemutar kaset
            hbox:
                xfill True
                spacing 22

                frame:
                    xsize 88
                    ysize 88
                    yalign 0.5
                    background Solid("#d49a58" if is_playing else "#33251d")
                    padding (10, 10)
                    add "images/ui/ui_ikon_kaset.png":
                        xysize (64, 64)
                        fit "contain"
                        align (0.5, 0.5)

                vbox:
                    spacing 6
                    yalign 0.5
                    text ui_tr("cassette_deck_label") size 22 bold True color gui.accent_color
                    text _title size 34 bold True color gui.selected_color substitute False

                    if is_playing:
                        text ui_tr("cassette_status_playing") size 22 color "#f6c987"
                    elif completed_unskipped:
                        text ui_tr("cassette_status_done") size 22 color gui.accent_color
                    else:
                        text ui_tr("cassette_status_ready") size 22 color UI_TEXT_MUTED

                ## Penghitung waktu pita (MM:SS / MM:SS)
                text (format_tape_mmss(elapsed_sec) + " / " + format_tape_mmss(_dur)):
                    size 28
                    bold True
                    color gui.text_color
                    xalign 1.0
                    yalign 0.5

            ## Bilah progres pita kaset
            bar value StaticValue(elapsed_sec, _dur):
                xfill True
                ysize 16
                left_bar Solid("#d49a58")
                right_bar Solid("#3d2e24")

            ## Tombol kendali pemutar kaset (Putar / Berhenti / Selesai)
            hbox:
                xfill True
                spacing 16

                textbutton (ui_tr("cassette_btn_replay") if (has_played and not is_playing) else ui_tr("cassette_btn_play")):
                    style "pill_button"
                    sensitive (not is_playing)
                    action CassettePlayAction(cassette_id, preview_only=is_overlay_preview)

                textbutton ui_tr("cassette_btn_stop"):
                    style "pill_button"
                    sensitive is_playing
                    action CassetteStopAction()

                $ _can_close = allow_skip or completed_unskipped or is_overlay_preview
                textbutton (ui_tr("btn_close") if is_overlay_preview else ui_tr("cassette_btn_continue")):
                    style "pill_button"
                    xalign 1.0
                    sensitive _can_close
                    action CassetteFinishAction(cassette_id, _lines, is_overlay_preview=is_overlay_preview)

            ## Area transkrip teks — SELALU tampil agar cerita utuh meski tanpa suara (PRD §4.8)
            frame:
                xfill True
                yfill True
                background Solid("#16100ce8")
                padding (30, 24)

                vbox:
                    xfill True
                    yfill True
                    spacing 14

                    hbox:
                        xfill True
                        text ui_tr("cassette_transcript_header") size 24 bold True color gui.accent_color
                        text ui_tr("cassette_transcript_always_on") size 20 color UI_TEXT_MUTED xalign 1.0 yalign 0.5

                    frame:
                        xfill True
                        ysize 2
                        padding (0, 0)
                        background Solid(UI_BORDER_SUBTLE)

                    viewport:
                        xfill True
                        yfill True
                        scrollbars "vertical"
                        vscrollbar_unscrollable "hide"
                        mousewheel True
                        draggable True
                        pagekeys True

                        vbox:
                            xfill True
                            spacing 16

                            for speaker, line_text in _lines:
                                vbox:
                                    spacing 4
                                    xfill True
                                    if speaker:
                                        text speaker size scaled_font_size(26) bold True color gui.accent_color substitute False
                                    text line_text size scaled_font_size(gui.text_size) color gui.text_color line_spacing 6 substitute False

    if is_overlay_preview:
        key "game_menu" action CassetteFinishAction(cassette_id, _lines, is_overlay_preview=True)


## Label pembantu yang dipakai ulang oleh adegan cerita pada fase berikutnya:
## Contoh pemanggilan di naskah:
##     call play_cassette("kaset_besok_busarah", label_title="...", transcript_lines=[...])
label play_cassette(cassette_id, label_title=None, transcript_lines=None, duration_sec=None, allow_skip=True):
    $ stop_skip_and_auto()
    call screen cassette_player(
        cassette_id=cassette_id,
        label_title=label_title,
        transcript_lines=transcript_lines,
        duration_sec=duration_sec,
        allow_skip=allow_skip,
        is_overlay_preview=False,
    )
    return _return
