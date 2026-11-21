## Interlude / Side B — Titik Masuk Utama Permainan (Lengkap: Bab 1–48 & 5 Ending Kanonik)
## Alur cerita Bab 1–48 berada di `game/story/bab_01_04.rpy` s.d. `bab_45_48.rpy`.

label start:
    ## Common Route (Bab 1–25: G1–G8, m01–m15)
    call bab_01
    call bab_02
    call bab_03
    call bab_04
    call bab_05
    call bab_06
    call bab_07
    call bab_08
    call bab_09
    call bab_10
    call bab_11
    call bab_12
    call bab_13
    call bab_14
    call bab_15
    call bab_16
    call bab_17
    call bab_18
    call bab_19
    call bab_20
    call bab_21
    call bab_22
    call bab_23
    call bab_24
    call bab_25

    ## Percabangan Tiga Rute G9–G11 (Bab 26–39: Rute Merah / Tunda / Sehat)
    call arc_bab_26_39

    ## Klimaks, Evaluasi 12 Gerbang, 5 Ending Kanonik, & Epilog (Bab 40–48)
    call arc_bab_40_48

    ## Kembali ke Menu Utama dengan progres persisten (ending, pencapaian, CG) tersimpan utuh.
    return


## Orkestrasi tiga rute Bab 26–39 (G9, K1, G10, G11, m16–m20).
label arc_bab_26_39:
    call bab_26

    if get_major_choice(9) == "A":
        ## [RUTE MERAH] — Barter kaset merah (K1), Bab 27–31 Merah
        call bab_27_merah
        call bab_28_merah
        call bab_29_merah
        call bab_30_merah
        call bab_31_merah
    elif get_major_choice(9) == "B":
        ## [RUTE TUNDA] — Jumat Berikutnya (T-1..T-3), lalu menyatu ke Bab 27–31 Sehat
        call bab_26_tunda
        call bab_27_sehat
        call bab_29_sehat
        call bab_30_sehat
        call bab_31_sehat
    else:
        ## [RUTE SEHAT] — Tolak kaset merah, Bab 27–31 Sehat (tanpa Bab 28)
        call bab_27_sehat
        call bab_29_sehat
        call bab_30_sehat
        call bab_31_sehat

    ## Bab 32 (m18 di kedua rute; 32-2..4 Merah vs 32S-1 G10-SEHAT)
    call bab_32

    if get_major_choice(9) == "A":
        call bab_33
        call bab_34_merah
    else:
        call bab_34_sehat

    ## Bab 35 — Semua rute menyatu (callback m18, m19, Pak Ageng sakit)
    call bab_35

    ## Bab 36–37 — Dua versi Bab 36; Bab 37 hanya pada Rute Merah + G10=A
    if get_major_choice(9) == "A":
        call bab_36_merah
        if get_major_choice(10) == "A":
            call bab_37
    else:
        call bab_36_sehat

    ## Bab 38–39 — Semua rute menyatu (G11, m20)
    call bab_38
    call bab_39
    return


## Orkestrasi klimaks Bab 40–48 (m20 callback, m21, G12, Bab 41 bila G12!=C, evaluasi 12 gerbang -> 5 ending).
label arc_bab_40_48:
    call bab_40
    call bab_42_g12_dan_evaluasi
    return
