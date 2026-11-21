## Interlude / Side B — Batch 10 (Bab 40–44 + 5 Varian Penutup Ending)
## Sumber verbatim: NASKAH-VN-MASTER-Interlude-Side-B.md (baris 3344–3727)
## Gerbang: callback m20 (Bab 40), m21 (Bab 40 — opsi kaset mini hanya bila item_kaset_kosong_mini),
##          G12 (Bab 42 — posisi 12), TITIK EVALUASI 12 GERBANG (`evaluate_current_ending`),
##          m22 (Bab 43 Happy-True -> callback Bab 44)
## CG & Kaset: cg_peron (Bab 44-1), cg_jendela_kereta & cg_tombol_play (Gantung),
##             kaset_hening_60detik (Sad-Ironis)

################################################################################
## BAB 40 — Bingkisan di Batas Waktu ◆ m21
################################################################################

label bab_40:
    $ chapter_autosave("bab_40", "Bab 40 — Bingkisan di Batas Waktu", "Ch. 40 — A Parcel at the Edge of Time")

    ## Adegan 40-1 — Keset anyaman, pagi 1 Agustus
    scene bg_kamar_kai with dissolve
    play music bgm_senja loop fadein 1.5
    show kai biasa at pos_center with dissolve

    "Satu Agustus. Akhirnya datang juga, nggak bisa ditawar. Langit Malang pagi ini aneh — nggak mendung, nggak terik. Dingin, tenang. Kayak satu kota lagi nahan napas nunggu sore." id b40_001

    kai_hati "Hari ini. Hari ini kereta itu berangkat. Hari ini kalimat di kaset merah itu… kejadian." id b40_002

    "Kai membuka pintu depan cuma buat cari udara. Tapi matanya langsung berhenti di keset anyaman. Ada paket kecil dibungkus kertas cokelat. Nggak ada nama pengirim. Cuma tulisan pena hitam yang dia kenal betul: \"Untuk Kai\"." id b40_003

    show kai cemas at pos_center
    kai_hati "Tulisan tangan Yara. {i}(menelan ludah){/i} …Sejak kapan ini di sini?" id b40_004

    ## Adegan 40-2 — Kaset dari Yara (callback m20)
    scene bg_kamar_kai with dissolve
    show kai cemas at pos_center with dissolve

    "Di kamar, Kai merobek bungkusnya pelan-pelan, kayak takut isinya ikut sobek. Di dalam: satu kaset mika bening. Bukan kaset merah. Kaset biasa Type II Chrome — kaset yang biasa Yara pakai buat rekaman hari-harinya. Di dalamnya terselip kertas kecil: \"Putar aku.\"" id b40_005

    kai "{i}(mengambil Walkman peraknya yang berdebu){/i} …Oke. Oke, Yar." id b40_006

    play sound sfx_klik_play
    queue sound sfx_desis_pita
    "Tawa. Kompilasi tawa mereka berdua. Tawa Yara waktu mereka hampir kepleset lumpur di pinggir sawah dekat Bukit Banyak. Tawa Kai sendiri — lepas, asing, kayak suara orang lain — waktu mereka berhasil merekam lengking klakson kereta tua. Desau angin malam. Gemercik hujan di teras toko Pak Ageng. Gesekan ranting." id b40_007

    ## CALLBACK m20 — satu suara terdengar menonjol di tengah mix sesuai pilihan Bab 39
    if get_minor_choice("m20") == "A":
        play sound sfx_panci
        "Di sela tawa itu, bunyi panci mendidih di kantin naik paling depan, jernih sekali — suara pertama yang pernah Kai rekam buat Yara." id b40_008a
        stop sound fadeout 0.6
    elif get_minor_choice("m20") == "B":
        play sound sfx_hujan_deras
        "Di sela tawa itu, bunyi hujan menghantam talang naik paling depan, rata dan sabar — rekaman pilihan Kai di teras toko." id b40_008b
        stop sound fadeout 0.6
    else:
        play sound sfx_desis_pita
        "Di sela tawa itu, desis pita kosong naik paling depan selama dua detik — suara \"hening\" yang dulu paling Kai takuti, sekarang cuma jadi jeda di antara tawa." id b40_008c

    show kai menangis at pos_center
    kai_hati "Itu… itu kami. Itu beneran kami. Kedengarannya… hidup banget. Deket banget. {i}(air matanya jatuh){/i} Padahal ingatanku soal perpustakaan itu masih bolong. Masih kosong. Tapi ini — dada aku inget. Dada aku inget semua." id b40_009

    "Pita terus berputar. Bising kota di rekaman meredup. Bersih. Lalu suara Yara masuk — bukan Yara yang dingin di sekolah belakangan ini. Yara yang lembut. Sedikit serak nahan emosi." id b40_010

    yara_kaset "Kai… Aku nggak tahu apa yang sebenarnya terjadi sama kamu. Aku nggak tahu kenapa kamu tiba-tiba menjauh. Kenapa tatapanmu berubah kaku. Kenapa kamu milih ngunci diri sendiri dalam sunyi." id b40_011

    yara_kaset "{i}(tarikan napas, kena mikrofon){/i} Tapi aku mau kamu tahu… di antara semua bising dunia yang kubenci, suara tawamu waktu nemenin aku berburu suara itu melodi paling indah yang pernah kurekam. Aku senang pernah kenal kamu, Kai. Aku… sangat senang." id b40_012

    play sound sfx_klik_play
    show kai biasa at pos_center
    kai "{i}(melepas earphone kasar, menatap jam dinding — 10.00){/i} …Sore ini. Keretanya sore ini. {i}(mengepalkan tangan){/i} Kata Pak Ageng kemarin… kaset merekam suara, bukan perasaan. Yang mutusin tangis itu bakal jadi tangis nyesel atau tangis rindu… aku. Aku sendiri." id b40_013

    kai_hati "Enam bulan aku lari dari hari ini. Enam bulan. {i}(berdiri){/i} Cukup. Aku nggak mau kehilangan dia tanpa ngelakuin apa-apa. Nggak lagi." id b40_014

    ## Adegan 40-3 — Bingkisan balasan ◆ m21
    "Kai membuka laci mejanya. Ada satu kaset kosong yang belum pernah dia pakai — dia mau Yara membawa sesuatu darinya juga, bukan cuma sebaliknya. Tangannya berhenti. Ada beberapa hal yang bisa dia selipkan sekalian." id b40_015

    ## GERBANG MINOR m21 (opsi A HANYA tampil bila item_kaset_kosong_mini dimiliki dari m02=A)
    menu:
        "Apa yang Kai selipkan ke bingkisan untuk Yara?"

        "Kaset kosong mini dari Pak Ageng." if item_kaset_kosong_mini:
            $ record_minor_choice("m21", "A")
            kai_hati "Kaset kosong kecil dari Pak Ageng. Dulu dia bilang: siapa tahu suatu hari aku butuh merekam sesuatu yang beneran dari aku sendiri. {i}(tersenyum tipis){/i} Ternyata bukan buat aku. Buat dia. Biar di Jogja nanti, dia bisa ngirim balik suaranya." id b40_016a

        "Surat pendek.":
            $ record_minor_choice("m21", "B")
            kai_hati "Aku nulisnya empat kali. Yang pertama kepanjangan. Yang kedua kayak surat resmi. Yang ketiga… jujur banget sampai aku malu sendiri. Yang keempat pendek saja. \"Dengar kasetnya pas kamu sudah sampai. Jangan di kereta. — K.\" …Ya. Itu saja." id b40_016b

        "Nggak usah diselipkan apa-apa. Kasetnya saja.":
            $ record_minor_choice("m21", "C")
            kai_hati "Nggak. Nggak pakai tambahan apa-apa. Kalau aku mau ngomong, aku ngomong langsung. Pakai mulut. Pakai suara. Itu… itu justru intinya, kan?" id b40_016c

    $ show_item("item_bingkisan_yara")
    "Bingkisan kecil itu masuk ke tas Kai. Di luar, langit yang dari pagi nahan diri mulai berubah warna." id b40_017

    stop music fadeout 1.0
    return


