## Interlude / Side B — Batch 4 (Bab 13–16)
## Sumber verbatim: NASKAH-VN-MASTER-Interlude-Side-B.md (baris 933–1236)
## Gerbang: G3 (Bab 13), m10 (Bab 14), m11 (Bab 15), G4 (Bab 16)
## CG & Pencapaian: cg_headphone (Bab 16-1), ach_telinga_kedua (G4=A)

################################################################################
## BAB 13 — Mencari Gema di Kelas Sebelah
################################################################################

label bab_13:
    $ chapter_autosave("bab_13", "Bab 13 — Mencari Gema di Kelas Sebelah", "Ch. 13 — Searching for Echoes Next Door")

    ## Adegan 13-1 — Kamar Kai, malam setelah perpustakaan ◆ G3
    scene bg_kamar_kai_malam with dissolve
    stop music fadeout 0.8
    play sound sfx_desis_pita
    show kai biasa at pos_center with dissolve

    "Sudah tiga hari sejak sore di perpustakaan itu. Kaset-kaset besok tetap diputar, tetap benar. Tapi yang berputar di kepala Kai sekarang bukan ramalan — melainkan suara tumpukan buku jatuh, dan seorang gadis dengan boom mic yang menatapnya datar." id b13_001

    kai_hati "Aku nggak tahu namanya. Nggak tahu kelasnya. Taunya cuma: dia merekam suara-suara aneh, dan gara-gara dia… aku nggak jadi mati hari Jumat. {i}(jeda){/i} Kedengarannya gila. Tapi tetap saja kepikiran." id b13_002

    kai_hati "Besok di sekolah… gimana?" id b13_003

    ## GERBANG UTAMA G3 (posisi 3 string 12 huruf)
    menu:
        "Apa yang Kai putuskan soal gadis di perpustakaan itu?"

        "\"Cari tahu siapa dia.\"":
            $ record_major_choice(3, "A")

        "\"Biarin. Kalau memang ketemu lagi, ya ketemu.\"":
            $ record_major_choice(3, "B")

        "\"Jangan ke perpustakaan lagi. Titik.\"":
            $ record_major_choice(3, "C")

    if get_major_choice(3) == "A":
        ## Adegan 13-2A — Kantin, jam istirahat [jika G3 = A]
        scene bg_kantin with dissolve
        play music bgm_sekolah loop fadein 1.2
        play sound sfx_kelas loop fadein 0.6
        show kai biasa at pos_center with dissolve

        "Kai duduk di sudut kantin, es tehnya diaduk-aduk tanpa diminum. Telinganya justru bekerja penuh — menangkap obrolan teman-teman sekelasnya. Akhirnya dia memberanikan diri memancing." id b13_004a

        kai "Eh… kalian tahu nggak, anak yang suka bawa alat rekam ke perpustakaan itu siapa? Yang headphone-nya gede itu, lho." id b13_005a

        show kai biasa at pos_left with ease
        show npc_teman1 at pos_right with dissolve
        teman1 "Oh, anak aneh dari kelas sebelah itu? XI-Sosial?" id b13_006a

        show npc_teman2 at pos_center with dissolve
        teman2 "Yara. Namanya Yara. Di angkatan kita dia dijuluki \"Gadis Aneh\", rek." id b13_007a

        kai "Aneh kenapa?" id b13_008a

        teman2 "Ya kerjaannya tiap hari cuma pakai headphone besar, jalan keliling sekolah bawa mikrofon panjang. Kemarin aku lihat dia jongkok dekat selokan. Merekam suara air, katanya. Nggak jelas banget, kan? {i}(terkekeh){/i}" id b13_009a

        teman1 "Katanya sih dia ngumpulin suara-suara berisik yang nggak penting gitu." id b13_010a

        "Obrolan beralih ke pertandingan bola nanti sore. Kai tidak ikut tertawa. Dia meletakkan gelas es tehnya yang sudah berkeringat." id b13_011a

        show kai senyum at pos_left
        kai_hati "Yara. {i}(mengulang pelan dalam hati){/i} Namanya Yara. Pendek. Kayak jeda ketukan di lagu yang belum selesai." id b13_012a

        stop sound fadeout 0.5
        scene bg_koridor_sekolah with dissolve
        show kai biasa at pos_center with dissolve
        "Dalam perjalanan ke kelas, Kai sengaja lewat depan kelas XI-Sosial. Di papan dekat pintu tergantung daftar piket kelas itu — dan di baris hari Kamis, tertulis nama yang sama. YARA." id b13_013a

        show kai senyum at pos_center
        kai_hati "Beneran Yara. Oke. Besok aku sapa. Besok. Pasti." id b13_014a

    elif get_major_choice(3) == "B":
        ## Adegan 13-2B — Koridor sekolah [jika G3 = B]
        scene bg_koridor_sekolah with dissolve
        play music bgm_sekolah loop fadein 1.2
        show kai biasa at pos_center with dissolve

        "Kai tidak bertanya ke siapa pun. Tidak juga berani lewat depan kelas XI-Sosial. Dia cuma menjalani hari seperti biasa — atau berusaha terlihat biasa." id b13_004b

        kai_hati "Kalau memang harus ketemu lagi, sekolah ini nggak besar-besar amat. Pasti ketemu. {i}(jeda){/i} …Mudah-mudahan ketemu." id b13_005b

        show kai sedih at pos_center
        "Tapi anehnya, seharian itu tidak ada tanda-tanda headphone besar atau mikrofon panjang di mana pun. Dan Kai pulang dengan perasaan yang tidak dia akui sebagai kecewa." id b13_006b

    else:
        ## Adegan 13-2C — Seminggu menghindar [jika G3 = C]
        scene bg_koridor_sekolah with dissolve
        play music bgm_sekolah loop fadein 1.2
        show kai cemas at pos_center with dissolve

        "Seminggu penuh Kai mengambil jalan memutar. Koridor timur memang lebih jauh ke kelasnya — tapi koridor itu tidak melewati perpustakaan." id b13_004c

        kai_hati "Bukan takut. Aku cuma… nggak mau kejadian kayak kemarin terulang. Orang normal nggak ketawa histeris di perpustakaan gara-gara nggak jadi mati. {i}(jeda){/i} Pokoknya jangan ke sana dulu." id b13_005c

        scene bg_perpustakaan with fade
        show kai sedih at pos_center with dissolve
        "Hari kedelapan, tugas kelompok memaksanya kembali. Dan perpustakaan itu sudah berubah sedikit: kursi dekat jendela — kursi gadis itu — sekarang dipakai anak lain. Jam kunjungannya rupanya sudah pindah." id b13_006c

        kai_hati "…Yah. Pindah jam. {i}(duduk, membuka buku tanpa benar-benar membaca){/i} Ya sudah. Memang itu mauku, kan?" id b13_007c

    ## Adegan 13-3 — Depan kelas XI-Sosial [semua rute, nada menyesuaikan G3]
    scene bg_koridor_sekolah with dissolve
    play music bgm_sekolah loop if_changed
    play sound sfx_hujan_deras loop fadein 0.8
    show kai biasa at pos_left with dissolve

    "Bel masuk berbunyi. Kai berjalan menyusuri koridor kelas XI-Sosial — hari ini memang giliran kelasnya lewat sini — dan langkahnya ia perlambat waktu melewati pintu yang terbuka lebar." id b13_015

    show yara biasa at pos_right with dissolve
    "Di sana. Dekat jendela, baris paling belakang. Gadis itu duduk menopang dagu, menatap lapangan yang diguyur gerimis tipis. Headphone hitam besar melingkar di lehernya. Tangannya memainkan perekam saku kecil di atas meja. Teman-teman sekelasnya melempar kertas dan berteriak-teriak — tapi semua itu seperti tidak sampai ke dia." id b13_016

    kai_hati "Itu dia. Tenang banget. Kayak ada dinding kaca di sekelilingnya, dan cuma dia yang tahu." id b13_017

    show yara penasaran at pos_right
    "Gadis itu menoleh. Pandangan mereka bertemu di antara ramainya koridor. Dia sedikit mengernyit — mengenali Kai: laki-laki yang tertawa seperti orang kesurupan di perpustakaan." id b13_018

    if get_major_choice(3) == "A":
        show yara biasa at pos_right
        yara "{i}(menatapnya datar, lalu berkata cukup keras untuk didengar){/i} …Kamu yang kemarin nanya-nanya soal aku di kantin, ya?" id b13_019a

        show kai panik at pos_left
        kai "{i}(membeku){/i} E-eh?! Kok kamu—" id b13_020a

        yara "Sekolah ini kecil. {i}(kembali menatap ke luar jendela){/i} Lain kali kalau penasaran, tanya langsung saja." id b13_021a

    elif get_major_choice(3) == "B":
        show yara biasa at pos_right
        "Yara menatapnya datar beberapa detik. Tidak marah, tidak tersenyum. Lalu kembali menatap ke luar jendela, seolah Kai cuma satu suara lagi di koridor yang bising." id b13_019b

    else:
        show yara penasaran at pos_right
        yara "{i}(mengangkat alis){/i} Oh. Masih hidup ternyata." id b13_019c

        show kai cemas at pos_left
        kai "…Hah?" id b13_020c

        show yara biasa at pos_right
        yara "Seminggu nggak kelihatan di perpustakaan. {i}(kembali menatap jendela){/i} Kupikir Laki-laki Penunggu Mati sudah beneran mati." id b13_021c

    hide yara with dissolve
    show kai senyum at pos_center with dissolve
    "Kai menarik napas dalam-dalam. Jantungnya berdegup kencang — tapi kali ini bukan karena takut. Rasanya beda. Rasanya seperti… awal." id b13_022

    kai_hati "Kemarin aku jalan ke arah akhir segalanya. Hari ini… kayaknya aku lagi jalan ke arah sesuatu yang baru. Sesuatu yang berisik. {i}(tersenyum tipis){/i} Dan aku pengin mempelajarinya." id b13_023

    stop sound fadeout 0.6
    return


