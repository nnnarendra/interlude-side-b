## Interlude / Side B — Batch 11 (Epilog Bab 45–48)
## Sumber verbatim: NASKAH-VN-MASTER-Interlude-Side-B.md (baris 3760–3990)
## Gerbang: K2 (Bab 45 — hanya Happy-True: A -> ach_kaset_terakhir + Bab 48 penuh; B -> bonus Galeri Bab 48),
##          m23 (Bab 47 — Happy-True & Happy-Sehat)
## CG & Kaset: cg_tombol_play (Bab 45-3), kaset_pesan_ageng (Bab 48-3 via pemutar kaset Fase 2)

################################################################################
## BAB 45 — Pita yang Tak Terputar [HAPPY-TRUE] ◆ K2
################################################################################

label bab_45:
    $ chapter_autosave("bab_45", "Bab 45 — Pita yang Tak Terputar", "Ch. 45 — The Unplayed Tape")

    ## Adegan 45-1 — Keluar dari stasiun, malam setelah hujan
    scene bg_stasiun with dissolve
    play music bgm_epilog loop if_changed
    show kai senyum at pos_center with dissolve

    "Kai berjalan keluar dari aula stasiun. Langkahnya ringan — jauh lebih ringan dari semua langkah yang pernah dia ambil tahun ini. Badai sore tadi sudah surut. Aspal masih basah, lampu-lampu jalan menyala satu-satu, dan dadanya… lapang. Rasa hampa yang berbulan-bulan mengganjal itu sudah mencair." id b45_001

    kai_hati "Yara nggak pergi ninggalin aku. Dia cuma pindah kota. \"Selamat tinggal\" itu… jeda. Cuma jeda. Kenapa hal sesederhana itu butuh waktu setahun buat kupahami, ya?" id b45_002

    "Kakinya berjalan sendiri. Tanpa disuruh, tanpa dipikir — trotoar itu membawanya belok ke arah yang sudah sangat dia kenal. Gang buntu. Toko Gema Masa." id b45_003

    ## Adegan 45-2 — Toko Gema Masa, kaset terakhir
    play sound sfx_lonceng_pintu
    scene bg_toko_dalam_malam with dissolve
    play music bgm_duka_siti loop fadein 1.5
    show kai biasa at pos_left with dissolve
    show ageng sakit at pos_right with dissolve

    "Lonceng di atas pintu berdenting pelan. Di dalam sunyi — tapi bukan sunyi yang mencekam seperti dulu. Pak Ageng duduk di kursi goyangnya di balik konter jati. Badannya jauh lebih kurus dari beberapa minggu lalu. Garis-garis di wajahnya lebih dalam. Matanya sedikit berkabut, seperti sedang menatap sesuatu yang jauh melampaui ruangan ini." id b45_004

    kai_hati "Pak Ageng kelihatan… capek banget. Kapan terakhir aku lihat beliau sekurus ini?" id b45_005

    ageng "{i}(menoleh lambat, tersenyum — senyum paling tulus yang pernah Kai lihat){/i} Kamu kembali, Nak. Dan kamu membawa pulang jiwamu." id b45_006

    kai "{i}(mendekati konter, mengangguk pelan){/i} Bapak benar, Pak. Selamat tinggal itu cuma jeda. Saya nggak perlu takut lagi sama apa yang ada di depan." id b45_007

    $ show_item("item_kaset_kosong_akhir")
    ageng "{i}(terkekeh pelan, lalu batuk kecil yang ditahan){/i} Bagus. Bagus… {i}(merogoh laci di bawah konter dengan gerakan sangat lambat, mengeluarkan kaset Type IV Metal yang masih terbungkus plastik segel){/i} Ini untukmu, Kai. Kaset terakhir dari toko ini. Gratis." id b45_008

    "Kaset itu diletakkan di atas konter. Tidak ada label merah. Tidak ada tanggal tulisan tangan. Label kertas putihnya benar-benar kosong." id b45_009

    kai "{i}(menatap kaset itu){/i} Kaset apa ini, Pak? Kok labelnya kosong?" id b45_010

    ageng "Ini kaset masa depanmu yang sesungguhnya. Isinya apa saja yang ingin kamu dengar setelah hari ini. {i}(menatap Kai dengan kehangatan seorang guru yang melepas muridnya){/i} Putarlah, kalau kamu ingin tahu jalan mana yang harus kamu ambil." id b45_011

    "Kai menatap kaset kosong itu lama. Kilau mikanya memantulkan lampu gantung. Di sudut kepalanya, godaan lama sempat berbisik lemah — membayangkan apa saja yang bisa dia dengar dari sisa hidupnya bersama Yara. Tapi cuma sebentar." id b45_012

    show kai senyum at pos_left
    kai "{i}(tersenyum tipis, menggeleng pelan; mengambil kaset itu dan memasukkannya ke saku jaket — tanpa merobek segelnya){/i} Makasih, Pak. Tapi saya nggak akan memutarnya. Saya mau pitanya tetap kosong… sampai saya sendiri yang ngisinya. Pakai suara-suara yang nyata." id b45_013

    ageng "{i}(terpaku sejenak — lalu tertawa hangat, tawa paling lega yang pernah keluar dari pria tua itu){/i} Pilihan yang sangat bijak, Kai. Kamu akhirnya benar-benar bebas." id b45_014

    ## Adegan 45-3 — Kamar Kai, malam itu ◆ K2 (CG Kanonik #6: cg_tombol_play)
    scene bg_kamar_kai_malam with dissolve
    show kai biasa at pos_center with dissolve

    "Malam itu di kamarnya, Kai membuka laci meja belajar. Di dalamnya: jalinan pita-pita kusut dari kaset-kaset lama — yang sekarang sudah tidak punya kekuatan apa-apa atas dirinya. Dia menyingkirkannya, lalu memegang kaset terakhir dari Pak Ageng." id b45_015

    $ show_cg_and_unlock("cg_tombol_play", dissolve)

    ## GERBANG KONDISIONAL K2 (hanya Happy-True; A -> ach_kaset_terakhir + Bab 48; B -> bonus Galeri Bab 48)
    menu:
        "Kaset berlabel kosong itu ada di tangan Kai."

        "\"Putar sekarang.\"":
            $ record_cond_k2("A")
            kai_hati "Tanganku bergerak ke Walkman… lalu berhenti. {i}(tersenyum kecil sendirian){/i} Nggak. Bukan karena takut. Justru karena sudah nggak takut. Kaset ini bakal kuputar — nanti, pas aku sudah benar-benar punya sesuatu buat didengar. Dan hari itu pasti datang." id b45_016a
            "Kai meletakkan kaset itu di sudut laci dengan label kosongnya menghadap ke atas. Seperti janji yang sengaja dibiarkan terlihat." id b45_017a

        "\"Simpan. Belum.\"":
            $ record_cond_k2("B")
            kai_hati "Belum. Pitanya biar kosong dulu. Hidupku saja yang jalan — kasetnya belakangan." id b45_016b
            "Kai meletakkan kaset terakhir dari Pak Ageng itu di sudut paling dalam laci, lalu menutup lacinya rapat-rapat. Beberapa hal memang untuk nanti." id b45_017b

    return