################################################################################
## BAB 41 — Memotong Pita Takdir [HANYA MAIN PENUH BILA G12 != C]
################################################################################

label bab_41:
    $ chapter_autosave("bab_41", "Bab 41 — Memotong Pita Takdir", "Ch. 41 — Cutting the Tape of Fate")

    ## Adegan 41-1 — Jam dua siang
    scene bg_kamar_kai with dissolve
    play music bgm_peron noloop fadein 1.5
    show kai biasa at pos_center with dissolve

    kai "{i}(menatap jam — 14.00){/i} …Bodoh. Aku ini bodoh banget." id b41_001

    "Kesadaran itu datang kayak ombak nabrak karang. Enam bulan ini, Kai jadi budak ketakutannya sendiri. Dia ngurung diri di sangkar ramalan, biarin masa kininya busuk cuma gara-gara takut sama akhir lagu yang bahkan belum tentu dia pahami." id b41_002
    "Kaset merah itu nggak pernah ngunci takdirnya. Kaset itu cuma merekam keputusasaannya — yang jadi nyata karena dia nyerah duluan." id b41_002_p2

    kai "Kaset itu nggak salah. {i}(menyambar jaket abu-abu di kursi){/i} Aku yang milih percaya terus. Aku yang milih diam terus. {i}(jeda){/i} Wes. Cukup." id b41_003

    kai_hati "Aku nggak peduli lagi sama pita kusut di meja itu. Nggak peduli sama ingatanku yang bolong. Yang ada sekarang cuma satu: Yara. Keretanya berangkat sore ini." id b41_004

    ## Adegan 41-2 — Hujan di jalanan Malang
    scene bg_gang_hujan with dissolve
    play sound sfx_hujan_deras loop fadein 0.6
    show kai cemas at pos_center with dissolve

    "Kai menyambar kunci motor di dekat pintu, mendorong pintu depan — dan langit Malang yang seharian nahan diri akhirnya tumpah. Hujan deras, angin kencang, pohon mangga di sepanjang perumahan goyang semua." id b41_005

    kai "{i}(naik motor, menyalakan mesin sekali injak){/i} Hujan lagi. {i}(memutar gas){/i} Ya sudah. Basah-basah sekalian!" id b41_006

    "Motor melesat. Jalan Sukarno-Hatta licin, penuh genangan. Air hujan menghantam kaca helm sampai Kai terpaksa membukanya — rintik dingin nusuk-nusuk wajah dan matanya. Dia meliuk di antara mobil yang merayap, menerobos genangan di persimpangan, nggak peduli klakson orang marah di mana-mana." id b41_007

    kai_hati "Harus sampai. Harus sampai sebelum sepurnya berangkat. {i}(gigi bergemeletuk kena hujan){/i} Aku nggak bakal biarin tangis di kaset itu jadi tangis perpisahan yang sia-sia. Nggak bakal." id b41_008

    "Di bawah hujan yang makin lebat, satu titik tujuannya: Stasiun Malang Kota Lama. Bukan pita magnetik yang mutusin sore ini. Langkahnya sendiri. Suaranya sendiri." id b41_009

    stop sound fadeout 0.6
    return


################################################################################
## BAB 42 — Pertemuan di Batas Peron ◆ G12 + TITIK EVALUASI 12 GERBANG
################################################################################

