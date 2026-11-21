init -12 python:

    ENDING_GERBANG = [
        ("G1",  {"A": (1, 0, 0, 1, 1), "B": (0, 1, 1, 0, 0), "C": (0, 2, 0, 0, 0)}),
        ("G2",  {"A": (1, 0, 0, 1, 0), "B": (1, 1, 0, 0, 0), "C": (0, 0, 1, 1, 0)}),
        ("G3",  {"A": (1, 1, 0, 0, 0), "B": (0, 0, 1, 0, 0), "C": (0, 0, 0, 1, 1)}),
        ("G4",  {"A": (2, 2, 0, 0, 0), "B": (0, 1, 1, 0, 0), "C": (0, 0, 0, 1, 1)}),
        ("G5",  {"A": (1, 0, 0, 0, 0), "B": (0, 0, 1, 0, 0), "C": (0, 0, 0, 0, 1)}),
        ("G6",  {"A": (2, 1, 0, 0, 0), "B": (0, 0, 1, 0, 0), "C": (0, 0, 0, 1, 1)}),
        ("G7",  {"A": (1, 2, 0, 0, 0), "B": (0, 0, 1, 0, 0), "C": (0, 0, 0, 1, 0)}),
        ("G8",  {"A": (2, 0, 0, 0, 0), "B": (0, 2, 0, 0, 0), "C": (0, 0, 1, 1, 2)}),
        ("G9",  {"A": (3, 0, 0, 1, 3), "B": (0, 0, 2, 0, 0), "C": (0, 3, 0, 0, 0)}),
        ("G10", {"A": (3, 2, 0, 0, 0), "B": (0, 0, 3, 0, 1), "C": (0, 0, 0, 3, 3)}),
        ("G11", {"A": (2, 2, 0, 0, 0), "B": (0, 0, 2, 0, 0), "C": (0, 0, 0, 3, 1)}),
        ("G12", {"A": (3, 2, 0, 0, 0), "B": (0, 0, 2, 0, 3), "C": (0, 0, 0, 3, 0)}),
    ]

    ENDING_INDEX_TO_ID = ("H1", "H2", "G", "S1", "S2")

    ENDING_INDEX_TO_TITLE_KEY = (
        "ending_h1_title",
        "ending_h2_title",
        "ending_g_title",
        "ending_s1_title",
        "ending_s2_title",
    )

    ENDING_INDEX_TO_TAG_KEY = (
        "ending_h1_tag",
        "ending_h2_tag",
        "ending_g_tag",
        "ending_s1_tag",
        "ending_s2_tag",
    )

    def validasi_string12(string12):
        """Kembalikan string 12 huruf A/B/C yang dinormalisasi, atau None jika tidak valid."""
        if not isinstance(string12, str):
            return None
        s = string12.strip().upper()
        if len(s) != 12 or not (set(s) <= set("ABC")):
            return None
        return s

    def nilai_ending_raw(string12):
        """
        Port PERSIS fungsi `nilai(rangkaian)` dari `ending_sim.py`.
        Mengembalikan tuple `(ending_index, skor_list)` dengan indeks 0..4:
        0=H1 (Happy-True), 1=H2 (Happy-Sehat), 2=G (Gantung), 3=S1 (Sad-Pasif), 4=S2 (Sad-Ironis).
        Flag minor (m01-m23) dan kondisional (K1/K2) TIDAK pernah dibaca di sini.
        """
        rangkaian = validasi_string12(string12)
        if rangkaian is None:
            raise ValueError("Rangkaian harus 12 huruf A/B/C")

        skor = [0] * 5
        for (_kode, tabel), huruf in zip(ENDING_GERBANG, rangkaian):
            poin = tabel[huruf]
            skor = [s + p for s, p in zip(skor, poin)]

        if (rangkaian[8], rangkaian[9], rangkaian[11]) == ("A", "C", "B"):
            return 4, skor

        layak = [True] * 5
        if rangkaian[8] != "A":
            layak[0] = False
            layak[4] = False
        if rangkaian[8] == "A":
            layak[1] = False

        if rangkaian[9] == "C" and rangkaian[11] == "C":
            layak[0] = False
            layak[1] = False

        kandidat = sorted(((skor[i], i) for i in range(5) if layak[i]), reverse=True)
        (skor1, e1), (skor2, e2) = kandidat[0], kandidat[1]

        pola_true = (
            rangkaian[5] == "A"
            and rangkaian[8] == "A"
            and rangkaian[9] == "A"
            and rangkaian[11] == "A"
        )
        if skor1 - skor2 == 0 and layak[2] and not (e1 == 0 and pola_true):
            return 2, skor

        return e1, skor

    def nilai_ending(string12):
        """
        Penilai ending utama untuk Ren'Py.
        Menggunakan logika `nilai_ending_raw(string12)` yang 100% identik dengan `ending_sim.py`,
        dan mengembalikan kamus hasil lengkap untuk kebutuhan cerita, galeri, dan mode debug.
        """
        rangkaian = validasi_string12(string12)
        if rangkaian is None:
            raise ValueError("Rangkaian harus 12 huruf A/B/C")

        idx, skor = nilai_ending_raw(rangkaian)

        pola_khusus_acb = (rangkaian[8], rangkaian[9], rangkaian[11]) == ("A", "C", "B")
        layak = [True] * 5
        if rangkaian[8] != "A":
            layak[0] = False
            layak[4] = False
        if rangkaian[8] == "A":
            layak[1] = False
        aturan_kritis_cc = (rangkaian[9] == "C" and rangkaian[11] == "C")
        if aturan_kritis_cc:
            layak[0] = False
            layak[1] = False
        pola_true = (
            rangkaian[5] == "A"
            and rangkaian[8] == "A"
            and rangkaian[9] == "A"
            and rangkaian[11] == "A"
        )

        if pola_khusus_acb:
            alasan_key = "debug_reason_layer2_acb"
        else:
            kandidat = sorted(((skor[i], i) for i in range(5) if layak[i]), reverse=True)
            (skor1, e1), (skor2, _e2) = kandidat[0], kandidat[1]
            if skor1 - skor2 == 0 and layak[2] and not (e1 == 0 and pola_true):
                alasan_key = "debug_reason_layer5_tie"
            elif skor1 - skor2 == 0 and e1 == 0 and pola_true:
                alasan_key = "debug_reason_layer5_true_override"
            else:
                alasan_key = "debug_reason_layer5_score"

        return {
            "index": idx,
            "id": ENDING_INDEX_TO_ID[idx],
            "title_key": ENDING_INDEX_TO_TITLE_KEY[idx],
            "tag_key": ENDING_INDEX_TO_TAG_KEY[idx],
            "scores": tuple(skor),
            "eligible": tuple(layak),
            "string": rangkaian,
            "pola_khusus_acb": pola_khusus_acb,
            "aturan_kritis_cc": aturan_kritis_cc,
            "pola_true": pola_true,
            "reason_key": alasan_key,
        }

    def evaluate_current_ending(unlock=True):
        """Nilai ending dari 12 gerbang playthrough aktif; opsional buka di data persisten."""
        s = get_choice_string()
        res = nilai_ending(s)
        if unlock:
            unlock_ending(res["id"], choice_string=res["string"])
        return res

    class EndingDebugInputValue(InputValue):
        def __init__(self):
            self.default = False

        def get_text(self):
            return getattr(store, "_debug_ending_input", "AAAAAAAAAAAA")

        def set_text(self, s):
            cleaned = "".join(ch for ch in s.upper() if ch in "ABC")[:12]
            store._debug_ending_input = cleaned
            renpy.restart_interaction()

        def enter(self):
            renpy.run(self.Disable())
            raise renpy.IgnoreEvent()

    class SetDebugGateChar(Action, DictEquality):
        """Ubah satu huruf (G1..G12) pada string uji di layar Mode Debug."""
        def __init__(self, idx, char):
            self.idx = idx
            self.char = char

        def __call__(self):
            cur = getattr(store, "_debug_ending_input", "AAAAAAAAAAAA").upper()
            chars = list(cur.ljust(12, "A")[:12])
            for i in range(12):
                if chars[i] not in ("A", "B", "C"):
                    chars[i] = "A"
            chars[self.idx] = self.char
            store._debug_ending_input = "".join(chars)
            renpy.restart_interaction()

        def get_selected(self):
            cur = getattr(store, "_debug_ending_input", "").upper()
            return len(cur) > self.idx and cur[self.idx] == self.char

    class SetDebugString(Action, DictEquality):
        def __init__(self, value):
            self.value = value

        def __call__(self):
            store._debug_ending_input = self.value
            renpy.restart_interaction()

        def get_selected(self):
            return getattr(store, "_debug_ending_input", "").upper() == self.value.upper()