################################################################################
## BAB 46 — Gema yang Menjadi Milik Sendiri [HAPPY-TRUE & VARIAN HAPPY-SEHAT]
################################################################################

label bab_46_true:
    $ chapter_autosave("bab_46_true", "Bab 46 — Gema yang Menjadi Milik Sendiri", "Ch. 46 — An Echo of One's Own")

    ## Adegan 46-1 — Gang buntu, beberapa bulan kemudian, senja kemarau
    scene bg_gang_kering with fade
    play music bgm_epilog loop if_changed
    show kai dewasa at pos_center with dissolve

    "Beberapa bulan kemudian. Angin musim kemarau menyapu Malang, kering tapi masih menyisakan dingin di sore hari. Kai berjalan dengan ransel kuliah di satu bahu — jaket abu-abu tebalnya sudah diganti kemeja flanel santai." id b46t_001
    "Langkahnya mantap. Kuliah arsitekturnya memang menyita waktu — maket, tugas gambar, begadang — tapi di sela-selanya, dia selalu bisa bernapas." id b46t_001_p2

    kai_hati "Dan entah kenapa… kaki ini belok lagi ke sini. Kebiasaan lama susah hilang, ya." id b46t_002

    scene bg_toko_kosong with dissolve
    show kai dewasa at pos_center with dissolve
    "Gang itu sekarang bersih, dinding batanya keemasan kena matahari senja. Tapi di ujung gang, langkah Kai melambat. Pintu kayu Toko Gema Masa tidak lagi digembok rantai berkarat. Papan kecil \"Buka/Tutup\" sudah lenyap. Di kaca jendela yang kini bersih mengilap, tertempel kertas putih besar bertuliskan tegas:" id b46t_003

    "DISEWAKAN." id b46t_004

    "Kai naik ke teras dan mengintip ke dalam. Kosong melompong. Tidak ada lemari kaca berisi ratusan takdir. Tidak ada konter jati tempat Pak Ageng menyeduh kopi dan menyajikan cenil. Kursi goyang tua itu pun sudah tidak ada. Hanya lantai kayu bersih dan bayangan senja yang memanjang." id b46t_005

    kai_hati "Pak Ageng sudah pergi. Tokonya juga. Toko yang lahir dari duka itu… sudah selesai tugasnya. {i}(mengusap kaca jendela perlahan){/i} Makasih, Pak. Nggak sempat bilang langsung. Jadi lewat sini saja." id b46t_006

    ## Adegan 46-2 — Panggilan video dari Yogyakarta
    scene bg_teras_toko with dissolve
    play sound sfx_notifikasi_hp
    show kai dewasa at pos_left with dissolve
    show yara dewasa at pos_right with dissolve

    "Ponsel di saku celananya bergetar. Panggilan video masuk — kontaknya bernama Yara. Kai memasang earphone dan menekan tombol terima. Wajah Yara yang cerah memenuhi layar; dia sedang duduk di kafe kecil di Yogyakarta, headphone hitam besarnya melingkar di leher seperti biasa." id b46t_007

    yara "Hai, Kai!" id b46t_008

    kai "Hai, Yara. Baru selesai kelas?" id b46t_009

    yara "Iya, baru saja. Hari ini aku belajar menyaring frekuensi suara rendah di studio. {i}(mendekatkan ponsel ke jendela kafe){/i} Eh, dengar ini, Kai." id b46t_010

    yara "Indah, kan?" id b46t_011

    kai "{i}(tersenyum, menatap bayangan dirinya di kaca toko kosong, bersanding wajah Yara di layar){/i} Sangat indah." id b46t_012

    kai_hati "Ratusan kilometer. Tapi suaranya dekat sekali. Jarak ternyata bukan pembatas. Cuma… jembatan yang bunyinya beda. — Aku mungkin nggak akan pernah ingat lagi gimana kami pertama bertemu di perpustakaan." id b46t_013
    kai_hati "Lubang itu tetap ada. Bekas luka dari masa laluku yang gila. Tapi nggak apa-apa. Kami lagi nulis cerita baru. Hari ini, besok, dan hari-hari sesudahnya. Tanpa ramalan." id b46t_013_p2

    kai "Aku merindukanmu, Yara." id b46t_014

    yara "Aku juga, Kai. Sampai ketemu akhir bulan nanti di stasiun, ya?" id b46t_015

    kai "{i}(mengangguk mantap){/i} Ya. Di stasiun." id b46t_016

    hide yara with dissolve
    "Kai berbalik dan berjalan keluar dari gang itu menuju jalan raya yang ramai. Di saku jaketnya, kaset kosong pemberian Pak Ageng tetap tersimpan aman — bukti bisu bahwa masa depannya sekarang miliknya sendiri, untuk ditulis dan didengarkan dengan penuh kejutan." id b46t_017

    return