################################################################################
## BAB 14 — Melodi dari Panci yang Bergolak
################################################################################

label bab_14:
    $ chapter_autosave("bab_14", "Bab 14 — Melodi dari Panci yang Bergolak", "Ch. 14 — Melody from a Boiling Pot")

    ## Adegan 14-1 — Kantin, siang
    scene bg_kantin with dissolve
    play music bgm_sekolah loop if_changed
    play sound sfx_kelas loop fadein 0.6
    show kai biasa at pos_left with dissolve

    "Kantin siang itu bisingnya luar biasa. Denting sendok, tawa anak-anak di sudut, penjual yang teriak-teriak menawarkan dagangan — semua bertumpuk jadi satu." id b14_001

    show yara fokus at pos_right with dissolve
    "Tapi di tengah kekacauan itu, Yara seperti pulau yang sunyi. Di pojok kantin, dekat stan mie, dia berjongkok. Headphone besarnya terpasang separuh — telinga kiri tertutup, telinga kanan terbuka. Tangannya terulur stabil, mengarahkan mikrofon kecil ke panci aluminium raksasa di atas kompor mawar. Uap putih mengepul tebal." id b14_002

    ## Nada pembuka Bab 14 menyesuaikan G3
    if get_major_choice(3) == "A":
        kai_hati "Oke. Kemarin dia bilang: tanya langsung saja. {i}(menarik napas){/i} Langsung saja. Jangan muter-muter lagi." id b14_003a
    elif get_major_choice(3) == "B":
        kai_hati "Nah. Ketemu juga, kan? {i}(menelan ludah){/i} …Terus sekarang apa? Masa cuma dilihatin dari jauh lagi." id b14_003b
    else:
        kai_hati "Dia di sini. Bukan di perpustakaan. {i}(jeda){/i} Seminggu aku menghindar, eh, ketemunya di kantin. Alam semesta ini bercandanya keterlaluan." id b14_003c

    "Kai melangkah pelan, menjaga sepatunya tidak berdecit di lantai kantin yang licin. Tenggorokannya mendadak kering. Aneh — biasanya dia cemas soal besok. Kali ini dia gugup soal sekarang." id b14_004

    show kai cemas at pos_left
    kai "{i}(pelan, hampir berbisik){/i} …Sedang apa?" id b14_005

    "Yara tidak kaget. Dia melirik sekilas dari balik bahu, mengenali Kai, lalu kembali menatap gelembung-gelembung air di panci." id b14_006

    yara "Merekam suara air mendidih. {i}(tanpa menoleh){/i} Diam dulu sebentar. Frekuensinya lagi bagus." id b14_007

    show kai biasa at pos_left
    "Kai langsung mengatupkan bibir. Dia ikut berjongkok di samping Yara, menjaga jarak supaya tidak menyenggol sikunya." id b14_008

    play sound sfx_panci loop fadein 0.6
    kai_hati "Bup… bup-bup… bup. Gelembungnya nabrak-nabrak dinding panci. Hampir semenit kami jongkok berdua di pojok kantin yang panas ini. Dan anehnya… aku nggak keberatan." id b14_009

    ## Adegan 14-2 — "Kamu lagi" ◆ m10
    stop sound fadeout 0.4
    play sound sfx_klik_play
    show yara penasaran at pos_right
    "Yara menekan tombol stop. Dia mengembuskan napas lega, menurunkan headphone ke leher, lalu berbalik menghadap Kai dengan satu alis terangkat." id b14_010

    yara "Kamu lagi. Laki-laki yang kemarin tertawa kayak orang kesurupan. {i}(menatapnya){/i} Kenapa sekarang ngikutin aku?" id b14_011

    show kai cemas at pos_left
    kai "Aku nggak ngikutin. {i}(mengalihkan pandang ke mangkuk mie kosong di meja dekat situ){/i} Aku cuma… penasaran. Kenapa kamu rekam suara air mendidih? Itu kan cuma… kebisingan biasa?" id b14_012

    play sound sfx_panci loop fadein 0.5
    "Sebelum Yara menjawab, panci di kompor sebelah bergolak makin keras — dan ibu penjual mie mulai kewalahan mengangkat panci kedua yang lebih kecil." id b14_013

    ## GERBANG MINOR m10 (opsi A memberi item file suara panci)
    menu:
        "Apa yang Kai lakukan selagi Yara menyiapkan jawaban?"

        "Diam-diam merekam suara panci itu dengan HP-nya.":
            $ record_minor_choice("m10", "A")
            "Kai mengeluarkan HP dari saku, membuka aplikasi perekam, dan mengarahkannya ke panci. Tangannya agak gemetar, tapi rekamannya jalan." id b14_014a
            $ renpy.notify(ui_tr("notify_item_panci"))
            show yara penasaran at pos_right
            yara "{i}(melirik HP Kai, alisnya naik sedikit){/i} …Kamu ngapain?" id b14_015a
            show kai cemas at pos_left
            kai "E-eh, ini… iseng. Habisnya suaranya… ya, lumayan, kan?" id b14_016a
            show yara ceria at pos_right
            yara "{i}(menahan senyum){/i} Iseng. Hm. Ya sudah, simpan yang benar. Siapa tahu kepakai." id b14_017a

        "Mendengarkan saja, tanpa merekam.":
            $ record_minor_choice("m10", "B")
            "Kai tetap jongkok, diam, membiarkan suara bergolak itu masuk apa adanya. Tidak ada yang dia simpan selain ingatannya sendiri." id b14_014b
            show yara biasa at pos_right
            yara "{i}(mengamati Kai sebentar){/i} Kamu bisa diam juga ternyata." id b14_015b
            show kai biasa at pos_left
            kai "…Baru belajar." id b14_016b

        "Refleks membantu ibu penjual mengangkat panci.":
            $ record_minor_choice("m10", "C")
            show kai biasa at pos_left
            kai "Bu, saya bantu, Bu— {i}(mengangkat sisi panci bertiga dengan ibu penjual){/i} …Nah. Hati-hati, panas." id b14_014c
            show npc_ibu_penjual at pos_right with dissolve
            ibu_penjual "Lho, makasih, Le. Jarang-jarang ada anak mau bantu. {i}(menyendokkan lauk ekstra ke mangkuk pesanan Kai nanti){/i} Ini, bonus. Jangan bilang siapa-siapa." id b14_015c
            show yara ceria at pos_right
            yara "{i}(menatap Kai, nadanya melunak){/i} …Kamu selalu begitu? Lihat orang repot langsung nyamperin?" id b14_016c
            kai "Nggak selalu. Kadang aku cuma… ya, refleks saja." id b14_017c

    stop sound fadeout 0.8
    show yara biasa at pos_right
    "Yara menatap panci yang masih mengepulkan uap di samping mereka, lalu beralih menatap wajah Kai. Tatapannya tajam, tapi dalam." id b14_018

    yara "Semua orang bilangnya itu bising, Kai." id b14_019

    show kai cemas at pos_left
    kai "…Kamu tahu namaku?" id b14_020

    show yara ceria at pos_right
    yara "Kemarin kamu nanya-nanya soal aku di kantin, ingat? {i}(tersenyum tipis){/i} Gantian, dong. Aku juga nanya. — Semua orang menyebutnya bising. Tapi buat alat ini, itu lagu yang jujur." id b14_021

    return


