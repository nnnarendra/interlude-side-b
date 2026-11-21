label bab_01:
    $ chapter_autosave("bab_01", "Bab 1 — Suara Hari Esok", "Ch. 1 — Tomorrow's Sound")

    scene bg_gang_hujan with dissolve
    play sound sfx_hujan_deras loop fadein 0.8
    stop music fadeout 0.8

    "Malang, jam lima sore. Langit gelap kayak malam. Kai, 17 tahun, baru pulang sekolah — dan hujan turun sebelum dia sempat sampai rumah." id b01_001

    show kai cemas at pos_center with dissolve
    kai_hati "Yah. Turun juga. Tas nggak ada plastiknya lagi. Buku-buku bisa basah semua ini." id b01_002

    "Dia lari. Bukan ke jalan besar — di sana cuma ada klakson dan genangan setinggi mata kaki. Dia belok ke celah sempit di antara dua gedung, terus masuk, terus masuk… sampai langkahnya berhenti sendiri." id b01_003

    kai_hati "…Ini gang apa? Perasaan aku nggak pernah lewat sini." id b01_004

    "Gang buntu. Selalu basah, kayak hujan di sini nggak pernah benar-benar berhenti. Dan di ujung gang, separuh tersembunyi di balik dinding gelap, ada bangunan kecil dengan papan kayu miring." id b01_005

    scene bg_toko_luar with dissolve
    show kai biasa at pos_center with dissolve
    kai_hati "\"Gema Masa\". Toko kaset? Serius, masih ada toko kaset?" id b01_006

    stop sound fadeout 0.6
    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    play music bgm_toko loop fadein 1.5

    "Pintu didorong. Lonceng kecil berbunyi. Dan anehnya, begitu masuk, suara hujan langsung jauh — seperti ditinggal di luar." id b01_007

    show kai biasa at pos_left with dissolve
    kai_hati "Hangat. Bau kertas tua… sama teh melati. Raknya tinggi-tinggi, kaset semua. Ini toko atau museum?" id b01_008

    show ageng biasa at pos_right with dissolve
    ageng "Di luar lagi nggak bersahabat, ya?" id b01_009

    "Kai kaget. Di balik meja kasir, seorang pria tua bangkit dari kursi goyang. Rambutnya putih, disisir rapi ke belakang. Umurnya mungkin enam puluhan, tapi caranya berdiri tenang sekali." id b01_010

    show kai cemas at pos_left
    kai "E-eh, iya, Pak. Maaf… saya cuma numpang berteduh sebentar. Itu— lantainya jadi basah gara-gara saya. Maaf ya, Pak." id b01_011

    show ageng senyum at pos_right
    ageng "Santai saja. Lantai toko ini sudah biasa kena air hujan. Monggo, duduk dulu. Keringkan badanmu." id b01_012

    play sound sfx_cangkir_teh
    $ show_item("item_teh_melati")
    "Tanpa tanya nama, tanpa tanya keperluan, Pak Ageng menuang teh dari teko tua ke cangkir keramik kecil, lalu menyodorkannya. Di sebelah cangkir ada piring kecil berisi jajanan pasar." id b01_013

    show kai biasa at pos_left
    kai "Oh— nggak usah repot-repot, Pak… {i}(duduk, menangkupkan tangan ke cangkir){/i} …Makasih, Pak." id b01_014

    ageng "Minum dulu. Kamu menggigil itu." id b01_015

    kai "{i}(menyesap){/i} …Enak. Manisnya pas. {i}(jeda, memandang rak){/i} Pak, ini kaset semua? Maksud saya… di zaman sekarang, masih ada yang beli kaset pita?" id b01_016

    show ageng biasa at pos_right
    ageng "Ada. Sebagian orang ke sini cari musik lama. {i}(berjalan ke rak, jarinya menyusuri punggung kaset){/i} Tapi ada juga yang datang bukan buat dengar kemarin, Nak. Buat dengar besok." id b01_017

    kai "…Besok?" id b01_018

    ageng "Hari esok." id b01_019

    "Jantung Kai berdegup satu ketukan lebih lambat. Cangkir di tangannya hampir tumpah." id b01_020

    show kai cemas at pos_left
    kai_hati "Dengar… besok? Dia barusan bilang dengar besok?" id b01_021

    kai "Maksud Bapak… kasetnya bisa— isinya suara besok? Beneran?" id b01_022

    $ hide_item()
    $ show_item("item_kaset_biasa")
    ageng "{i}(mengambil satu kaset biasa dari rak, meletakkannya pelan di konter){/i} Di pita ini terekam suara dari esok harimu. Percakapan yang belum terjadi. Enam puluh detik. Hanya suara besok." id b01_023

    kai "{i}(menelan ludah){/i} Enam puluh detik…" id b01_024

    show ageng serius at pos_right
    ageng "Dan satu aturan. Ini yang paling penting, jadi dengarkan baik-baik. {i}(menatap Kai lurus){/i} Jangan coba mengubahnya. Ojo. Kalau kamu paksa ubah, pitanya kusut." id b01_025

    show ageng biasa at pos_right
    "Pak Ageng meletakkan tiga Kaset Biasa berdampingan. Isinya sama-sama suara besok — beda sampulnya saja: gambar hujan di atap seng, gambar keramaian pasar, gambar gang di pagi hari." id b01_026

    ageng "Pilih satu. Yang mana pun. Biasanya orang memilih yang pertama kali menarik matanya." id b01_027

    menu:
        "Kaset mana yang diambil Kai?"

        "Yang bergambar hujan di atap seng.":
            $ record_minor_choice("m01", "A")
            show ageng senyum at pos_right
            ageng "Hmm. Anak yang suka suara hujan. {i}(tersenyum kecil){/i} Biasanya yang begitu itu pikirannya ramai." id b01_028a

        "Yang bergambar keramaian pasar.":
            $ record_minor_choice("m01", "B")
            ageng "Pasar. Ramai, tapi jujur. Di pasar, semua suara nggak ada yang dibuat-buat." id b01_028b

        "Yang bergambar gang pagi hari.":
            $ record_minor_choice("m01", "C")
            ageng "Gang sepi di pagi hari. Kamu suka tempat yang belum dijamah orang, ya." id b01_028c

    "Kai memegang kaset pilihannya. Plastiknya kasar, pitanya tegang dan utuh. Ringan — tapi entah kenapa tangannya gemetar." id b01_029

    return