label bab_42_g12_dan_evaluasi:
    $ chapter_autosave("bab_42", "Bab 42 — Pertemuan di Batas Peron", "Ch. 42 — Meeting at the Platform Edge")

    ## GERBANG UTAMA G12 (posisi 12 — melengkapi string 12 huruf playthrough).
    ## Diambil sebelum Bab 41 sehingga G12=C melewati Bab 41 & Adegan 42-1 sesuai penanda naskah.
    menu:
        "Sore ini, Kai…"

        "\"Lari. Bicara apa adanya.\"":
            $ record_major_choice(12, "A")

        "\"Lari — tapi yang keluar malah menyalahkan.\"":
            $ record_major_choice(12, "B")

        "Tidak datang.":
            $ record_major_choice(12, "C")

    ## Bab 41 & Adegan inti peron 42-1 hanya dimainkan penuh bila G12 != C (penanda naskah Bab 41–42).
    if get_major_choice(12) != "C":
        call bab_41

        ## Adegan 42-1 — Aula Stasiun Malang Kota Lama [hanya bila G12 != C]
        scene bg_stasiun with dissolve
        play sound sfx_hujan_deras loop fadein 0.5
        show kai panik at pos_center with dissolve

        "Motor Kai mati di parkiran, miring, nggak sempat dia tegakkan beneran. Dia lari nembus tempias hujan, masuk ke aula yang penuh orang berteduh dan calon penumpang bawa kardus, ransel, payung basah. Napasnya memburu. Jaket abu-abunya kuyup — air netes dari ujung rambut dan ujung bajunya ke ubin stasiun." id b42_001

        kai_hati "Di mana… di mana dia… {i}(memindai kerumunan){/i} Jam dinding — tiga lewat lima belas. Keretanya belum berangkat. Belum. Harus belum." id b42_002

        show kai cemas at pos_left with dissolve
        show yara sedih at pos_right with dissolve
        "Dekat loket pemeriksaan tiket, dia melihatnya. Yara. Jalan pelan, menyeret koper hitam besar yang kelihatan keberatan buat badannya. Tas kanvas berisi tripod dan alat rekam masih di bahu kirinya. Headphone hitam besarnya nggak di telinga — menggantung pasrah di leher." id b42_003

        kai "{i}(berteriak, parau){/i} YARA!" id b42_004

        "Teriakan itu membelah bising pengumuman stasiun. Yara berhenti. Bahunya menegang. Pelan-pelan dia berbalik — dan matanya yang sembap membelalak lihat Kai: kuyup dari kepala sampai kaki, napas naik-turun nggak teratur, berdiri di tengah kerumunan." id b42_005

        yara "{i}(hampir nggak kedengaran){/i} Kai…? Kenapa kamu… kenapa kamu basah kuyup begini?" id b42_006

        "Beberapa meter jarak di antara mereka. Di titik ini, seluruh pilihan Kai sejak hari pertama di toko itu — semua kaset, semua diam, semua lari — ditimbang." id b42_007

    ## =========================================================================
    ## TITIK EVALUASI ENDING KANONIK (5 LAPIS — PORT PERSIS `ending_sim.py`)
    ## TEGAS: Varian penutup ditentukan oleh hasil evaluasi seluruh 12 gerbang
    ## (`evaluate_current_ending()` -> `nilai_ending(string12)`),
    ## BUKAN oleh huruf G12 semata!
    ## =========================================================================
    $ _ending_res = evaluate_current_ending(unlock=True)
    $ _ending_id = _ending_res["id"]

    if _ending_id == "H1":
        call ending_h1_happy_true
    elif _ending_id == "H2":
        call ending_h2_happy_sehat
    elif _ending_id == "G":
        call ending_g_gantung
    elif _ending_id == "S1":
        call ending_s1_sad_pasif
    else:
        call ending_s2_sad_ironis

    ## Tampilkan kartu penutup ending lalu kembali ke Menu Utama (progres persisten tetap utuh).
    stop sound fadeout 0.8
    stop music fadeout 1.5
    call screen ending_card(ending_id=_ending_id, choice_code=_ending_res["string"])
    return


################################################################################
## [PENUTUP — HAPPY-TRUE] "Simfoni yang Kita Tulis Sendiri" (H1)
## Lanjut: Bab 43 -> Bab 44 -> Bab 45 (K2) -> Bab 46 True -> Bab 47 (m23) -> [Bab 48 bila K2=A]
################################################################################

label ending_h1_happy_true:
    scene bg_stasiun with dissolve
    show kai cemas at pos_left with dissolve
    show yara sedih at pos_right with dissolve

    "Yara masih terpaku, gagang koper di tangannya melemas. Dan Kai — untuk pertama kalinya setelah enam bulan — nggak mundur." id b42_h1_001

    ## CALLBACK m21 — bingkisan dari Bab 40
    if get_minor_choice("m21") == "A":
        $ show_item("item_kaset_kosong_mini")
        "Sambil melangkah mendekat, Kai mengangkat bingkisan kecil itu. Di dalamnya, kaset kosong mini dari Pak Ageng ikut bergetar pelan kena langkahnya." id b42_h1_002a
    elif get_minor_choice("m21") == "B":
        "Sambil melangkah mendekat, Kai mengangkat bingkisan kecil itu. Di dalamnya ada surat pendek yang dia tulis empat kali." id b42_h1_002b
    else:
        "Sambil melangkah mendekat, tangan Kai kosong selain kaset kosong itu. Nggak ada perantara. Cuma dia dan suaranya." id b42_h1_002c

    kai "{i}(melangkah maju, masih ngos-ngosan){/i} Yar… tunggu. Jangan naik dulu. Aku… aku harus ngomong. Sekarang. Di sini." id b42_h1_003

    call bab_43
    call bab_44
    call bab_45
    call bab_46_true
    call bab_47
    if cond_k2 == "A":
        call bab_48
    return