################################################################################
## BAB 15 — Kejujuran di Balik Kebisingan
################################################################################

label bab_15:
    $ chapter_autosave("bab_15", "Bab 15 — Kejujuran di Balik Kebisingan", "Ch. 15 — Honesty Beneath the Noise")

    ## Adegan 15-1 — Portofolio
    scene bg_kantin with dissolve
    play music bgm_sekolah loop if_changed
    show kai biasa at pos_left with dissolve
    show yara biasa at pos_right with dissolve

    "Yara merapikan kabel mikrofonnya dengan gerakan yang tenang dan terbiasa. Di tengah kantin yang riuh, dia seperti punya ruang sunyi sendiri yang tidak bisa ditembus siapa pun." id b15_001

    yara "Aku ngumpulin suara-suara ini buat portofolio. {i}(menepuk tas kanvasnya yang penuh alat rekam){/i} Aku pengin masuk jurusan seni musik. Tapi bukan musik yang biasa diajarkan di sekolah." id b15_002

    kai "{i}(mengerutkan kening, masih berjongkok){/i} Bukan musik biasa? Maksudnya… bukan band, bukan orkestra?" id b15_003

    show yara ceria at pos_right
    yara "{i}(mendengus pelan, senyumnya agak sinis tapi manis){/i} Aku benci musik pop yang terlalu teratur. Nadanya disusun rapi, kordnya bisa ditebak, liriknya manis-manis dipaksakan. Buatku itu semua… palsu." id b15_004

    "Dia mengangkat perekam sakunya, menunjukkannya tepat di depan wajah Kai." id b15_005

    yara "Aku lebih suka noise. Kebisingan yang jujur. {i}(matanya berbinar){/i} Suara air mendidih. Derit pintu perpustakaan yang belum dikasih pelumas. Gesekan ban truk di aspal basah. Mereka nggak pura-pura terdengar indah. Mereka bersuara karena mereka ada." id b15_006

    kai_hati "Aneh. Penjelasannya asing banget. Tapi ada bagian di dadaku yang… setuju. Aku kan juga muak sama dunia yang serba diatur, serba cepat, serba harus begini-begitu." id b15_007

    show yara fokus at pos_right
    yara "{i}(menatap Kai lurus-lurus){/i} Dunia ini berisik, Kai. Kalau kamu cuma mau dengar yang indah-indah saja… kamu sebenarnya tuli sama separuh kehidupan." id b15_008

    "Kalimat itu menghantam Kai pelan-pelan, seperti gelombang." id b15_009

    show kai cemas at pos_left
    kai_hati "Tuli sama separuh kehidupan… Aku selama ini ngapain? Aku pakai kaset-kaset itu buat menyaring besok. Cuma pengin dengar yang pasti-pasti saja. Yang aman. Sisanya — kututup telinga rapat-rapat. {i}(jeda){/i} Termasuk… kejutan kayak ketemu dia." id b15_010

    kai "{i}(lirih, menerawang){/i} Tuli sama separuh kehidupan…" id b15_011

    ## Adegan 15-2 — Suara yang paling dibenci ◆ m11
    show yara biasa at pos_right
    yara "{i}(berdiri, menepuk-nepuk rok abu-abunya yang kena debu lantai){/i} Kenapa? Kesindir?" id b15_012

    show kai biasa at pos_left
    kai "{i}(buru-buru ikut berdiri){/i} Nggak— ya… dikit. {i}(menggaruk kepala){/i} Dikit banget. Nggak, lumayan sih." id b15_013

    show yara ceria at pos_right
    yara "{i}(tertawa kecil){/i} Jujur juga akhirnya. — Ngomong-ngomong, aku penasaran satu hal. {i}(menatapnya menyelidik){/i} Suara apa yang paling kamu benci?" id b15_014

    kai "Hah? Kok tiba-tiba?" id b15_015

    show yara penasaran at pos_right
    yara "Setiap orang punya. Ayo. Yang pertama kepikiran saja, nggak usah dipikir lama-lama. Justru itu yang jujur." id b15_016

    ## GERBANG MINOR m11 (callback dibayar di Bab 18-3)
    menu:
        "Suara apa yang paling dibenci Kai?"

        "\"Suara bel masuk.\"":
            $ record_minor_choice("m11", "A")
            kai "Bel masuk. Serius. Bunyinya kayak… perintah. \"Sudah, waktunya takut lagi.\"" id b15_017a
            show yara biasa at pos_right
            yara "{i}(mengangguk pelan){/i} Bel masuk. Oke. Kucatat." id b15_018a

        "\"Suara orang berbisik.\"":
            $ record_minor_choice("m11", "B")
            kai "Orang berbisik. Kedengarannya kayak ada yang disembunyiin… dan biasanya yang disembunyiin itu soal aku. {i}(tertawa kering){/i} Kedengarannya paranoid, ya." id b15_017b
            show yara ceria at pos_right
            yara "Sedikit. {i}(tersenyum){/i} Tapi jujur. Kucatat." id b15_018b

        "\"Suara diam.\"":
            $ record_minor_choice("m11", "C")
            show kai sedih at pos_left
            kai "{i}(jeda){/i} Diam. Hening. Kalau ruangan tiba-tiba sepi total… kepalaku langsung ngisi sendiri pakai hal-hal yang nggak-nggak." id b15_017c
            show yara fokus at pos_right
            yara "{i}(menatapnya lebih lama dari biasanya){/i} …Diam. Oke. Yang itu… kucatat baik-baik." id b15_018c

    show yara biasa at pos_right
    yara "{i}(memasukkan perekam ke tas kanvas, bersiap pergi){/i} Sudah. Bel masuk sebentar lagi bunyi. Aku harus balikin beberapa alat ke ruang seni." id b15_019

    show kai biasa at pos_left
    kai_hati "Dia mau pergi. Percakapan ini selesai. {i}(jeda){/i} …Aku nggak mau selesai. Baru kali ini aku ngobrol sama orang dan besok nggak terasa kayak ancaman. Besok terasa kayak… lembar kosong. Yang pengin kudengar bareng dia." id b15_020

    kai "Ya— ya sudah. Hati-hati. {i}(setelah Yara melangkah dua langkah){/i} …Yara." id b15_021

    show yara penasaran at pos_right
    yara "{i}(berhenti, menoleh){/i} Hm?" id b15_022

    show kai senyum at pos_left
    kai "{i}(membuka mulut, menutupnya lagi, akhirnya:){/i} Nggak. Nggak apa-apa. Sampai ketemu lagi." id b15_023

    show yara ceria at pos_right
    yara "{i}(mengangkat bahu, tersenyum tipis){/i} Pasti ketemu. Sekolah ini kecil." id b15_024

    return