label bab_46_sehat:
    $ chapter_autosave("bab_46_sehat", "Bab 46 — Gema yang Menjadi Milik Sendiri", "Ch. 46 — An Echo of One's Own")

    ## Adegan 46S-1 — Di depan toko yang kosong [HAPPY-SEHAT]
    scene bg_toko_kosong with fade
    play music bgm_epilog loop fadein 1.5
    show kai dewasa at pos_center with dissolve

    "Beberapa bulan kemudian, kaki Kai membawanya lagi ke gang itu. Toko Gema Masa sudah kosong — kertas \"DISEWAKAN\" tertempel di kacanya yang bersih. Pak Ageng sudah pergi, dan toko itu sudah selesai dengan tugasnya. Kai tersenyum tipis ke arah jendela kosong itu, lalu merogoh saku jaketnya." id b46s_001

    kai_hati "Bukan kaset kosong. Dan bukan ramalan. Kaset ini isinya kami sendiri yang merekam — suara panci di kantin, rel kereta, hujan di teras toko… dan ketawa kami yang jelek-jelek itu. Pita ini penuh. Penuhnya karena diisi, bukan karena diberi." id b46s_002

    show kai dewasa at pos_left with dissolve
    show yara dewasa at pos_right with dissolve
    "Ponselnya bergetar. Panggilan video dari Yara, dari kafe kecilnya di Yogyakarta." id b46s_003

    yara "Hai, Kai! Kamu di mana? Kok latarnya kayak… {i}(menyipitkan mata){/i} Itu gang toko Pak Ageng, ya?" id b46s_004

    kai "Iya. Toko kosongnya lagi kutengok. {i}(mengangkat kaset rekamannya ke kamera){/i} Nih. Aku bawa terus. Kemarin kuputar di kos — bagian kamu ketawa pas kehujanan itu masih paling kencang sendiri suaranya." id b46s_005

    yara "{i}(tertawa){/i} Itu bukan ketawa, itu aku kedinginan! Eh, tunggu — akhir bulan aku pulang ke Malang. Kita rekam sisi B-nya, ya? Stasiun. Harus stasiun." id b46s_006

    kai "Deal. Sisi B di stasiun." id b46s_007

    kai_hati "Lubang di ingatanku nggak ada — karena memang nggak pernah ada yang kutukar. Yang ada cuma pita yang makin lama makin penuh. Dan isinya… kami yang nulis sendiri." id b46s_008

    hide yara with dissolve
    "Kai melangkah keluar dari gang menuju jalan raya yang ramai, kaset rekaman itu aman di sakunya — bukan untuk diintip isinya besok, tapi untuk didengar ulang kapan pun dia mau ingat hari ini." id b46s_009

    return