label bab_02:
    $ chapter_autosave("bab_02", "Bab 2 — Harga Sebuah Kepastian", "Ch. 2 — The Price of Certainty")

    scene bg_toko_dalam with dissolve
    show kai biasa at pos_left with dissolve
    show ageng biasa at pos_right with dissolve
    play music bgm_toko loop if_changed
    play sound sfx_derit_kursi_goyang loop fadein 0.5

    "Pak Ageng kembali duduk di kursi goyangnya. Derit kayunya pelan, teratur, bikin mengantuk — tapi kepala Kai justru makin ramai." id b02_001

    ageng "Dunia ini jalan menurut garisnya sendiri, Nak. Manusia itu sering merasa lagi pegang kemudi. Padahal… cuma penumpang yang lagi ketakutan." id b02_002

    kai "Pak… saya masih nggak habis pikir. Gimana caranya suara besok bisa ada di sini, sekarang?" id b02_003

    stop sound fadeout 0.5
    show ageng senyum at pos_right
    $ show_item("item_klepon")
    ageng "{i}(tidak menjawab; menyodorkan piring klepon){/i} Makan dulu. Klepon itu makannya sekaligus, jangan digigit separuh. Nanti muncrat." id b02_004

    show kai senyum at pos_left
    kai "{i}(mengambil satu, memasukkan utuh){/i} —Mmh! {i}(kaget, gula merah meletus di mulutnya){/i} …Manis banget. Enak, Pak." id b02_005

    ageng "Nah. Itu nyata, kan? {i}(tersenyum){/i} Sekarang dengar. Di toko ini ada dua jenis kaset." id b02_006

    show ageng biasa at pos_right
    show kai biasa at pos_left
    ageng "Yang pertama, yang kamu pegang itu. Kaset Biasa. C-60, Type I. Murah — cukup uang sakumu beberapa lembar. Isinya enam puluh detik suara besok. Cuma besok. Efeknya ringan: habis dengar, kamu bisa jadi lega… bisa juga malah tambah cemas." id b02_007

    $ hide_item()
    $ show_item("item_kaset_merah")
    kai "Dan… yang itu, Pak? {i}(menunjuk rak khusus berisi sedikit kaset berselongsong merah darah){/i}" id b02_008

    show ageng serius at pos_right
    ageng "{i}(suaranya berubah lebih dingin){/i} Itu Kaset Merah. C-90, Type IV, Metal. Lebih kuat. Enam puluh detik juga — tapi dari jauh. Setengah tahun sampai setahun ke depan." id b02_009

    show kai cemas at pos_left
    kai_hati "Setahun…? Aku bisa tahu aku lulus apa nggak. Aku bisa tahu hidupku masih sesak kayak sekarang apa nggak." id b02_010

    kai "Harganya, Pak?" id b02_011

    ageng "Bukan uang." id b02_012

    kai "Terus apa?" id b02_013

    ageng "Satu kenangan paling bahagia yang kamu punya sekarang. Kamu tukar. Kenangan itu hilang dari kepalamu — permanen. Tersedot masuk ke pita, jadi bahan bakarnya. Perjalanan jauh butuh energi besar, Nak. Dan nggak ada energi yang lebih murni dari kebahagiaan orang." id b02_014

    "Cangkir teh di tangan Kai terasa mendadak dingin." id b02_015

    ageng "Seringnya, masa depan yang didengar itu nggak sepadan sama kenangan yang dibuang. Orang menyesal belakangan — pas dia sadar dia sudah nggak punya alasan buat tersenyum waktu ingat masa lalu." id b02_016

    kai_hati "Kenangan paling bahagia… aku nggak punya banyak. Kalau satu saja hilang… {i}(jeda panjang){/i} Nggak. Belum. Aku belum seputus asa itu." id b02_017

    show kai biasa at pos_left
    kai "Saya… ambil yang biasa saja, Pak." id b02_018

    show ageng biasa at pos_right
    "Kai merogoh saku jaketnya. Uangnya sedikit lembap kena hujan." id b02_019

    menu:
        "Bagaimana Kai membayar?"

        "Bayar penuh, tidak menawar.":
            $ record_minor_choice("m02", "A")
            kai "Ini, Pak. Pas, kan?" id b02_020a
            show ageng senyum at pos_right
            $ show_item("item_kaset_kosong_mini")
            ageng "Pas. {i}(mengambil kaset kosong mini dari bawah konter, menyelipkannya ke kantong kertas bersama kaset Kai){/i} Ini bonus. Kaset kosong, kecil. Simpan saja. Siapa tahu suatu hari kamu butuh merekam sesuatu yang benar-benar dari kamu sendiri." id b02_021a
            $ renpy.notify(ui_tr("notify_item_mini_tape"))
            $ hide_item()

        "Menawar sekali.":
            $ record_minor_choice("m02", "B")
            kai "Pak… bisa kurang dikit? Uang saku saya minggu ini tinggal—" id b02_020b
            ageng "{i}(menggeleng pelan, tidak marah){/i} Harga di toko ini nggak bisa ditawar, Nak. Bukan karena saya pelit. Karena yang kamu beli itu bukan plastiknya." id b02_021b
            kai "…Iya, Pak. Maaf. Ini, pas saja." id b02_022b

        "Bertanya soal cicilan.":
            $ record_minor_choice("m02", "C")
            kai "Pak, kalau… dicicil bisa? Saya bayar separuh dulu, sisanya Jumat depan—" id b02_020c
            show ageng senyum at pos_right
            ageng "{i}(tertawa kecil){/i} Besok itu nggak bisa dicicil, Nak. Dia datang utuh, mau kamu siap atau tidak." id b02_021c
            kai "{i}(menghela napas, mengeluarkan uangnya){/i} …Iya juga sih. Ini, Pak." id b02_022c

    show ageng biasa at pos_right
    ageng "{i}(memasukkan kaset ke kotak bening, menyerahkan){/i} Ini buat hari Jumat. Enam puluh detik." id b02_023

    kai "{i}(membaca label tulisan tangan di kaset){/i} …Jumat." id b02_024

    show ageng serius at pos_right
    ageng "Satu lagi, sebelum kamu pulang. Kaset ini nggak pernah bohong. Tapi telinga manusia sering salah dengar. Ingat itu." id b02_025

    play sound sfx_lonceng_pintu
    scene bg_toko_luar with dissolve
    show kai biasa at pos_center with dissolve
    stop music fadeout 1.2

    menu:
        "Kai pulang lewat mana?"

        "Lewat gang basah lagi.":
            $ record_minor_choice("m03", "A")
            scene bg_gang_hujan with dissolve
            show kai biasa at pos_center with dissolve
            "Di mulut gang, seekor kucing oranye duduk berteduh di bawah pot, menatap Kai seperti sudah kenal lama. Kai berjongkok sebentar." id b02_026a
            show kai senyum at pos_center
            kai "Kamu tinggal di sini? …Jagain tokonya, ya." id b02_027a

        "Lewat jalan besar.":
            $ record_minor_choice("m03", "B")
            "Jalanan masih basah dan ramai. Di papan pengumuman dekat pertigaan, ada poster pertunjukan sekolah yang sudah sobek separuh. Kai meliriknya sekilas, lalu jalan lagi — kaset di tasnya terasa lebih berat dari semua bukunya." id b02_026b

    show kai cemas at pos_center
    kai_hati "Di tas aku ada suara hari Jumat. Aku harusnya senang. Kenapa malah… ya sudahlah. Dengar dulu saja malam ini." id b02_028

    return