################################################################################
## [PENUTUP — HAPPY-SEHAT] "Pita yang Tak Pernah Ditukar" (H2)
## Lanjut: Bab 46 Varian Sehat -> Bab 47 (m23)
################################################################################

label ending_h2_happy_sehat:
    scene bg_stasiun with dissolve
    play music bgm_senja loop fadein 1.5
    show kai senyum at pos_left with dissolve
    show yara ceria at pos_right with dissolve

    "Yara menatap Kai yang kuyup itu, lalu — di luar dugaan Kai sendiri — dia ketawa kecil. Ketawa yang capek, tapi lega." id b42_h2_001

    yara "Kamu ini… {i}(menggeleng){/i} Aku nungguin di sekolah dari pagi, kamu nggak nongol-nongol. Eh, malah muncul di stasiun kayak kucing kecebur got." id b42_h2_002

    kai "{i}(masih ngos-ngosan, ikut ketawa pendek){/i} Aku… aku muter dulu ke toko Pak Ageng. Mau nitip salam. Terus… ya, terus hujannya— sudahlah. Nggak penting. {i}(menarik napas){/i} Aku cuma mau pastiin aku ngomong ini langsung. Bukan lewat kaset. Bukan lewat surat. Langsung." id b42_h2_003

    show yara biasa at pos_right
    yara "Ngomong apa?" id b42_h2_004

    kai "Selamat jalan. {i}(jeda; suaranya melembut){/i} Dan makasih. Buat semua suara yang kamu ajarin aku dengar. Dulu kupikir dunia ini bising banget, Yar. Ternyata aku saja yang nggak tahu cara dengarnya." id b42_h2_005

    $ show_item("item_bingkisan_yara")
    "Kai mengeluarkan bingkisan kecil dari tasnya — kaset kosong yang mereka isi berdua dengan rekaman suara mereka sendiri, sebelum hari ini. Bukan ramalan. Bukan bocoran besok. Cuma suara mereka, direkam dengan sadar, buat didengar ulang kapan pun salah satu dari mereka kangen." id b42_h2_006
    $ show_cg_and_unlock("cg_peron_sehat", dissolve)

    yara "{i}(menerima bingkisan itu, tersenyum){/i} Yang ini isinya kita, kan? Bukan \"besok\". Bukan \"tahun depan\"." id b42_h2_007

    kai "Kita. Hari ini. Apa adanya." id b42_h2_008

    yara "{i}(memeluk Kai sekilas — cepat, agak canggung, jaketnya basah — lalu mundur sambil tertawa kecil){/i} Kamu basah banget, sumpah. {i}(mengusap matanya){/i} Jaga diri baik-baik ya, Kai." id b42_h2_009

    kai "Kamu juga. Di Jogja… rekam yang banyak. Kirim ke aku." id b42_h2_010

    yara "Pasti. {i}(mengangkat gagang koper, melangkah mundur ke pintu peron, masih menatapnya){/i} Selamat tinggal." id b42_h2_011

    hide yara with dissolve
    "Kalimat itu terucap juga akhirnya. Tapi di rute ini, kalimat itu ringan. Nggak ada kaset yang menagihnya, nggak ada ramalan yang mengintainya. Cuma dua orang yang berpisah karena hidup memang begitu — dan berjanji, dengan suara mereka sendiri, bahwa lagu ini belum selesai." id b42_h2_012

    stop sound fadeout 0.8
    call bab_46_sehat
    call bab_47
    call epilog_h2_kaset_ultah
    return


################################################################################
## [PENUTUP — GANTUNG] "Sisi B Belum Selesai" (G)
################################################################################