################################################################################
## BAB 47 — Aroma Baru di Sudut yang Sama [HAPPY-TRUE & HAPPY-SEHAT] ◆ m23
################################################################################

label bab_47:
    $ chapter_autosave("bab_47", "Bab 47 — Aroma Baru di Sudut yang Sama", "Ch. 47 — A New Aroma in the Same Corner")

    ## Adegan 47-1 — Dua tahun kemudian, kedai kopi di bekas Toko Gema Masa
    play sound sfx_lonceng_pintu
    scene bg_kafe with fade
    play music bgm_kafe_baru loop fadein 1.5
    show kai dewasa at pos_center with dissolve

    "Dua tahun berlalu. Gang buntu itu tidak lagi senyap: udara dingin pasca-hujan, riuh rendah yang hangat, dan di ujungnya — Toko Gema Masa sudah bersalin rupa. Pintu kayu kokoh diganti pintu kaca berbingkai besi hitam." id b47_001
    "Di dalamnya, bar kopi panjang dengan mesin espresso mengilap berdiri di tempat lemari-lemari kaset dulu berjejer. Kursi goyang Pak Ageng sudah digantikan kursi-kursi kayu berbusa dan meja panjang yang penuh laptop, kertas kalkir, dan cangkir keramik." id b47_001_p2

    show kai dewasa at pos_left with ease
    show npc_teman1_dewasa at pos_right with dissolve
    teman1 "Kai! Sini, rek — tarik kursinya ke sini, maket tapaknya hampir selesai!" id b47_002

    "Di meja sudut — tepat di titik lemari kaset merah dulu berada — dua teman kuliah arsitektur Kai sudah tenggelam di antara kertas kalkir, potongan karton, dan laptop yang menampilkan model 3D." id b47_003

    kai "{i}(meletakkan ransel beratnya, duduk){/i} Sori agak telat. Tadi harus asistensi struktur dulu. {i}(menyambar iced americano yang sudah dipesankan untuknya, meminumnya){/i} Nah. Hidup lagi." id b47_004

    show npc_teman2_dewasa at pos_center with dissolve
    teman2 "{i}(tanpa mengalihkan pandangan dari layar){/i} Santai. Ini tinggal merapikan kontur tanah di bagian belakang bangunan. Tapi serius, Kai, rekomendasi tempatmu ini juara. Tenang, kopinya enak tenan, dan entah kenapa… suasananya bikin fokus." id b47_005

    kai "{i}(tersenyum tipis, mengedarkan pandangan ke sekeliling ruangan){/i} Iya. Tempat ini memang… segitu-nya." id b47_006

    kai_hati "Buat mereka, ini cuma kedai kopi enak buat nugas. Buat aku… di balik dinding ekspos ini, kadang aku masih kayak dengar putaran kaset pelan-pelan. Gesekan pita. Tawa Pak Ageng pas menyajikan cenil. Gemanya sudah mati — diganti gema yang hidup. Dan itu nggak apa-apa. Malah bagus." id b47_007

    ## Adegan 47-2 — Kilas balik: pertama kali Kai masuk ke kedai ini ◆ m23
    hide npc_teman1_dewasa with dissolve
    hide npc_teman2_dewasa with dissolve
    "Kai ingat pertama kali dia mendorong pintu kaca ini, tidak lama setelah kedai ini buka. Waktu itu dia berdiri lama di depan bar, membaca papan menu — di tempat yang persis sama dengan konter jati dulu." id b47_008

    ## GERBANG MINOR m23 (pesanan pertama Kai di kedai kopi bekas toko)
    menu:
        "Pesanan pertama Kai di kedai kopi bekas toko itu:"

        "Kopi hitam.":
            $ record_minor_choice("m23", "A")
            show npc_barista at pos_right with dissolve
            barista "Kopi hitam satu. Diminum di sini?" id b47_009a
            kai "Di sini. {i}(duduk menghadap bar){/i} Di sini… lama." id b47_010a

        "Teh.":
            $ record_minor_choice("m23", "B")
            show npc_barista at pos_right with dissolve
            barista "Teh panas satu. Diminum di sini?" id b47_009b
            kai "Di sini. {i}(tersenyum kecil sendiri — teh melati di toko ini dulu selalu gratis, sekarang dia membayar, dan rasanya tetap sama-sama hangat){/i}" id b47_010b

        "Tidak pesan, hanya duduk.":
            $ record_minor_choice("m23", "C")
            show npc_barista at pos_right with dissolve
            kai "Nggak pesan dulu, Mas. Duduk saja sebentar, boleh?" id b47_009c
            barista "Boleh, santai saja." id b47_010c
            kai_hati "Waktu itu aku cuma butuh duduk. Memastikan tempat ini sudah jadi tempat lain — dan aku baik-baik saja dengan itu." id b47_011c

    ## Adegan 47-3 — Pesan suara dari Yara
    "Saat teman-temannya kembali tenggelam dalam diskusi kolom dan atap, ponsel Kai bergetar. Pesan dari Yara — dengan lampiran rekaman suara sepuluh detik." id b47_012

    yara_pesan "\"Kai, dengar ini! Aku baru saja merekam suara rintik hujan yang jatuh di atas atap seng stasiun Tugu sore ini. Nadanya persis seperti gema di Stasiun Malang Kota Lama dua tahun lalu. Aku merindukanmu.\"" id b47_013

    play sound sfx_hujan_deras loop fadein 0.8
    "Kai memasang satu earphone dan menekan play. Rintik hujan Yogyakarta memenuhi telinganya, menyatu dengan bunyi mesin espresso dan obrolan teman-temannya. Dia memejamkan mata sebentar." id b47_014

    kai_hati "Dulu, di tempat ini persis, aku gemetar mikirin besok. Sekarang aku duduk di sini merayakan hari ini. Belajar. Ketawa sama teman. Dan mencintai Yara — dengan melodi yang kami susun sendiri, tiap hari. Nggak pakai kaset ramalan lagi." id b47_015

    stop sound fadeout 0.8

    ## Baris penutup adegan mengikuti pilihan m23
    if get_minor_choice("m23") == "A":
        "Kopi hitam pertamanya di tempat ini sudah lama habis. Yang tersisa cuma rasanya — pahit, jujur, dan nggak perlu diramal." id b47_016a
    elif get_minor_choice("m23") == "B":
        "Teh pesanannya sore itu sudah dingin. Nggak apa-apa. Di tempat ini, teh yang dingin pun pernah jadi awal dari semuanya." id b47_016b
    else:
        "Kadang yang dibutuhkan memang cuma duduk. Di kursi yang sama, di sudut yang sama — sebagai orang yang sudah berbeda." id b47_016c

    return