label bab_03:
    $ chapter_autosave("bab_03", "Bab 3 — Gema yang Menjadi Nyata", "Ch. 3 — Echoes Made Real")

    scene bg_kamar_kai_malam with dissolve
    stop music fadeout 0.8
    play sound sfx_hujan_deras loop fadein 0.8

    "Kamar Kai sempit dan penuh barang lama: komik bertumpuk, poster yang mulai mengelupas, dan di meja — Walkman perak tuanya. Cat sudutnya sudah terkelupas, tapi tombol-tombolnya masih mantap bunyinya. Klik." id b03_001

    show kai cemas at pos_center with dissolve
    kai_hati "Oke. Oke. Cuma enam puluh detik. Kalau isinya ngaco, berarti tadi aku cuma dikerjain orang tua eksentrik. Kalau isinya beneran… {i}(menarik napas){/i} …nanti saja mikirnya." id b03_002

    "Kaset masuk. Headphone besar dengan bantalan retak terpasang. Kai memejamkan mata. Lalu— play." id b03_003

    stop sound fadeout 0.4
    play sound sfx_desis_pita

    call play_cassette(
        cassette_id="kaset_besok_busarah",
        label_title=_("Kaset Hari Jumat"),
        transcript_lines=[
            (_("Bu Sarah (dari kaset)"), _("Kai! Apa kamu benar-benar tidak memperhatikan saya sejak tadi?!")),
            (None, _("Kai tersentak sampai Walkman-nya hampir jatuh.")),
            (_("Bu Sarah (dari kaset)"), _("Keluar dari kelas sekarang. Kerjakan soal halaman lima puluh sampai enam puluh di perpustakaan. Jangan kembali sampai jam pelajaran saya selesai!")),
        ],
        duration_sec=12,
        allow_skip=True,
    )

    play sound sfx_klik_play
    show kai panik at pos_center with vpunch
    kai "{i}(melepas headphone, napasnya cepat){/i} …Hah. Hahaha. Nggak. Nggak mungkin. Besok memang ada kelas Bu Sarah, otakku cuma… cuma mengarang. Aku terlalu cemas, itu saja. {i}(jeda; menatap Walkman){/i} …Kan?" id b03_004

    scene bg_kelas with dissolve
    play music bgm_sekolah loop fadein 1.2
    play sound sfx_kelas loop fadein 0.6
    show kai cemas at pos_center with dissolve

    "Bu Sarah masuk membawa tumpukan buku dan membantingnya ke meja. Persis seperti di kaset. Kai memutuskan membuktikan kaset itu salah: dia mencatat semua angka, menatap papan tulis sampai matanya perih, tidak menoleh sama sekali." id b03_005

    kai_hati "Fokus. Fokus. Hari ini aku murid paling rajin se-Malang. Nggak bakal ada alasan—" id b03_006

    stop sound fadeout 0.3
    "Pulpennya habis tinta. Refleks, dia membongkar tempat pensil besinya. Klotak-klotik. Di kelas yang hening, bunyinya nyaring sekali. Bu Sarah berhenti menulis. Berbalik. Perlahan." id b03_007

    show kai panik at pos_center
    kai_hati "…Jangan. Jangan bilang kalimat itu. Jangan—" id b03_008

    stop music fadeout 0.4
    show kai panik at pos_left with ease
    show npc_bu_sarah at pos_right with dissolve
    bu_sarah "Kai! Apa kamu benar-benar tidak memperhatikan saya sejak tadi?!" id b03_009

    "Seluruh kelas menoleh. Wajah Kai memanas sampai ke telinga." id b03_010

    bu_sarah "Keluar dari kelas sekarang. Kerjakan soal halaman lima puluh sampai enam puluh di perpustakaan. Jangan kembali sampai jam pelajaran saya selesai!" id b03_011

    show kai sedih at pos_left
    kai "{i}(berdiri, kaki lemas, mengemasi buku tanpa suara){/i} …Baik, Bu." id b03_012

    scene bg_koridor_sekolah with dissolve
    show kai cemas at pos_center with dissolve

    "Di koridor, Kai bersandar ke dinding semen yang dingin. Tangannya masih gemetar." id b03_013

    kai_hati "Kata per kata. Sama persis. Nada marahnya, jedanya, semuanya. Itu bukan sugesti. Itu… rekaman. Rekaman beneran dari hari ini, yang aku dengar kemarin. {i}(menatap kaset kosong di sakunya){/i} Kalau hal sekecil dimarahi guru saja bisa seakurat ini… hal lain di rak toko itu isinya apa saja, ya?" id b03_014

    kai_hati "Harusnya aku tenang sekarang. Aku punya cara mengintip besok. {i}(jeda){/i} Tapi kenapa rasanya malah kayak dicekik?" id b03_015

    return