label ending_g_gantung:
    scene bg_stasiun with dissolve
    play music bgm_peron noloop if_changed
    play sound sfx_kereta_lewat
    show kai panik at pos_center with dissolve

    "Kai sampai di peron tepat saat pintu-pintu kereta ditutup. Tepat saat peluit petugas berbunyi. Tepat — dan tetap saja terlambat." id b42_g_001

    kai "{i}(berlari di samping kereta yang mulai bergerak, menepuk-nepuk udara){/i} Yara! YARA!" id b42_g_002

    ## CG Kanonik #5: cg_jendela_kereta (Ending Gantung — aset_manifest.json)
    $ show_cg_and_unlock("cg_jendela_kereta", dissolve)

    "Di balik jendela yang berembun, satu wajah berbalik. Yara. Matanya membesar. Dia menempelkan telapak tangan ke kaca. Kereta berjalan makin cepat — Kai berlari, lalu setengah berlari, lalu cuma bisa jalan cepat sambil terengah." id b42_g_003

    yara "{i}(dari balik jendela, teriakannya teredam kaca dan deru roda){/i} KAI?! Kamu— kamu ngapain—" id b42_g_004

    kai "{i}(berteriak sambil kehabisan napas){/i} Aku… aku mau ngomong… aku selama ini… aku—" id b42_g_005

    play sound sfx_kereta_lewat
    "Enam puluh detik. Kurang lebih segitu waktu yang mereka punya — Kai berlari di peron, Yara menempel di jendela, dua-duanya berteriak tanpa benar-benar mendengar. Enam puluh detik yang sama persis seperti isi kaset pertama yang dulu membuka semua ini." id b42_g_006

    yara "{i}(terdengar samar, terakhir kalinya sebelum jarak menang){/i} Kai… aku belum bisa jawab sekarang." id b42_g_007

    scene bg_stasiun with dissolve
    show kai sedih at pos_center with dissolve
    "Kereta melesat keluar stasiun, membawa kalimat itu pergi sebelum sempat jadi apa-apa. Kai berdiri di ujung peron, kuyup, sendirian, menatap rel yang kosong. Nggak ada putus. Nggak ada janji. Nggak ada apa-apa yang selesai." id b42_g_008

    ## CG Kanonik #6: cg_tombol_play (Penutup Gantung: jari melayang di atas tombol PLAY tanpa pilihan)
    stop music fadeout 1.2
    scene bg_kamar_kai_malam with fade
    $ show_cg_and_unlock("cg_tombol_play", dissolve)

    "Malamnya, di kamar, kaset kosong pemberian Pak Ageng ada di tangan Kai. Jarinya melayang di atas tombol play. Kalau dia tekan, mungkin ada jawaban. Kalau dia tekan, mungkin nggak ada apa-apa. Jarinya berhenti. Gemetar — lalu, dengan satu tarikan napas panjang, ia menekannya." id b42_g_009

    "Tidak ada suara Yara di pita itu. Tidak ada rekaman masa depan yang pernah dijanjikan. Yang terdengar dari balik desis pita hanyalah satu suara tua yang sangat pelan — perpisahan terakhir dari seorang penjaga toko." id b42_g_009b

    call play_cassette(
        cassette_id="kaset_pesan_ageng",
        label_title=_("Side B — Pesan Terakhir Pak Ageng"),
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

    play sound sfx_klik_play
    "— Side B selesai." id b42_g_010

    return


################################################################################
## [PENUTUP — SAD-IRONIS] "Hening Enam Puluh Detik" (S2)
################################################################################

label ending_s2_sad_ironis:
    scene bg_stasiun with dissolve
    stop music fadeout 0.8
    play music bgm_cemas loop fadein 1.5
    show kai panik at pos_left with dissolve
    show yara sedih at pos_right with dissolve

    kai "{i}(melangkah maju, cepat, kalimatnya tumpah nggak terkendali){/i} Yar, dengerin aku dulu. Aku bisa jelasin. Aku menjauh itu karena kasetnya, Yar. Kaset merah itu. Dia nunjukin kamu bakal pergi — kamu nangis, kamu bilang selamat tinggal — aku denger itu semua sebelum kejadian, aku— aku nggak kuat, makanya aku—" id b42_s2_001

    yara "{i}(memotong, pelan){/i} …Kaset?" id b42_s2_002

    kai "Aku nuker kenangan buat denger masa depan. Kenangan kita. Pertemuan pertama kita di perpustakaan itu — aku bahkan sudah nggak inget lagi, Yar, lubang, kosong — tapi itu demi— aku cuma mau siap, aku cuma takut kehilang—" id b42_s2_003

    "Yara nggak langsung jawab. Dia menatap Kai lama — bukan tatapan marah. Tatapan orang yang baru saja ngerti sesuatu yang menyedihkan." id b42_s2_004

    yara "Jadi selama ini… {i}(suaranya kecil){/i} waktu kamu diem, waktu kamu ngejauh, waktu aku mikir aku yang salah — kamu lagi dengerin kaset. Tentang aku. Tanpa aku." id b42_s2_005

    kai "B-bukan gitu maksudku—" id b42_s2_006

    show yara menangis at pos_right
    yara "Kamu nuker ingatan tentang aku… buat ngintip akhir cerita aku. {i}(menggeleng pelan; matanya berkaca-kaca, tapi suaranya rata){/i} Kai. Kamu ke sini bukan untukku." id b42_s2_007

    kai "Yar—" id b42_s2_008

    yara "Kamu ke sini untuk kaset itu. Buat nenangin takutmu sendiri. {i}(menarik gagang kopernya; satu langkah mundur){/i} Aku ini orang, Kai. Bukan… bukan rekaman yang bisa kamu putar-putar sampai kamu tenang." id b42_s2_009

    hide yara with dissolve
    $ show_cg_and_unlock("cg_pita_ironis", dissolve)
    "Pengumuman boarding berbunyi. Yara berbalik dan jalan ke pintu peron — nggak lari, nggak buru-buru. Cuma jalan. Seperti orang yang sudah selesai. Kai berdiri membeku di tengah aula, bingkisan kecil masih di tangannya, nggak pernah sempat dia berikan." id b42_s2_010

    kai_hati "Bukan gitu… aku ke sini buat dia. Aku lari kehujanan buat dia. {i}(jeda panjang){/i} …Kan? Buat dia, kan? Bukan buat… {i}(dia nggak bisa menyelesaikan kalimatnya sendiri){/i}" id b42_s2_011

    "Dan tangis Yara sore itu — yang sempat terdengar waktu dia menaiki tangga kereta — persis seperti di kaset merah. Tangis penyesalan. Persis seperti yang selama ini Kai takutkan. Ramalan itu jadi nyata sore ini. Yang membuatnya nyata: Kai sendiri." id b42_s2_012

    stop sound fadeout 0.6
    scene bg_kamar_kai_malam with fade
    show kai sedih at pos_center with dissolve
    play sound sfx_klik_play

    "Di rumah, tengah malam, Kai akhirnya memutar kaset kosong pemberian Pak Ageng. Kaset yang katanya merekam potensi kebahagiaan." id b42_s2_013

    ## Pemutaran kaset hening 60 detik (aset manifest `kaset_hening_60detik.ogg` — Sad-Ironis)
    call play_cassette(
        cassette_id="kaset_hening_60detik",
        label_title=_("Kaset Kosong — 60 Detik Hening"),
        transcript_lines=[
            (None, _("[Desis. Hening. Hening terus. Tidak ada tawa, tidak ada suara, tidak ada pesan. Tepat enam puluh detik — lalu: klik.]")),
        ],
        duration_sec=60,
        allow_skip=True,
    )

    play sound sfx_klik_play
    "Hening. Tepat enam puluh detik. Lalu klik. Potensi kebahagiaan yang nggak pernah jadi apa-apa." id b42_s2_014

    return


################################################################################
## [PENUTUP — SAD-PASIF] "Desis Statis" (S1)
################################################################################

label ending_s1_sad_pasif:
    stop sound fadeout 0.5
    scene bg_kamar_kai_malam with fade
    play music bgm_cemas loop fadein 1.5
    play sound sfx_hujan_deras loop fadein 0.8
    $ show_cg_and_unlock("cg_kamar_pasif", dissolve)

    "Jam tiga sore. Di kamar yang lampunya nggak dinyalakan, Kai duduk di lantai, punggungnya nempel ke kaki tempat tidur. Bingkisan kecil buat Yara ada di meja — rapi, kering, nggak pernah berangkat ke mana-mana. Di sebelahnya, kaset merah. Di sebelahnya lagi, HP yang layarnya mati sejak kemarin." id b42_s1_001

    kai_hati "Sekarang jam tiga. Keretanya… bentar lagi. Kalau aku lari sekarang — kalau aku naik motor sekarang — mungkin masih… {i}(jeda sangat panjang){/i} …Mungkin. {i}(dia nggak berdiri){/i}" id b42_s1_002

    "Jam tiga lewat sepuluh. Jam tiga lewat dua puluh. Di luar, hujan turun pelan, sopan, nggak kayak di rute-rute lain yang mengharuskan seseorang berlari menembusnya. Di kamar ini hujan cuma jadi suara latar." id b42_s1_003

    kai_hati "Dia pasti mikir aku nggak peduli. {i}(menutup mata){/i} Biar. Biar dia mikir gitu. Itu… lebih gampang. Buat dia. Buat aku juga. {i}(suaranya pecah){/i} …Bohong. Nggak gampang. Nggak gampang sama sekali." id b42_s1_004

    stop sound fadeout 0.6
    play sound sfx_kereta_lewat
    queue sound sfx_pita_kusut
    "Sore itu lewat begitu saja. Malamnya, Kai memutar kaset merah. Desis. Tangis. \"Selamat tinggal.\" Dia putar lagi. Desis. Tangis. \"Selamat tinggal.\" Lagi." id b42_s1_005
    "Sampai suatu malam — entah malam keberapa — Walkman-nya mengeluarkan bunyi gemeretak kasar. Pitanya kusut. Melilit. Rusak permanen. Dan Kai cuma menatapnya, tanpa terkejut, seperti orang yang memang sudah menunggu itu terjadi." id b42_s1_005_p2

    ## Epilog Sad-Pasif: bertahun kemudian, di seberang kedai kopi bekas Toko Gema Masa
    stop music fadeout 1.2
    scene bg_kafe with fade
    play music bgm_cemas loop fadein 1.5
    show kai dewasa at pos_center with dissolve

    "Bertahun-tahun kemudian. Gang itu masih ada, tapi toko di ujungnya sudah bukan toko kaset. Papan \"Gema Masa\" sudah turun. Sekarang di sana kedai kopi yang ramai — lampu hangat, musik pelan, anak-anak muda ketawa di meja-meja yang dulu adalah rak kaset." id b42_s1_006

    "Kai berdiri di seberang gang. Lebih tua. Tas selempang. Dia menatap kedai itu lama. Tangannya sudah terangkat setengah — kayak mau melambai ke seseorang di dalam yang bahkan nggak ada. Lalu turun lagi." id b42_s1_007

    kai_hati "Di dalam situ dulu… ada kursi goyang. Ada teh melati. Ada orang tua yang… {i}(jeda){/i} Aku bahkan nggak pernah pamit sama Pak Ageng. Nggak pernah datang lagi. Setelah hari itu… nggak pernah." id b42_s1_008

    "Seorang barista muda keluar membuang sampah, melirik Kai sekilas — orang asing yang berdiri terlalu lama di seberang. Kai mengangguk kecil, canggung. Lalu berbalik. Dan jalan pulang. Dia nggak masuk. Dia nggak pernah masuk." id b42_s1_009

    return


################################################################################
## BAB 43 — Jarak yang Menjelma Suara [KHUSUS HAPPY-TRUE] ◆ m22
################################################################################

label bab_43:
    $ chapter_autosave("bab_43", "Bab 43 — Jarak yang Menjelma Suara", "Ch. 43 — Distance Turned Into Sound")

    ## Adegan 43-1 — Pengakuan
    scene bg_stasiun with dissolve
    play music bgm_peron noloop if_changed
    show kai menangis at pos_left with dissolve
    show yara sedih at pos_right with dissolve

    "Kai melangkah maju. Genangan kecil terbentuk dari tetesan jaketnya di ubin yang bersih. Jarak beberapa meter itu habis. Sekarang dia bisa lihat jelas-jelas: ujung hidung Yara merah, sisa air mata kering di pipinya." id b43_001

    kai "{i}(suara bergetar, berebut dengan pengeras suara){/i} Aku takut, Yara." id b43_002

    kai "Aku takut karena kaset itu. Aku denger tangisanmu. Aku denger kamu bilang selamat tinggal. Terus aku— aku pengecut. Kupikir kalau aku menjauh duluan, perpisahan hari ini nggak bakal ngancurin kita. {i}(napasnya putus-putus){/i} Aku takut kehilangan duniaku… yang baru saja bunyi lagi gara-gara ada kamu di dalamnya." id b43_003

    "Yara menatapnya. Kalimat itu berantakan. Telanjang. Nggak ada lagi dinding es yang berbulan-bulan ini nyiksa mereka berdua. Hening aneh menggantung sebentar di antara bising stasiun." id b43_004

    show yara menangis at pos_right
    "Lalu bahu Yara berguncang. Yang keluar bukan marah — tawa kecil yang getir, yang pelan-pelan melebur jadi isakan. Dia tertawa sambil menangis, nutupin wajah pakai satu tangan; tangan satunya masih megang gagang koper erat-erat." id b43_005

    yara "{i}(di sela tangis dan tawa){/i} Kamu… kamu tuh bener-bener orang paling bodoh yang pernah kutemui, Kai." id b43_006

    kai "…Aku tahu." id b43_007

    show yara senyum_perpisahan at pos_right
    yara "{i}(mendongak; mata basah, tapi hangat lagi){/i} Aku pergi kuliah, Kai. Bukan pergi mati. Kita cuma beda kota. Bukan beda dunia!" id b43_008

    kai "{i}(terdiam){/i} …" id b43_009

    yara "{i}(satu langkah lebih dekat; tempias air dari jaket Kai kena sepatunya, dia nggak peduli){/i} \"Selamat tinggal\" yang kamu denger di kaset merah itu — ya karena aku memang harus naik kereta ini sore ini!" id b43_010
    yara "Ya aku nangis, aku ninggalin Malang, ninggalin rumahku… ninggalin cowok bodoh yang nganterin aku ke stasiun basah kuyup kayak kucing kehujanan!" id b43_010_p2

    show kai senyum at pos_left
    kai "{i}(ketawa pendek, matanya ikut basah){/i} …Kucing kehujanan. Iya. Iya, mirip sih." id b43_011

    yara "{i}(mengusap air mata kasar pakai lengan jaket denimnya){/i} Jogja itu cuma beberapa jam naik kereta ini, Kai. Kereta ini jalan tiap hari. Suara relnya itu — kita bisa dengerin bareng lewat telepon tiap malam, kalau kamu mau. Kenapa sih kamu bikin ribet sesuatu yang sebenarnya sesederhana itu?" id b43_012

    ## Adegan 43-2 — Janji jarak jauh ◆ m22
    "Kai menatap rel di balik pintu peron, lalu menatap Yara lagi. Buat pertama kalinya, \"jarak\" nggak kedengaran kayak vonis. Kedengaran kayak… jadwal. Sesuatu yang bisa diatur." id b43_013

    kai "Kalau gitu… kita atur beneran. Jangan cuma \"nanti ya, nanti ya\". Nanti-nanti itu bahaya buat aku, Yar. Kamu tahu sendiri." id b43_014

    show yara ceria at pos_right
    yara "{i}(tersenyum kecil){/i} Hmm. Oke. Gimana maumu, Tuan Perencana?" id b43_015

    ## GERBANG MINOR m22 (khusus Happy-True — menentukan montase komunikasi di Bab 44)
    menu:
        "Pola komunikasi jarak jauh mereka:"

        "Telepon tiap Jumat, jam 16.00.":
            $ record_minor_choice("m22", "A")
            kai "Tiap Jumat. Jam empat sore. Jam segitu… jam aku pertama kali denger suara kamu di perpustakaan. Tiap Jumat jam segitu, kita teleponan. Kamu cerita Jogja, aku cerita Malang. Pakai suara. Bukan chat." id b43_016a
            yara "{i}(terdiam sebentar, lalu senyumnya melebar){/i} …Kamu inget jamnya. Oke. Jumat, jam empat. Awas kalau telat." id b43_017a

        "Telepon bebas — kapan pun kangen.":
            $ record_minor_choice("m22", "B")
            kai "Nggak usah dijadwal. Kalau kamu kangen, telepon. Kalau aku kangen, aku telepon. Jam berapa pun. Lagi ngerekam juga angkat dulu, ngomong \"bentar\" kek, apa kek." id b43_016b
            yara "{i}(ketawa){/i} Itu bukan aturan, Kai, itu mah… ya sudah. Itu emang kita banget sih. Oke. Kapan pun." id b43_017b

        "Tukar surat suara.":
            $ record_minor_choice("m22", "C")
            kai "Kita… tukar kaset. Maksudku — rekaman suara. Tiap minggu aku kirim satu kaset ke Jogja: isinya suaraku, suara toko, suara Malang. Kamu kirim balik punya kamu. Kayak surat, tapi suara." id b43_016c
            yara "{i}(matanya berbinar){/i} …Surat suara. {i}(mengangguk cepat){/i} Itu. Itu bagus banget. Itu paling kita. Oke, deal." id b43_017c

    show yara senyum_perpisahan at pos_right
    yara "Deal, ya. {i}(mengangkat kelingking sebentar, lalu menurunkan lagi sambil ketawa kecil){/i} Wes, jangan nangis lagi. Nanti aku ikut— {i}(suaranya pecah duluan){/i} …tuh kan." id b43_018

    return


################################################################################
## BAB 44 — Jeda, Bukan Akhir [KHUSUS HAPPY-TRUE]
################################################################################

label bab_44:
    $ chapter_autosave("bab_44", "Bab 44 — Jeda, Bukan Akhir", "Ch. 44 — A Pause, Not an End")

    ## Adegan 44-1 — Pelukan di peron (CG Kanonik #4: cg_peron)
    scene bg_stasiun with dissolve
    play sound sfx_kereta_lewat
    show kai senyum at pos_left with dissolve
    show yara senyum_perpisahan at pos_right with dissolve

    pengumuman "Perhatian, para penumpang Kereta Api Malioboro Ekspres tujuan Yogyakarta, kereta Anda telah siap di peron satu. Harap segera mempersiapkan tiket dan kartu identitas Anda untuk proses boarding…" id b44_001

    "Waktu mereka habis. Yara menatap Kai lurus-lurus. Semua keraguan, amarah, dan dinding es berbulan-bulan ini menguap — yang sisa cuma kesadaran paling bersih: detik ini punya mereka." id b44_002

    $ show_cg_and_unlock("cg_peron", dissolve)

    "Yara melepas gagang kopernya. Nggak peduli jaket Kai masih kuyup dan dingin, dia melangkah maju dan melingkarkan dua lengannya erat-erat di leher Kai. Memeluknya pakai seluruh tenaga — kayak mau menenggelamkan seluruh jarak yang bakal membentang, ke dalam pelukan itu saja." id b44_003

    "Kai terpaku sejenak. Hangat tubuh Yara nembus kain jaketnya yang dingin, menjalar ke dada yang selama ini hampa. Pelan-pelan, dia mengangkat dua tangannya dan membalas — nggak kalah erat. Wajahnya tenggelam di ceruk leher Yara. Bau gerimis dan sabun tipis. Bau yang dia rindukan berbulan-bulan." id b44_004

    kai_hati "Ini dia. Ini yang ditakutin kaset itu berbulan-bulan. {i}(jeda){/i} …Ternyata rasanya gini. Nggak serem. Sedih, iya. Tapi nggak serem." id b44_005

    ## Adegan 44-2 — "Selamat tinggal"
    scene bg_stasiun with dissolve
    play sound sfx_hujan_deras loop fadein 0.6
    show kai menangis at pos_left with dissolve
    show yara senyum_perpisahan at pos_right with dissolve

    "Yara melepas pelukan itu pelan-pelan. Mundur satu langkah. Menatap wajah Kai — yang sekarang juga basah, dan bukan cuma karena hujan. Dia menarik napas dalam. Berat. Gemetar. Patah-patah. Persis frekuensi yang terekam di kaset merah itu." id b44_006

    yara "{i}(tersenyum di sela tangis; ujung hidungnya merah){/i} Jaga diri baik-baik ya, Kai." id b44_007

    "Suaranya bergetar hebat dan pecah di ujung kalimat. Persis seperti yang Kai dengar sendirian di kamarnya yang sunyi, berbulan-bulan lalu." id b44_008

    yara "{i}(memegang gagang koper, melangkah mundur ke pintu peron, pandangannya nggak lepas dari Kai){/i} Selamat tinggal." id b44_009

    hide yara with dissolve
    "Kalimat itu meluncur. Nyata. Di udara bebas stasiun. Dan kali ini — Kai nggak lemas. Nggak hancur. Jantungnya nggak dipenuhi teror." id b44_010

    show kai senyum at pos_center with dissolve
    if get_minor_choice("m22") == "A":
        kai "{i}(tersenyum, air mata jatuh, tapi suaranya mantap){/i} Selamat tinggal, Yar. {i}(jeda){/i} Sampai Jumat." id b44_011a
    elif get_minor_choice("m22") == "B":
        kai "{i}(tersenyum, air mata jatuh, tapi suaranya mantap){/i} Selamat tinggal, Yar. {i}(jeda){/i}" id b44_011b0
        kai "…Telepon aku pas kamu sampai. Jam berapa pun." id b44_011b
    else:
        kai "{i}(tersenyum, air mata jatuh, tapi suaranya mantap){/i} Selamat tinggal, Yar. {i}(jeda){/i}" id b44_011c0
        kai "…Kaset pertamaku kukirim minggu ini. Tungguin." id b44_011c

    "Di kepalanya, kata-kata Pak Ageng akhirnya utuh: kaset merekam suara, bukan perasaan. \"Selamat tinggal\" itu bukan titik. Dia koma. Koma yang manis — janji kalau lagu mereka masih lanjut, cuma pindah ke pita yang baru." id b44_012

    ## Adegan 44-3 — Montase jarak [CALLBACK m22]
    stop sound fadeout 0.6
    stop music fadeout 1.0
    play music bgm_epilog loop fadein 1.5

    if get_minor_choice("m22") == "A":
        scene bg_kamar_kai with fade
        show kai senyum at pos_center with dissolve
        "Jumat. Jam empat sore kurang semenit, Kai sudah duduk di meja, HP di depan, kayak nunggu ujian. Jam empat tepat — layar menyala." id b44_013a
        yara_telepon "Halo? Tes, tes. Malang kedengaran?" id b44_014a
        kai "{i}(tersenyum lebar){/i} Kedengaran. Jogja juga. Keras malah." id b44_015a
        yara_telepon "Bagus. Berarti jaraknya cuma segitu. Nggak jauh-jauh amat, kan?" id b44_016a

    elif get_minor_choice("m22") == "B":
        scene bg_toko_dalam_malam with fade
        play sound sfx_desis_pita
        show kai senyum at pos_center with dissolve
        "Telepon Kai bunyi jam sebelas malam, waktu dia lagi bantu Pak Ageng beresin rak. Layarnya: \"Yara — Jogja\"." id b44_013b
        kai "{i}(mengangkat, berbisik){/i} Halo? Kamu nggak tidur?" id b44_014b
        yara_telepon "Nggak bisa. Di sini ada suara jangkriknya beda, Kai. Beda sama Malang. Dengerin, deh. {i}(hening dua detik, lalu suara jangkrik dari seberang){/i} …Kedengaran nggak?" id b44_015b
        kai "{i}(ketawa pelan){/i} Kedengaran. Rekam itu. Kirim sebagai kaset juga." id b44_016b

    else:
        scene bg_kamar_kai with fade
        play sound sfx_klik_play
        queue sound sfx_desis_pita
        show kai senyum at pos_center with dissolve
        "Paket dari Jogja datang seminggu kemudian. Satu kaset, label tulisan tangan Yara: \"Sisi A — Jogja, minggu pertama. Putar pas kamu lagi sepi.\"" id b44_013c
        yara_kaset "Halo, Kai. Ini aku, dari kota yang relnya bunyi persis kayak rel di Malang. Ternyata di mana-mana sama saja… {i}(tawa kecil){/i} Sisanya dengerin sendiri. Oh, dan — giliranmu. Aku tunggu Sisi B-nya." id b44_014c
        "Kai menatap kaset kosong di mejanya. Kali ini, dia tahu persis mau ngisi apa." id b44_015c

    "Jarak, ternyata, bisa menjelma suara. Dan suara — kalau dua orangnya mau — nggak pernah benar-benar pergi." id b44_017

    return