################################################################################
## BAB 48 — Frekuensi yang Tak Pernah Hilang [HANYA BILA K2=A / BONUS GALERI]
################################################################################

label bab_48:
    $ chapter_autosave("bab_48", "Bab 48 — Frekuensi yang Tak Pernah Hilang", "Ch. 48 — Frequency Never Lost")

    ## Adegan 48-1 — Empat tahun kemudian, kamar Kai, siang
    scene bg_kamar_kai with fade
    play music bgm_epilog loop fadein 1.5
    show kai dewasa at pos_center with dissolve

    "Empat tahun. Ribuan malam begadang, kertas kalkir lecek, dan revisi maket yang tidak berkesudahan — semuanya sudah terlipat jadi selembar ijazah arsitektur. Skripsi Kai sudah dipertahankan minggu lalu." id b48_001
    "Siang ini kamarnya berantakan dengan cara yang melegakan: kardus-kardus berisi buku struktur, penggaris segitiga, dan draf-draf lama. Masa kuliah selesai. Babak baru, sebagai arsitek muda, sebentar lagi mulai." id b48_001_p2

    "Saat mengosongkan laci terdalam meja belajarnya — laci yang bertahun-tahun tidak disentuh — jemari Kai membentur sesuatu yang keras di sudut paling belakang. Cangkang mika bening." id b48_002

    $ show_item("item_kaset_kosong_akhir")
    kai_hati "Ini… {i}(menariknya keluar, meniup debu tipis di permukaannya){/i} Kaset terakhir dari Pak Ageng. Segelnya masih utuh. Labelnya masih kosong. Empat tahun, dan aku nggak pernah berani— nggak, bukan nggak berani." id b48_003
    kai_hati "Nggak pernah butuh. {i}(jeda; menatap Walkman perak tua di rak buku){/i} Dulu aku takut setengah mati sama kaset ini. Sekarang yang tersisa cuma… kangen sama orangnya." id b48_003_p2

    kai "{i}(duduk di tepi tempat tidur, merobek plastik segelnya perlahan){/i} Pak… saya putar sekarang, ya." id b48_004

    ## Adegan 48-2 — Isi kaset Side A: Potensi Kebahagiaan (kaset_ultah_kai_yara.ogg)
    stop music fadeout 0.8
    $ hide_item()
    "Desis halus mengalir. Lalu hening, tiga detik. Kai menahan napas. Dan suara yang keluar membuat matanya membelalak." id b48_005

    call play_cassette(
        cassette_id="kaset_ultah_kai_yara",
        label_title=_("Kaset Penutup — Side A: Potensi Kebahagiaan"),
        transcript_lines=[
            (_("Yara (dari kaset)"), _("—eh, taruh lilinnya di tengah! Kai, potong kuenya cepat, aku sudah lapar!")),
            (_("Kai 22 th (dari kaset)"), _("Sabar, Yar, ini koreknya macet. Nah, ayo tiup bareng-bareng! Satu… dua… tiga!")),
        ],
        duration_sec=18,
        allow_skip=True,
    )

    "Itu suara Yara — renyah, dewasa, tertawa lepas tanpa beban. Dan suara kedua adalah suara Kai sendiri: suara pemuda dua puluh dua tahun yang sangat bahagia, di tengah perayaan ulang tahun sederhananya di kontrakan, beberapa bulan lalu. Kai terduduk. Air matanya mengalir tanpa dia sadari." id b48_008

    kai_hati "Gimana mungkin… Kaset ini disegel empat tahun lalu. Ulang tahunku baru beberapa bulan kemarin. Gimana dia bisa merekamnya? {i}(jeda panjang; lalu pemahaman itu datang pelan-pelan){/i} …Oh. Oh, Pak. Kaset ini nggak pernah merekam takdir. Nggak ada toko itu yang merekam takdir." id b48_009
    kai_hati "Yang direkamnya… potensi kebahagiaan. Getaran dari keputusan-keputusan baik yang kuambil sejak hari di stasiun itu. Setiap kali aku milih percaya sama hari ini ketimbang takut sama besok — kaset ini menyelaraskan dirinya. Merekam gema kebahagiaan yang memang seharusnya kumiliki." id b48_009_p2

    ## Adegan 48-3 — Pesan terakhir Pak Ageng (komponen pemutar kaset Fase 2 + transkrip penuh)
    stop music fadeout 1.0
    $ hide_item()
    call play_cassette(
        cassette_id="kaset_pesan_ageng",
        label_title=_("Kaset Terakhir — Pesan Pak Ageng"),
        transcript_lines=[
            (_("Pak Ageng (dari kaset)"), _("Kai… Jika kamu akhirnya memutuskan untuk memutar kaset ini, itu artinya kamu sudah berhasil melewati ketakutanmu. Kamu sudah tidak lagi menjadi budak dari ramalan mati.")),
            (None, _("Suara itu sangat lemah. Tapi kelegaannya luar biasa. Ada batuk kecil, lalu suara itu melanjutkan, sangat lembut.")),
            (_("Pak Ageng (dari kaset)"), _("Saat kamu mendengar suara ini, toko kaset kita mungkin sudah tidak ada. Dan aku… aku mungkin sudah kembali berkumpul bersama Sitiku. Mendengar tawa indahnya yang nyata — tanpa perlu bantuan pita magnetik lagi. Jangan sedih, Nak. Ini bukan perpisahan yang buruk. Ini akhir dari sebuah lagu lama… dan awal dari simfoni barumu.")),
            (None, _("[Derit kursi goyang jati — terakhir kalinya.]")),
            (_("Pak Ageng (dari kaset)"), _("Terima kasih sudah pernah meramaikan toko duka itu dengan langkah kakimu, Kai. Jaga dirimu baik-baik. Selamat tinggal selamanya.")),
        ],
        duration_sec=45,
        allow_skip=True,
    )

    ## Adegan 48-4 — Penutup
    play sound sfx_klik_play
    play music bgm_epilog loop fadein 1.5
    scene bg_kamar_kai with dissolve
    show kai dewasa at pos_center with dissolve

    "Kai melepaskan earphone-nya perlahan. Dia menatap kaset di genggamannya sambil tersenyum di sela tangisnya. Hangat menjalar di seluruh dadanya. Perpisahan dengan Pak Ageng memang selamanya — tapi gema kebijaksanaan pria tua itu akan tetap tersimpan rapat di dalam dirinya." id b48_010

    kai_hati "Selamat tinggal juga, Pak. Dan… makasih. Untuk semuanya." id b48_011

    "Kai melangkah ke jendela, membuka gorden, dan membiarkan cahaya matahari sore Malang menerpa wajahnya. Di luar sana, dunia yang bising dan indah sedang menunggu — dan kali ini, dia siap menjalani setiap detiknya. Dengan melodinya sendiri." id b48_012

    stop music fadeout 1.5
    return