label bab_04:
    $ chapter_autosave("bab_04", "Bab 4 — Candu Hari Esok", "Ch. 4 — Addicted to Tomorrow")

    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    play music bgm_toko loop fadein 1.2

    "Sejak hari itu, gang yang selalu basah jadi rute wajib Kai sepulang sekolah. Toko Gema Masa berubah fungsi: semacam apotek. Dan kaset-kaset itu — obat penenang dosis tinggi buat kecemasannya." id b04_001

    show kai biasa at pos_left with dissolve
    show ageng biasa at pos_right with dissolve
    ageng "Yang biasa?" id b04_002

    kai "Yang biasa, Pak. {i}(menyerahkan uang saku yang sudah disisihkan){/i} Hari ini ada kue apa, Pak?" id b04_003

    show ageng senyum at pos_right
    ageng "Putu. Makan dulu sebelum pulang. Kamu itu kurus, Nak." id b04_004

    "Malamnya, ritual yang sama: kamar gelap, headphone, enam puluh detik suara besok. Dan anehnya — awalnya kaset itu benar-benar membantu." id b04_005

    scene bg_kamar_kai_malam with dissolve
    stop music fadeout 1.0
    play sound sfx_desis_pita
    show kai biasa at pos_center with dissolve

    kai_hati "Cipratan air… angkot… Besok pagi jangan lewat trotoar jalan utama. Berangkat lebih pagi, lewat sisi dalam." id b04_006

    "Besoknya, dari kejauhan, Kai melihat angkot melindas genangan persis seperti di kaset — tapi seragamnya bersih. Dia tersenyum kecil sendirian." id b04_007

    show kai senyum at pos_center
    kai_hati "…Bisa. Ternyata bisa diakali." id b04_008

    play sound sfx_desis_pita
    ibu_kaset "Kunci motor Ibu di mana, ya? Perasaan kemarin Ibu taruh sini…" id b04_009

    "Pagi harinya, sebelum Ibu bangun, Kai meletakkan kunci motor di meja makan. Diam-diam. Seperti agen rahasia." id b04_010

    kai_hati "Untuk pertama kalinya… aku bangun tanpa dada sesak. Aku tahu apa yang bakal terjadi. Aku bisa siap-siap. {i}(tersenyum){/i} Ini dia. Ini yang selama ini aku cari." id b04_011

    scene bg_kamar_kai_malam with dissolve
    play music bgm_cemas loop fadein 1.2
    play sound sfx_desis_pita
    show kai cemas at pos_center with dissolve

    kai_kaset "Tanganku… berdarah." id b04_012

    play sound sfx_klik_play
    show kai panik at pos_center with vpunch
    kai "{i}(mematikan Walkman, pucat){/i} Nggak. Kali ini nggak. {i}(berdiri, mulai menyingkirkan semua benda kaca dari kamarnya){/i} Pigura — pindah. Gelas — pindah. Cermin kecil — pindah. Besok aku nggak keluar kamar. Titik. Nggak makan malam di luar juga. Aku nggak bakal kena. Nggak bakal." id b04_013

    scene bg_kamar_kai_malam with fade
    show kai biasa at pos_center with dissolve

    "Seharian Kai mengunci diri. Tidak ada kaca pecah. Tidak ada darah. Jam menunjukkan malam — masa krisis lewat. Dia berdiri, lega bukan main, hendak mematikan lampu." id b04_014

    show kai senyum at pos_center
    kai_hati "Menang. Aku menang dari kaset—" id b04_015

    "Kakinya tersandung ujung karpet yang terlipat. Tubuhnya oleng. Tangannya menggapai meja — dan sikunya menyenggol satu-satunya benda kaca yang terlewat: pigura foto di meja belajar." id b04_016

    show kai panik at pos_center with vpunch
    kai "Akh! {i}(terjatuh, telapak tangannya mendarat di serpihan){/i} …Tanganku… berdarah." id b04_017

    "Persis. Intonasinya pun persis. Sambil meringis, Kai menatap darah di telapak tangannya — dan mengerti sesuatu yang mengerikan: usahanya menghindar justru yang mengantarnya ke sana." id b04_018

    play sound sfx_pita_kusut
    $ hook_tape_jammed()
    $ show_cg_and_unlock("cg_pita_kusut", dissolve)

    kai_hati "Pitanya… kusut. {i}(jeda lama){/i} Kata Pak Ageng… kalau dicoba diubah, pitanya kusut. {i}(menatap tangannya yang diperban seadanya){/i} …Tapi aku nggak kapok. Itu yang paling serem. Aku nggak kapok. Besok aku tetap ke toko itu. Aku tetap butuh tahu besok ada apa." id b04_019

    stop music fadeout 1.0
    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    play music bgm_toko loop fadein 1.2
    show kai sedih at pos_left with dissolve
    show ageng serius at pos_right with dissolve

    ageng "{i}(melihat perban di tangan Kai, lalu menatap matanya lama){/i} …Kamu sudah coba mengubahnya, ya." id b04_020

    kai "{i}(menunduk){/i} …Iya, Pak." id b04_021

    ageng "Dan?" id b04_022

    kai "Pitanya kusut. {i}(jeda){/i} Tapi saya tetap ke sini, Pak. Saya tetap… butuh." id b04_023

    show ageng biasa at pos_right
    "Pak Ageng tidak memarahi. Ia hanya mengambil satu Kaset Biasa dan meletakkannya di konter, seperti biasa. Tapi kali ini ia tidak langsung berbalik pergi." id b04_024

    menu:
        "Kai menatap kaset itu. Apa yang dia putuskan soal kebiasaan barunya?"

        "\"Besok saya ke sini lagi, Pak. Tiap hari, kalau bisa.\"":
            $ record_major_choice(1, "A")
            ageng "{i}(menggeser kaset itu pelan ke arah Kai){/i} Hmm. {i}(tidak berkomentar lebih jauh; jam dinding toko terdengar lebih keras dari biasanya){/i}" id b04_025a

        "\"Saya batasi, Pak. Seminggu sekali saja. Janji.\"":
            $ record_major_choice(1, "B")
            show ageng senyum at pos_right
            ageng "{i}(mengangguk kecil){/i} Anak pintar. Obat itu, Nak… yang bikin dia jadi racun biasanya bukan obatnya. Dosisnya." id b04_025b

        "\"Ini yang terakhir, Pak. Saya berhenti. Ini nggak sehat.\"":
            $ record_major_choice(1, "C")
            show ageng senyum at pos_right
            ageng "{i}(tersenyum tipis){/i} Kalau begitu, jangan ambil yang ini juga. Pulanglah. Tidur tanpa tahu besok hujan atau tidak — seperti orang kebanyakan." id b04_025c
            show kai cemas at pos_left
            kai "{i}(menatap kaset itu lama… lalu menggeleng pelan){/i} …Belum bisa, Pak. Maaf. {i}(mengambil kasetnya){/i} Mungkin besok saya berhenti. Besoknya lagi." id b04_026c

    "Apa pun yang Kai katakan sore itu, kakinya tetap membawanya pulang dengan satu kaset di tas. Yang berubah hanyalah: seberapa erat dia menggenggamnya." id b04_027

    return