################################################################################
## BAB 16 — Ketika Bising Menjelma Simfoni
################################################################################

label bab_16:
    $ chapter_autosave("bab_16", "Bab 16 — Ketika Bising Menjelma Simfoni", "Ch. 16 — When Noise Becomes a Symphony")

    ## Adegan 16-1 — Headphone berdua
    scene bg_kantin with dissolve
    play music bgm_sekolah loop if_changed
    play sound sfx_kelas loop fadein 0.6
    show kai biasa at pos_left with dissolve
    show yara fokus at pos_right with dissolve

    "Siang berikutnya, tanpa rencana apa pun, kaki Kai membawanya lagi ke pojok kantin itu. Yara sudah di sana — kali ini tidak jongkok, hanya berdiri memegang mikrofonnya ke arah keramaian, seperti orang memancing di sungai yang deras." id b16_001

    yara "{i}(tanpa menoleh){/i} Kamu lagi." id b16_002

    kai "Kamu selalu tahu, ya." id b16_003

    show yara biasa at pos_right
    yara "Langkahmu kedengaran. Semua orang jalannya buru-buru. Kamu… kayak orang yang lagi minta izin sama lantai. {i}(berbalik, menatapnya){/i} Sini." id b16_004

    show kai cemas at pos_left
    kai "Hah? Sini kenapa—" id b16_005

    show yara ceria at pos_right
    yara "Pakai ini." id b16_006

    "Sebelum Kai sempat mencerna, Yara sudah melangkah mendekat dan memasangkan headphone hitam besarnya ke telinga Kai. Gerakannya cepat, tanpa permisi. Ada sisa kehangatan tipis di bantalan headphone itu — bekas dipakai Yara." id b16_007

    ## CG Kanonik #2: cg_headphone (dipakai Bab 16 — aset_manifest.json)
    stop sound fadeout 0.6
    stop music fadeout 0.8
    $ show_cg_and_unlock("cg_headphone", dissolve)
    play music bgm_senja loop fadein 1.5

    "Dan dunia berubah. Bising kantin yang biasanya cuma satu bongkahan kacau, sekarang terurai jadi lapisan-lapisan yang detail sekali. Lewat mikrofon sensitif di tangan Yara, Kai mendengar hal-hal yang selama ini lolos begitu saja." id b16_008

    play sound sfx_hujan_deras loop fadein 0.8
    kai_hati "Itu… hujan di atap seng. Bunyinya kayak alat musik. Acak, tapi berpola." id b16_009

    kai_hati "Klakson. Dari sini kedengarannya malah kayak… melodi sedih di tengah macet." id b16_010

    kai_hati "Langkah kaki. Semua orang. Dekat banget, bertekstur banget… kayak mereka lagi menari di dalam kepalaku." id b16_011

    "Kai memejamkan mata. Untuk pertama kalinya, kebisingan dunia tidak membuatnya cemas. Di bawah panduan telinga Yara, dia mulai mendengar musik di dalam kekacauan." id b16_012

    yara "{i}(suaranya terdengar jauh, dari luar headphone){/i} Gimana? Masih kamu anggap bising yang nggak berguna?" id b16_013

    stop sound fadeout 0.8
    scene bg_kantin with dissolve
    show kai senyum at pos_left with dissolve
    show yara ceria at pos_right with dissolve
    "Kai membuka mata perlahan. Dia melepaskan headphone itu dan menyerahkannya kembali ke Yara. Lalu dia tersenyum — senyuman tulus yang jarang sekali muncul di wajahnya." id b16_014

    kai "Nggak. Ini… luar biasa. Rasanya kayak ada dunia lain yang selama ini nggak pernah kudengar. {i}(jeda){/i} Dan dia ada di situ saja, tiap hari. Aku saja yang nggak pernah dengar." id b16_015

    yara "{i}(tersenyum puas){/i} Nah. Laki-laki Penunggu Mati ternyata bisa diajak dengar juga." id b16_016

    kai "Kamu masih manggil aku begitu, ya." id b16_017

    show yara biasa at pos_right
    yara "Julukan bagus itu susah dibuang. {i}(mengemasi alatnya){/i} Lagipula kamu belum kasih aku alasan buat ganti." id b16_018

    ## Adegan 16-2 — Tawaran ◆ G4
    "Yara menggendong tas kanvasnya yang berat — tripod, kabel-kabel, perekam cadangan — lalu melangkah pergi seperti biasa. Tapi tiga langkah kemudian dia berhenti." id b16_019

    yara "{i}(tanpa berbalik){/i} Besok aku ke kolong jembatan dekat stasiun. Gema suaranya unik di sana. {i}(jeda){/i} Lusa ke pasar. Besoknya… entah. Jadwal buruanku banyak." id b16_020

    show kai cemas at pos_left
    kai_hati "Dia ngomong ke aku. Itu bukan obrolan basa-basi. Itu… {i}(menelan ludah){/i} Itu pintu. Pintu yang dia buka sedikit. Tinggal aku berani masuk atau nggak." id b16_021

    ## GERBANG UTAMA G4 (posisi 4 string 12 huruf; opsi A memicu ach_telinga_kedua)
    menu:
        "Apa jawaban Kai?"

        "\"Mulai besok, aku ikut.\"":
            $ record_major_choice(4, "A")
            show kai senyum at pos_left
            kai "{i}(cepat, sebelum keberaniannya hilang){/i} Mulai besok, aku ikut. Tasmu berat, kan? Biar aku yang bawa. Kamu pegang mikrofonnya saja." id b16_022a
            show yara ceria at pos_right
            yara "{i}(berbalik, menatapnya lama — lalu tersenyum lebar untuk pertama kalinya){/i} …Deal. Jam tiga, gerbang sekolah. Telat semenit, kutinggal." id b16_023a
            kai "Nggak bakal telat." id b16_024a
            yara "Kita lihat. {i}(melangkah pergi, lalu setengah berteriak tanpa menoleh){/i} Dan jangan bawa kaset besokmu itu. Besok nggak butuh bocoran." id b16_025a
            hide yara with dissolve
            kai_hati "…Dia tahu soal kaset? {i}(tertawa kecil sendirian){/i} Ya sudahlah. Besok aku ikut. Besok, untuk sekali ini, aku nggak mau tahu isinya dulu." id b16_026a

        "\"Kalau sempat, aku ikut.\"":
            $ record_major_choice(4, "B")
            show kai cemas at pos_left
            kai "Kalau sempat… aku ikut. Nggak janji tiap hari, sih. Ada hari-hari aku harus— {i}(berhenti sendiri){/i} …ya, pokoknya kalau sempat." id b16_022b
            show yara biasa at pos_right
            yara "{i}(mengangguk sekali, datar){/i} Oke. Kalau sempat." id b16_023b
            hide yara with dissolve
            "Dia tidak mengajak dua kali. Kai menatap punggungnya menjauh, dan kata \"kalau sempat\" itu terasa menggantung di udara kantin — seperti kalimat yang tidak selesai." id b16_024b
            show kai sedih at pos_left
            kai_hati "Kenapa mulutku selalu pasang rem duluan, sih." id b16_025b

        "\"Itu duniamu. Aku dengerin aja hasilnya.\"":
            $ record_major_choice(4, "C")
            show kai sedih at pos_left
            kai "Kedengarannya seru… tapi itu duniamu, Yar. Aku nggak ngerti apa-apa soal begituan. {i}(tersenyum kaku){/i} Nanti saja aku dengar hasil jadinya, ya." id b16_022c
            show yara biasa at pos_right
            yara "{i}(jeda sebentar, lalu mengangkat bahu){/i} Ya sudah. Hasil jadinya. {i}(pergi){/i}" id b16_023c
            hide yara with dissolve
            "Yara berjalan pergi sendirian, tas kanvas berat di pundaknya, boom mic teracung seperti biasa. Kantin kembali jadi sekadar bising di telinga Kai." id b16_024c
            kai_hati "…Aneh. Aku barusan nolak hal yang sebenarnya pengin banget kuikuti. Dan aku bahkan nggak tahu kenapa." id b16_025c

    ## Adegan 16-3 — Penutup: dinamika baru [nada mengikuti G4]
    show kai biasa at pos_center with dissolve
    if get_major_choice(4) == "A":
        "Sejak siang itu, sepulang sekolah Kai punya tujuan baru. Bukan kamar, bukan gang basah itu — melainkan ke mana pun Yara dan mikrofonnya pergi. Dia membawa tas kanvas berat berisi tripod dan kabel ke kolong jembatan, ke pasar tradisional yang riuh, ke taman kota waktu senja." id b16_027a
        "Yara berjalan di depan, boom mic teracung seperti pemburu melacak hewan langka. Kai di belakangnya, membawa barang — dan tertawa lebih sering dari yang dia ingat pernah dia lakukan." id b16_027a_p2
    elif get_major_choice(4) == "B":
        "Sejak siang itu, ada hari-hari Kai ikut — membawa tas kanvas Yara ke pasar, ke taman kota — dan ada hari-hari dia tidak muncul, tanpa kabar. Yara tidak pernah bertanya kenapa." id b16_027b
        "Dia hanya selalu mulai lima menit lebih lambat pada hari-hari Kai datang, seolah menyisakan ruang. Dan pada hari-hari Kai tidak datang, dia merekam sendirian, seperti biasa. Seperti sebelum ada Kai." id b16_027b_p2
    else:
        "Sejak siang itu, tidak banyak yang berubah — di permukaan. Yara tetap berburu suara sendirian, dan sesekali, di kantin atau perpustakaan, dia memutarkan hasil jadinya untuk Kai lewat satu sisi headphone." id b16_027c
        "Kai mendengarkan, memuji dengan tulus… lalu pulang, memutar kaset besoknya, dan bertanya-tanya kenapa pujian itu tadi terasa seperti menonton hidup orang lain dari balik kaca." id b16_027c_p2

    kai_hati "Dunia ternyata bisa melambat. Nggak selalu — tapi bisa. {i}(jeda){/i} Dan lucunya, aku baru sadar: akhir-akhir ini aku ke toko Pak Ageng bukan karena panik. Kadang cuma karena… pengin cerita hari ini." id b16_028

    stop music fadeout 1.2
    return
