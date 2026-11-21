label start:

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

    call arc_bab_26_39

    call arc_bab_40_48

    return

label arc_bab_26_39:
    call bab_26

    if get_major_choice(9) == "A":

        call bab_27_merah
        call bab_28_merah
        call bab_29_merah
        call bab_30_merah
        call bab_31_merah
    elif get_major_choice(9) == "B":

        call bab_26_tunda
        call bab_27_sehat
        call bab_29_sehat
        call bab_30_sehat
        call bab_31_sehat
    else:

        call bab_27_sehat
        call bab_29_sehat
        call bab_30_sehat
        call bab_31_sehat

    call bab_32

    if get_major_choice(9) == "A":
        call bab_33
        call bab_34_merah
    else:
        call bab_34_sehat

    call bab_35

    if get_major_choice(9) == "A":
        call bab_36_merah
        if get_major_choice(10) == "A":
            call bab_37
    else:
        call bab_36_sehat

    call bab_38
    call bab_39
    return

label arc_bab_40_48:
    call bab_40
    call bab_42_g12_dan_evaluasi
    return