## Titik putar Adegan Bonus Bab 48 dari Galeri CG (hanya terbuka bila K2=B di Happy-True — PRD §4.7).
label bab_48_bonus:
    call bab_48
    return


################################################################################
## EPILOG KHUSUS H2 (HAPPY-SEHAT) — Side A Saja: Gema Bahagia (kaset_ultah_kai_yara)
################################################################################

label epilog_h2_kaset_ultah:
    scene bg_kamar_kai with fade
    play music bgm_epilog loop fadein 1.5
    show kai dewasa at pos_center with dissolve

    "Malamnya di kamar, Kai merapikan meja belajarnya dan menemukan satu kaset rekaman kecil yang dulu dia rekam sendiri bareng Yara — bukan kaset ramalan, bukan barang barter. Cuma pita biasa berisi suara yang sengaja dia simpan karena hari itu terlalu indah untuk dilewatkan." id ep_h2_001

    kai "{i}(tersenyum tipis, memasukkan kaset itu ke Walkman perak tua di mejanya){/i} Coba putar sebentar, ah." id ep_h2_002

    stop music fadeout 0.8
    call play_cassette(
        cassette_id="kaset_ultah_kai_yara",
        label_title=_("Side A — Gema Bahagia (Kai & Yara)"),
        transcript_lines=[
            (_("Yara (dari kaset)"), _("—eh, taruh lilinnya di tengah! Kai, potong kuenya cepat, aku sudah lapar!")),
            (_("Kai 22 th (dari kaset)"), _("Sabar, Yar, ini koreknya macet. Nah, ayo tiup bareng-bareng! Satu… dua… tiga!")),
        ],
        duration_sec=18,
        allow_skip=True,
    )

    play sound sfx_klik_play
    play music bgm_epilog loop fadein 1.5
    scene bg_kamar_kai with dissolve
    show kai dewasa at pos_center with dissolve

    "Suara tawa itu memenuhi kamar yang hangat. Tidak ada ramalan masa depan di pita ini — hanya suara nyata yang mereka buat sendiri. Kai melepas earphone-nya, tersenyum tenang, dan melangkah menuju hari esok tanpa perlu takut lagi." id ep_h2_003

    stop music fadeout 1.5
    return