default _debug_ending_input = "AAAAAAAAAAAA"

screen ending_debug():
    tag menu

    $ _input_val = EndingDebugInputValue()
    $ _raw_str = _debug_ending_input
    $ _valid_str = validasi_string12(_raw_str)
    $ _eval_res = nilai_ending(_valid_str) if _valid_str is not None else None

    use game_menu(ui_tr("debug_ending_title"), scroll="viewport"):

        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (32, 26)

            vbox:
                xfill True
                spacing 18

                text ui_tr("debug_input_label") style "section_title"

                hbox:
                    spacing 20

                    button:
                        xsize 460
                        yminimum 62
                        background Solid("#16100ce6")
                        hover_background Solid("#221913f2")
                        padding (22, 12)
                        action _input_val.Toggle()
                        input value _input_val length 12 allow "ABCabc" size 34 color gui.selected_color

                    text ui_tr("debug_char_count", count=len(_raw_str)) size 24 color (gui.accent_color if _valid_str else "#e07a68") yalign 0.5

                hbox:
                    spacing 12
                    box_wrap True
                    box_wrap_spacing 10

                    textbutton ui_tr("debug_preset_h1") style "pill_button" action SetDebugString("AAAAAAAAAAAA")
                    textbutton ui_tr("debug_preset_g") style "pill_button" action SetDebugString("BBBBBBBBBBBB")
                    textbutton ui_tr("debug_preset_s1") style "pill_button" action SetDebugString("CCCCCCCCCCCC")
                    textbutton ui_tr("debug_preset_s2_acb") style "pill_button" action SetDebugString("BBBBBBBBACBB")
                    if not main_menu and validasi_string12(get_choice_string()):
                        textbutton ui_tr("debug_use_current") style "pill_button" action SetDebugString(get_choice_string())

        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (32, 26)

            vbox:
                xfill True
                spacing 16

                text ui_tr("debug_gates_grid_title") style "section_title"

                grid 4 3:
                    xfill True
                    spacing 16

                    for idx in range(12):
                        frame:
                            xfill True
                            background Solid("#1a130fe0")
                            padding (14, 12)

                            hbox:
                                xfill True
                                spacing 8
                                text ("G" + str(idx + 1)) size 24 bold True color gui.accent_color xminimum 58 yalign 0.5
                                for ch in ("A", "B", "C"):
                                    textbutton ch:
                                        xminimum 54
                                        yminimum 44
                                        padding (10, 6)
                                        background Solid("#2a1f18")
                                        hover_background Solid("#4a3424")
                                        selected_background Solid("#8a5c2e")
                                        text_size 22
                                        text_xalign 0.5
                                        action SetDebugGateChar(idx, ch)

        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (32, 26)

            vbox:
                xfill True
                spacing 18

                text ui_tr("debug_result_section") style "section_title"

                if _eval_res is None:
                    text ui_tr("debug_invalid_input") size 26 color "#e07a68"
                else:
                    frame:
                        xfill True
                        background Solid("#382619f2")
                        padding (26, 20)

                        vbox:
                            spacing 8
                            hbox:
                                spacing 16
                                text (_eval_res["id"] + " · " + ui_tr(_eval_res["tag_key"])) size 32 bold True color gui.accent_color
                                text ui_tr(_eval_res["title_key"]) size 32 bold True color gui.selected_color
                            text ui_tr(_eval_res["reason_key"]) size 23 color gui.text_color

                    grid 5 1:
                        xfill True
                        spacing 14

                        for i in range(5):
                            $ _is_winner = (i == _eval_res["index"])
                            $ _is_elig = _eval_res["eligible"][i]
                            frame:
                                xfill True
                                background Solid("#523821f5" if _is_winner else ("#211812e6" if _is_elig else "#17110db8"))
                                padding (16, 14)

                                vbox:
                                    spacing 6
                                    xalign 0.5
                                    text ENDING_INDEX_TO_ID[i] size 26 bold True color (gui.selected_color if _is_winner else gui.accent_color) xalign 0.5
                                    text ui_tr(ENDING_INDEX_TO_TAG_KEY[i]) size 20 color (gui.text_color if _is_elig else UI_TEXT_DIM) xalign 0.5
                                    text str(_eval_res["scores"][i]) size 34 bold True color (gui.selected_color if _is_winner else gui.text_color) xalign 0.5
                                    text (ui_tr("debug_eligible_yes") if _is_elig else ui_tr("debug_eligible_no")) size 18 color (gui.accent_color if _is_elig else "#c96e5d") xalign 0.5

                    hbox:
                        spacing 32
                        text ui_tr("debug_flag_acb", val=(ui_tr("confirm_yes") if _eval_res["pola_khusus_acb"] else ui_tr("confirm_no"))) size 22 color UI_TEXT_MUTED
                        text ui_tr("debug_flag_cc", val=(ui_tr("confirm_yes") if _eval_res["aturan_kritis_cc"] else ui_tr("confirm_no"))) size 22 color UI_TEXT_MUTED
                        text ui_tr("debug_flag_true", val=(ui_tr("confirm_yes") if _eval_res["pola_true"] else ui_tr("confirm_no"))) size 22 color UI_TEXT_MUTED

        frame:
            xfill True
            background Solid(UI_BG_CARD)
            padding (32, 24)

            vbox:
                xfill True
                spacing 12

                text ui_tr("debug_state_section") style "section_title"
                text ui_tr("debug_state_choices", code=get_choice_string()) size 23 color gui.text_color
                text ui_tr("debug_state_cond", k1=(cond_k1 or "—"), k2=(cond_k2 or "—")) size 23 color UI_TEXT_MUTED
                text ui_tr("debug_state_items", mini=(ui_tr("confirm_yes") if item_kaset_kosong_mini else ui_tr("confirm_no")), panci=(ui_tr("confirm_yes") if item_file_panci else ui_tr("confirm_no")), hujan=(item_file_hujan or "—")) size 23 color UI_TEXT_MUTED

                null height 6
                hbox:
                    spacing 14
                    textbutton ui_tr("debug_test_cassette_btn"):
                        style "pill_button"
                        action Show(
                            "cassette_player",
                            cassette_id="kaset_besok_busarah",
                            label_title=ui_tr("cassette_test_title"),
                            transcript_lines=[(None, ui_tr("cassette_test_transcript_1")), (None, ui_tr("cassette_test_transcript_2"))],
                            duration_sec=10,
                            allow_skip=True,
                            is_overlay_preview=True,
                        )
