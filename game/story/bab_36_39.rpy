## Interlude / Side B — Batch 9 (Bab 36–39)
## Sumber verbatim: NASKAH-VN-MASTER-Interlude-Side-B.md (baris 2977–3311)
## Gerbang: callback m19 (Bab 36), G10 final Rute Merah (Bab 36 — A versi lengkap bila G6=A atau G8=B; ach_jujur),
##          G11 (Bab 38 + callback G8=B di surat), m20 (Bab 39 — opsi panci hanya bila item_file_panci)

################################################################################
## BAB 36 — Dua Versi Rute (Kejujuran yang Terlambat / Kejujuran yang Tepat Waktu)
################################################################################

label bab_36_m19_callback:
    ## Callback m19 dari Bab 35 (dibayar di awal Bab 36 pada semua rute bila m19=A/B)
    if get_minor_choice("m19") == "A":
        ageng "{i}(melihat foto di HP Kai){/i} Gang ini… kering. Sudah lama sekali saya nggak lihat dia kering." id b36_m19_a1
        kai "Iya, Pak. Rasanya aneh. Kayak bukan gang yang sama." id b36_m19_a2
        ageng "Gangnya sama, Nak. Yang berubah itu yang lewat." id b36_m19_a3
    elif get_minor_choice("m19") == "B":
        ageng "{i}(mendengarkan rekaman langkah dari HP Kai){/i} Langkahmu. Nggak ada genangan. {i}(tersenyum tipis){/i} Suara orang yang nggak lagi sembunyi dari hujan, itu." id b36_m19_b1
        kai "…Saya nggak sembunyi, Pak. Cuma— ya. Mungkin iya." id b36_m19_b2
    return


label bab_36_merah:
    $ chapter_autosave("bab_36_merah", "Bab 36 — Kejujuran yang Terlambat", "Ch. 36 — Honesty Too Late")

    ## Adegan 36R-1 — Toko Gema Masa, sore (membayar m19)
    scene bg_gang_kering with dissolve
    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    play music bgm_toko loop fadein 1.5
    show kai sedih at pos_left with dissolve
    show ageng biasa at pos_right with dissolve

    if get_minor_choice("m19") in ("A", "B"):
        call bab_36_m19_callback
    else:
        "Tidak ada komentar apa-apa sore itu. Kai langsung masuk, duduk, dan diam — seperti biasa akhir-akhir ini." id b36r_001c

    "Pak Ageng tidak bertanya kenapa Kai datang. Ia hanya menyeduh teh, lalu duduk. Belakangan ini Kai lebih sering diam daripada bicara, dan Pak Ageng membiarkannya." id b36r_002

    ## Adegan 36R-2 — Rumah Kai, malam. Ketukan yang tidak sabar
    stop music fadeout 1.0
    scene bg_kamar_kai_malam with fade
    play music bgm_cemas loop fadein 1.5
    show kai panik at pos_left with vpunch
    show yara menangis at pos_right with dissolve

    "Malam itu, ketukan di pintu rumah Kai terdengar tidak sabar. Begitu pintu dibuka — Yara. Tanpa alat rekam. Tanpa headphone di leher. Cuma jaket denim tipis, mata sembap, hidung merah." id b36r_003

    yara "Cukup, Kai." id b36r_004

    "Dia melangkah masuk tanpa menunggu dipersilakan. Kai mundur selangkah." id b36r_005

    yara "Aku butuh jawaban. Sekarang. {i}(suaranya bergetar){/i} Apa salahku? Bilang. Apa salahku sampai kamu tiba-tiba buang aku kayak… kayak semua waktu kemarin itu nggak ada artinya?" id b36r_006

    kai_hati "Dia nangis. Dia beneran nangis, di depan aku, sekarang. Bukan di kaset. Bukan tanggal satu Agustus. Sekarang — gara-gara aku." id b36r_007

    show kai sedih at pos_left
    kai "Kamu nggak salah apa-apa, Yara." id b36r_008

    show yara marah at pos_right with vpunch
    yara "Terus kenapa?! {i}(setengah berteriak, air matanya tumpah){/i} Kenapa kamu natap aku kayak nggak pernah kenal? Kenapa kamu nggak mau dengar suara bareng aku lagi? Kamu bikin aku ngerasa kayak orang gila, Kai. Jalan sendirian. Berminggu-minggu." id b36r_009

    "Tangan Kai mengepal rapat-rapat. Di kepalanya, semua alasan dingin itu — \"ini buat melindungi dia\" — runtuh satu-satu." id b36r_010

    ## GERBANG UTAMA G10 — RUTE MERAH (final, posisi 10 string 12 huruf; A memicu ach_jujur)
    menu:
        "Apa yang Kai lakukan?"

        "\"Yar. Ada yang harus kamu tahu. Semuanya.\"":
            $ record_major_choice(10, "A")

            ## Cabang G10-A — Pengakuan penuh (runtut bila G6=A atau G8=B; tersendat bila tidak)
            if flag_g6_cermin or get_major_choice(8) == "B":
                ## Versi runtut (modal dialog G6=A atau G8=B terpenuhi)
                show kai menangis at pos_left
                kai "Karena aku takut, Yara. {i}(menarik napas dalam){/i} Duduk dulu. Aku cerita semuanya. Semua kegilaan yang selama ini aku sembunyiin dari kamu. Jangan potong dulu, ya. Soalnya kalau berhenti di tengah, aku nggak yakin bisa lanjut." id b36r_011a1

                "Di ruang tamu yang sunyi, Kai membuka semuanya. Suaranya bergetar, tapi tidak berhenti." id b36r_012a1

                kai "Kamu ingat toko kaset di gang buntu itu? Gema Masa. Kaset di sana… bisa muter suara dari masa depan. Enam puluh detik. Awalnya cuma besok. Aku ketagihan, Yar. Aku takut setengah mati sama besok, jadi aku dengerin terus." id b36r_013a1

                kai "Dulu, sebelum kita kenalan, aku pernah dengar satu kaset isinya hening. Satu menit penuh, nggak ada suara apa-apa. Aku kira itu artinya aku mati hari Jumat itu. {i}(tertawa pendek, pahit){/i} Ternyata bukan. Hening itu… momen aku lihat kamu di perpustakaan. Aku nggak mati, Yara. Aku justru ngerasa hidup, gara-gara kamu." id b36r_014a1

                show yara sedih at pos_right
                yara "{i}(diam, mata membelalak, mendengarkan){/i}" id b36r_015a1

                kai "Terus aku tahu kamu bakal pergi kuliah enam bulan lagi. Dan aku jadi pengecut lagi. Aku beli kaset tanggal satu Agustus. Aku mau tahu… kamu masih ada apa nggak di masa depan aku." id b36r_016a1

                kai "{i}(menunduk; air matanya jatuh ke pangkuan){/i} Harganya ingatan paling bahagia yang aku punya. Dan aku bayar, Yara. Aku tukar ingatan pertemuan pertama kita di perpustakaan. Makanya aku natap kamu kayak orang asing. Logikaku tahu kamu Yara. Tapi dada aku kosong. Rasanya… hilang." id b36r_017a1

                kai "Isi kaset satu Agustus itu cuma suara kamu nangis. Ngucapin selamat tinggal. Jadi otak bodohku mikir: kalau dari sekarang aku jauhin kamu, kalau kita nggak terlalu dekat, perpisahan itu nggak akan sesakit ini. Buat kamu. Buat aku. Aku kira aku lagi ngelindungin kamu. Ternyata aku cuma… matiin rasaku sendiri." id b36r_018a1

            else:
                ## Versi tersendat (G6!=A dan G8!=B; skor G10=A tetap sama)
                show kai menangis at pos_left
                kai "Karena aku takut, Yara. {i}(jeda lama){/i} Aku… denger. Duduk. Duduk dulu. Aku cerita, tapi— pelan-pelan, ya. Aku nggak tahu mulai dari mana." id b36r_011a2

                show yara sedih at pos_right
                yara "Dari mana aja, Kai. Mulai aja." id b36r_012a2

                kai "Toko itu. Gema Masa. Kasetnya… {i}(berhenti; mengusap wajah){/i} Kamu nggak bakal percaya." id b36r_013a2

                yara "Coba dulu." id b36r_014a2

                kai "Kaset di sana bisa muter suara masa depan. Enam puluh detik. Aku… aku sering beli. Buat besok-besok. Terus ada kaset buat tanggal satu Agustus, dan aku— {i}(suara pecah){/i} aku bayar pakai ingatan aku tentang pertemuan pertama kita. Di perpustakaan. Ingatannya hilang, Yar. Beneran hilang. Makanya aku—" id b36r_015a2

                yara "{i}(pelan){/i} …Makanya kamu natap aku kayak orang asing." id b36r_016a2

                kai "Iya. Iya. Dan isi kasetnya suara kamu nangis, bilang selamat tinggal. Jadi aku mikir, kalau aku jauh dari sekarang, nanti nggak sesakit— {i}(berhenti; menggeleng){/i} Bodoh. Aku tahu itu bodoh. Aku tahu." id b36r_017a2

                "Tersendat, terpotong-potong, berkali-kali harus mulai lagi dari tengah — tapi malam itu, untuk pertama kalinya, Kai tidak berhenti sampai semuanya keluar." id b36r_018a2

        "\"Maafin aku. Udah, itu aja.\"":
            $ record_major_choice(10, "B")

            ## Cabang G10-B (melewati Bab 37, langsung lanjut ke Bab 38)
            show kai sedih at pos_left
            kai "{i}(menunduk lama){/i} …Maafin aku, Yara." id b36r_011b

            show yara sedih at pos_right
            yara "{i}(menunggu){/i}" id b36r_012b

            kai "Udah. Itu aja." id b36r_013b

            yara "Maaf untuk apa, Kai?" id b36r_014b

            "Kai membuka mulut. Menutupnya lagi. Kata-kata itu ada — toko, kaset, satu Agustus — tapi semuanya berhenti di tenggorokan, seperti biasa." id b36r_015b

            kai "Pokoknya… maafin aku." id b36r_016b

            yara "{i}(mengangguk pelan, sekali){/i} Oke." id b36r_017b

            hide yara with dissolve
            "Dia tidak mengejar. Tidak bertanya lagi. Dia berbalik, membuka pintu sendiri, dan pergi — meninggalkan Kai dengan permintaan maaf yang tidak pernah menjelaskan apa-apa." id b36r_018b

        "Diam dan pergi.":
            $ record_major_choice(10, "C")

            ## Cabang G10-C (melewati Bab 37, langsung lanjut ke Bab 38)
            show kai datar at pos_left
            kai "{i}(menggeleng pelan; mundur selangkah; tidak mengatakan apa-apa){/i}" id b36r_011c

            show yara sedih at pos_right
            yara "{i}(menatapnya lama){/i} …Oke. Oke, Kai." id b36r_012c

            hide yara with dissolve
            "Yara mengangguk seperti orang yang baru saja mendengar jawaban — karena diam juga jawaban. Dia pergi. Pintu tertutup pelan, jauh lebih menyakitkan daripada kalau dibanting." id b36r_013c

    stop music fadeout 1.0
    return


label bab_36_sehat:
    $ chapter_autosave("bab_36_sehat", "Bab 36 — Kejujuran yang Tepat Waktu", "Ch. 36 — Honesty Right on Time")

    ## Adegan 36S-1 — Toko Gema Masa, sore [RUTE SEHAT & TUNDA]
    scene bg_toko_dalam with dissolve
    play sound sfx_lonceng_pintu
    play music bgm_toko loop fadein 1.5
    play sound sfx_derit_kursi_goyang loop fadein 0.8
    show kai biasa at pos_left with dissolve
    show ageng biasa at pos_right with dissolve

    ## Callback m19 bila pemain memotret / merekam gang kering di Bab 35
    if get_minor_choice("m19") in ("A", "B"):
        call bab_36_m19_callback

    stop sound fadeout 0.6
    hide ageng with dissolve
    show yara ceria at pos_right with dissolve
    "Yara datang ke toko sore itu dengan langkah cepat dan mata berbinar — surat penerimaan universitas di Yogyakarta baru saja sampai. Tapi begitu melihat Kai, langkahnya melambat." id b36s_001

    show yara penasaran at pos_right
    yara "Kai. Kamu kok… dari tadi aku cerita, kamu cuma \"hm\" \"oh\" \"iya\". {i}(duduk di sebelahnya){/i} Hei. Kamu kenapa?" id b36s_002

    kai_hati "Bilang. Sekarang. Mumpung belum jadi apa-apa. Mumpung masih bisa dibilang sambil ketawa-tawa kecil, bukan sambil nangis." id b36s_003

    show kai cemas at pos_left
    kai "Yar. Ada yang mau aku bilang. Ini agak… memalukan, sebenarnya." id b36s_004

    yara "{i}(memiringkan kepala){/i} Kamu ngutang siapa?" id b36s_005

    kai "Bukan. {i}(tertawa pendek, gugup){/i} Dengerin dulu. {i}(jeda){/i} Aku seneng kamu keterima. Serius, seneng banget. Kamu kerja buat portofolio itu berbulan-bulan, aku lihat sendiri. Cuma… ada bagian dari aku yang— {i}(berhenti){/i}" id b36s_006

    show yara biasa at pos_right
    yara "Yang takut." id b36s_007

    kai "{i}(terdiam){/i} …Iya. Yang takut. Satu Agustus itu kedengerannya masih lama, tapi nggak, Yar. Cepet. Dan aku nggak tahu kita bakal kayak apa. Aku nggak tahu aku bakal kayak apa." id b36s_008

    show yara sedih at pos_right
    yara "{i}(pelan){/i} Kamu kira aku nggak takut?" id b36s_009

    kai "Kamu kelihatan… berani terus." id b36s_010

    show yara ceria at pos_right
    yara "Kelihatannya. {i}(tersenyum kecil){/i} Kai, aku juga nggak tahu kita bakal kayak apa. Nggak ada yang tahu. Kamu mau aku janji yang aneh-aneh? Nggak bisa. Yang bisa aku janji cuma satu: aku nggak bakal hilang tanpa bilang-bilang. Kalau aku pergi, kamu tahu kapan, naik apa, jam berapa. Kamu boleh nganter. Boleh nangis juga, nggak aku larang." id b36s_011

    show kai senyum at pos_left
    kai "{i}(tertawa, kali ini beneran){/i} …Deal yang buruk buat aku." id b36s_012

    yara "Deal yang jujur. {i}(berdiri, menepuk bahu Kai sekali){/i} Udah. Jangan diem-diem an lagi. Kalau kepikiran yang aneh-aneh, bilang. Aku lebih bisa jawab pertanyaan beneran daripada nebak-nebak isi kepala kamu." id b36s_013

    show ageng senyum at pos_center with dissolve
    ageng "{i}(dari balik konter, tanpa mengangkat kepala dari kaset yang sedang ia bersihkan){/i} Anak-anak sekarang itu… masalahnya bukan nggak punya jawaban. Kebanyakan nggak berani nanya." id b36s_014

    show kai cemas at pos_left
    kai "Pak Ageng dari tadi dengerin?!" id b36s_015

    ageng "Toko saya kecil, Nak. {i}(tersenyum){/i} Wes, sana. Antar dia pulang. Keburu hujan — gang ini kalau sudah mendung nggak pakai lama." id b36s_016

    ## Adegan 36S-2 — Gang buntu, perjalanan pulang
    hide ageng with dissolve
    play sound sfx_lonceng_pintu
    scene bg_gang_hujan with dissolve
    play music bgm_senja loop fadein 1.5
    show kai biasa at pos_left with dissolve
    show yara biasa at pos_right with dissolve

    "Di mulut gang, Yara berhenti sebentar. Menatap papan kayu miring bertuliskan \"Gema Masa\"." id b36s_017

    yara "Kai. Satu lagi, mumpung aku ingat. {i}(jeda){/i} Waktu itu kamu pernah cerita ada kaset yang bisa dengar setahun ke depan. Yang harganya… ingatan." id b36s_018

    kai "{i}(terdiam){/i} …Iya." id b36s_019

    show yara penasaran at pos_right
    yara "Kamu sempat kepikiran beli?" id b36s_020

    show kai senyum at pos_left
    kai "{i}(lama baru menjawab){/i} Sempat. Banget, malah. Tanganku sudah di dompet. {i}(tertawa pendek){/i} Terus aku ingat muka kamu waktu pertama kali nunjukin suara panci itu. Dan aku mikir… kalau ingatan yang harus aku bayar itu ternyata yang itu, aku nggak mau. Aku nggak mau dengar masa depan dari mulut kaset. Aku mau dengar dari kamu, pas waktunya." id b36s_021

    show yara ceria at pos_right
    yara "{i}(menatapnya, lalu tersenyum){/i} …Itu kalimat paling bener yang pernah keluar dari mulut kamu, Kai." id b36s_022

    kai "Sekali-sekali." id b36s_023

    yara "Sekali-sekali nggak cukup. Latihan terus. {i}(berjalan lagi){/i} Ayo. Keburu hujan beneran. Kalau kehujanan, kamu yang gendong tasku." id b36s_024

    kai "Kenapa jadi aku—" id b36s_025

    yara "Karena kamu yang ngajak mampir toko. Ayo, rek." id b36s_026

    "Dan sore itu, untuk sekali ini, Kai pulang dengan dada yang lebih ringan daripada saat dia datang — bukan karena dia tahu masa depan, tapi karena dia berhenti mencoba mengetahuinya sendirian." id b36s_027

    stop music fadeout 1.2
    return


################################################################################
## BAB 37 — Logam yang Tak Punya Jiwa [KHUSUS RUTE MERAH + G10=A]
################################################################################

label bab_37:
    $ chapter_autosave("bab_37", "Bab 37 — Logam yang Tak Punya Jiwa", "Ch. 37 — Soulless Metal")

    ## Adegan 37-1 — Ruang tamu Kai, lanjutan malam itu
    scene bg_kamar_kai_malam with dissolve
    play music bgm_cemas loop fadein 1.2
    show kai menangis at pos_left with dissolve
    show yara marah at pos_right with dissolve

    "Yara bangkit dari duduknya. Napasnya memburu. Amarah yang tadi tertahan oleh air mata sekarang mendidih — karena sekarang dia tahu semuanya." id b37_001

    yara "Kamu… {i}(menunjuk dada Kai, jarinya bergetar){/i} Kamu beneran bodoh, Kai!" id b37_002

    kai "{i}(mendongak, tertegun){/i}" id b37_003

    yara "Kamu lebih percaya gulungan pita magnetik mati itu daripada ngomong langsung sama aku?! {i}(suaranya melengking){/i} Kita berminggu-minggu jalan bareng keliling kota! Makan rawon basah-basahan di pinggir rel!" id b37_004
    yara "Kedinginan di puncak bukit! Aku bagi suara dunia lewat headphone-ku sendiri, buat kamu! Terus habis semua itu, kamu milih bisik-bisik sama kaset di toko usang, cuma buat ngintip masa depan?" id b37_004_p2

    kai "Aku cuma takut kehilanganmu, Yara… {i}(suaranya kecil, parau){/i}" id b37_005

    show yara menangis at pos_right with vpunch
    yara "Takut kehilangan?! {i}(memotong, air mata kemarahan mengalir){/i} Kalau takut kehilangan, genggam hari ini lebih erat! Bukan buang masa lalu kita buat ramalan satu menit yang belum tentu kejadian!" id b37_006

    "Yara melangkah maju, memaksa Kai menatap matanya yang basah." id b37_007

    yara "Kamu bilang kaset itu muter suara aku nangis, bilang selamat tinggal, tanggal satu Agustus? {i}(tertawa pendek, pahit){/i} Ya tentu saja aku nangis, Kai! Siapa yang nggak nangis kalau orang yang dia cintai tiba-tiba berubah sedingin batu? Jauhin dia kayak pembawa wabah? Natap dia kayak orang asing?!" id b37_008

    kai_hati "…Oh. Oh, tidak. Tangisnya… bukan takdir. Tangisnya gara-gara aku. Kaset itu nggak ngerekam masa depan yang nggak bisa dihindari. Kaset itu ngerekam akibatnya. Akibat aku." id b37_009

    show yara sedih at pos_right
    yara "{i}(suaranya melemah, kecewa yang dalam){/i} Kamu rusak masa kini kita cuma buat siap-siap patah hati di masa depan. Kamu korbanin ingatan pertama kita — detik aku pertama kali lihat kamu di perpustakaan — buat sepotong plastik merah." id b37_010

    yara "Aku keterima di universitas impianku, Kai. Aku lari ke sini karena mau ngerayain sama kamu. Karena mau kita cari jalan keluar bareng, buat enam bulan ke depan. Tapi kamu… kamu malah lari sembunyi di balik ramalan konyolmu." id b37_011

    "Yara menyeka air matanya dengan kasar. Berbalik ke pintu." id b37_012

    yara "Pita magnetik itu nggak punya jiwa, Kai. Dia nggak bisa ngerasain dinginnya hujan. Nggak bisa ngerasain hangatnya rawon. Kalau kamu lebih milih hidup sama ramalan mati itu — silakan. Tapi jangan harap aku terus berdiri di sini, nunggu orang yang bahkan nggak ingat gimana cara kita pertama kali ketemu." id b37_013

    hide yara with vpunch
    "Kai sendirian di ruang tamu yang mendadak sunyi senyap. Di tangannya, cangkang kaset merah terasa makin dingin — seperti seluruh sisa kehidupan di dalamnya sudah menguap habis." id b37_014

    stop music fadeout 1.2
    return


################################################################################
## BAB 38 — Surat dari Sisa Waktu (SEMUA RUTE MENYATU) ◆ G11
################################################################################

label bab_38:
    $ chapter_autosave("bab_38", "Bab 38 — Surat dari Sisa Waktu", "Ch. 38 — A Letter from Remaining Time")

    ## Adegan 38-1 — Sekolah, berminggu-minggu sesudahnya
    scene bg_koridor_sekolah with dissolve
    play music bgm_cemas loop fadein 1.5
    play sound sfx_kelas loop fadein 0.6
    show kai sedih at pos_center with dissolve

    "Minggu demi minggu lewat tanpa satu kata pun bertukar. Di sekolah, Yara sekarang tidak terjangkau: headphone hitam besar terpasang rapat dari turun angkot sampai bel pulang — benteng yang tidak boleh ditembus siapa pun. Terutama Kai." id b38_001

    kai_hati "Dulu aku yang sembunyi di balik sunyi. Sekarang gantian. Rasanya… pantas, sih." id b38_002

    "Kalender di kamar Kai berganti lembaran. Sisa satu bulan menuju satu Agustus." id b38_003

    ## Adegan 38-2 — Toko Gema Masa, sore
    stop sound fadeout 0.5
    scene bg_toko_dalam with dissolve
    stop music fadeout 0.8
    play music bgm_toko loop fadein 1.5
    show kai sedih at pos_left with dissolve
    show ageng sakit at pos_right with dissolve

    "Pak Ageng sudah bisa bangkit dari ranjangnya. Tubuhnya jauh lebih kurus sekarang, dan jalannya dibantu tongkat kayu jati yang berderit tiap menyentuh lantai. Di depan Kai, sebungkus onde-onde dari pasar sudah dingin — kulit wijennya mengeras." id b38_004

    ageng "Makanlah selagi hangat — harusnya begitu. {i}(menatap Kai pelan){/i} Tapi kamu bahkan biarin makananmu dingin. Kayak kamu biarin hari-harimu membeku, Kai." id b38_005

    $ show_item("item_onde_onde")
    "Kai tidak menjawab. Dia mengunyah onde-onde dingin itu lambat-lambat, tanpa benar-benar merasakan manis kacang hijaunya." id b38_006

    $ hide_item()
    ## Adegan 38-3 — Amplop putih
    stop music fadeout 1.0
    scene bg_kamar_kai with dissolve
    show kai cemas at pos_center with dissolve

    $ show_item("item_surat_yara")
    "Keesokan harinya, ada ketukan pelan — bukan orang, tapi kotak pos di pagar. Di dalamnya: amplop putih tanpa perangko. Di depan, nama Kai ditulis pena hitam. Tulisan tangan Yara. Tegas, rapi." id b38_007

    kai_hati "Tanganku gemetar. Amplop doang, padahal. Amplop doang." id b38_008

    ## Adegan 38-4 — Isi surat Yara (tampil langsung di atas CG surat terbuka tanpa kotak dialog)
    play music bgm_senja loop fadein 1.5
    python:
        _yara_letter_paras = [
            _("Kai, aku nggak tahu apakah kamu masih mendengarkan suara di sekitarmu, atau kamu sudah sepenuhnya milih sunyi."),
            _("Aku berangkat ke Yogyakarta tanggal 1 Agustus sore, naik kereta. Portofolioku sudah selesai sepenuhnya, dan pihak universitas minta aku datang lebih awal buat urusan administrasi."),
        ]
        if get_major_choice(8) == "B":
            _yara_letter_paras.append(
                _("Aku masih ingat kalimat yang tidak kamu selesaikan waktu itu, di bawah hujan. Aku nunggu kamu menyelesaikannya sampai sekarang. Mungkin di stasiun. Mungkin nggak pernah.")
            )
        _yara_letter_paras.append(
            _("Sebelum aku pergi, aku ingin ketemu kamu sekali lagi. Di stasiun, atau di mana pun kamu mau. Aku ingin kita bicara sebagai manusia. Bukan sebagai dua orang asing yang saling menghindar.")
        )
        _yara_letter_paras.append(_("Aku tunggu balasan surat ini. — Yara"))

    call show_letter(
        cg_id="cg_surat_yara",
        letter_title=_("Surat dari Yara"),
        paragraphs=_yara_letter_paras,
        paper_bg="#f7f2e8e0",
    )

    scene bg_kamar_kai with dissolve
    show kai sedih at pos_center with dissolve
    kai_hati "Satu Agustus. Sore. Kereta. Nyata. Semuanya nyata. {i}(jeda lama){/i} Kalau aku balas… kalau aku datang ke stasiun itu… aku bakal dengar dia nangis. Aku bakal dengar \"selamat tinggal\" itu, beneran, pakai telingaku sendiri." id b38_014
    kai_hati "{i}(lebih pelan){/i} Jangan balas. Kalau aku nggak datang, mungkin dia nggak nangis buat aku. Mungkin dia pergi tenang-tenang aja, tanpa harus lihat muka pengecut ini lagi." id b38_014_p2

    ## GERBANG UTAMA G11 (posisi 11 string 12 huruf)
    menu:
        "Surat ini dibalas, atau tidak?"

        "Balas malam ini.":
            $ record_major_choice(11, "A")

            ## Cabang G11-A — Balas malam ini
            scene bg_kamar_kai_malam with dissolve
            show kai biasa at pos_center with dissolve

            "Kai duduk di meja belajar. Kertas kosong. Pena di tangan." id b38_015a

            kai_hati "Draf satu: \"Yara, maaf.\" {i}(mencoret){/i} Terlalu pendek. Kayak nggak niat." id b38_016a

            "Kertas diremas, dibuang. Draf dua." id b38_017a

            kai_hati "\"Yara, selama ini aku—\" {i}(mencoret lagi){/i} Nggak. Kalau mulai dari aku terus, ini surat buat aku, bukan buat dia." id b38_018a

            "Draf tiga ditulis paling lama. Dibaca ulang dua kali. Tidak dicoret." id b38_019a

            show kai senyum at pos_center
            kai "{i}(membaca pelan){/i} \"Yara. Aku akan datang. Satu Agustus, sore, di stasiun. Ada kalimat yang harus aku selesaikan — dan kali ini aku selesaikan.\" {i}(melipat kertas, memasukkannya ke amplop){/i} …Kirim besok pagi. Sebelum aku berubah pikiran." id b38_020a

        "Balas tiga hari kemudian.":
            $ record_major_choice(11, "B")

            ## Cabang G11-B — Balas tiga hari kemudian
            "Tiga hari surat itu tergeletak di meja. Tiga hari Kai melewatinya, menatapnya, lalu melakukan hal lain. Di hari ketiga, malam-malam, dia akhirnya menulis balasan pendek — terlalu pendek untuk semua yang seharusnya dikatakan, tapi terkirim juga." id b38_015b

            "Balasannya datang seminggu kemudian. Amplop kecil. Satu lembar. Satu baris di tengah halaman, sisanya kosong." id b38_016b

            call show_letter(
                cg_id="cg_surat_balasan_yara",
                letter_title=_("Balasan dari Yara"),
                paragraphs=[
                    _("\"Kupikir kamu nggak akan balas.\""),
                ],
                centered_mode=True,
                paper_bg="#f7f4ede0",
            )

            scene bg_kamar_kai with dissolve
            show kai sedih at pos_center with dissolve
            kai_hati "Satu baris. Dan rasanya lebih keras dari semua teriakan dia malam itu." id b38_018b

        "Tidak balas.":
            $ record_major_choice(11, "C")

            ## Cabang G11-C — Tidak balas
            "Kai melipat surat itu dan memasukkannya ke laci meja — tepat di samping gulungan pita-pita kaset yang kusut. Tetangga yang cocok, pikirnya. Benda-benda yang tidak sanggup dia hadapi, disimpan berdekatan." id b38_015c

            "HP-nya dia matikan dan dia taruh di laci yang sama. Seminggu penuh benda itu tidak menyala. Di sekolah dia menunduk. Di rumah dia tidur lebih awal. Satu bulan menuju satu Agustus, Kai memutuskan tenggelam sepenuhnya dalam sunyi yang dia ciptakan sendiri — mengabaikan uluran tangan terakhir dari gadis yang sudah menghidupkan dunianya." id b38_016c

    stop music fadeout 1.2
    return


################################################################################
## BAB 39 — Spektrum Suara Tanpa Jiwa ◆ m20
################################################################################

label bab_39:
    $ chapter_autosave("bab_39", "Bab 39 — Spektrum Suara Tanpa Jiwa", "Ch. 39 — A Spectrum of Soulless Sound")

    ## Adegan 39-1 — Toko Gema Masa, tiga minggu kemudian
    scene bg_gang_kering with dissolve
    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    play music bgm_cemas loop fadein 1.5
    show kai sedih at pos_left with dissolve
    show ageng biasa at pos_right with dissolve

    "Tiga minggu sejak surat itu masuk laci. Tiga minggu Kai hidup seperti mayat hidup — menatap punggung Yara dari kejauhan di koridor, punggung yang makin tegak, makin jauh." id b39_001
    "Sore ini dia kembali ke gang buntu yang kering itu. Pak Ageng berdiri di balik konter, menatap tumpukan kaset kosong yang baru datang. Badannya sudah jauh lebih baik, meski wajah tuanya masih menyisakan lelah." id b39_001_p2

    "Kai merosot di kursi kayu di depan konter. Wajahnya dia sembunyikan di balik dua telapak tangan yang gemetar." id b39_002

    show kai menangis at pos_left
    kai "Aku ngerusak semuanya, Pak. {i}(suaranya pecah){/i} Enam bulan ini rasanya kayak neraka. Aku kangen dia. Tapi aku nggak bisa balas suratnya. Aku terlalu takut sama tanggal satu Agustus itu." id b39_003

    show ageng serius at pos_right with vpunch
    "Pak Ageng menghentikan kegiatannya. Dia meletakkan satu kaset ke meja — plak, cukup keras. Napas panjang. Lalu tatapan yang tidak lagi iba. Tegas. Menusuk." id b39_004

    ageng "Kamu bodoh, Nak." id b39_005

    kai "{i}(mendongak, mata berkaca-kaca){/i} …Pak?" id b39_006

    ageng "Kamu beneran bodoh. {i}(menunjuk kaset merah tanggal satu Agustus yang menyembul dari saku jaket Kai){/i} Kamu biarin sepotong plastik berlapis logam ngendaliin seluruh hidupmu. Kamu perlakukan mesin analog ini kayak dewa yang tahu semua isi hati manusia." id b39_007

    kai "Tapi kaset itu ngerekam suara Yara nangis, Pak! Dia ngucapin selamat tinggal ke aku! Itu bukti hubungan kami bakal berakhir hancur, kan?!" id b39_008

    ageng "Kaset merekam suara, Kai! Bukan perasaan! {i}(suaranya meninggi; debu di rak kaca seakan ikut bergetar){/i} Mesin ini cuma nangkep gelombang udara. Getaran pita suara. Desis statis. Dia nggak bisa nerjemahin apa yang sebenernya ada di dada manusia waktu suara itu diucapin!" id b39_009

    "Pak Ageng melangkah mendekat. Menatap Kai lurus-lurus." id b39_010

    ageng "Pikirin pakai otakmu yang masih utuh, Nak. Kalimat \"selamat tinggal\" yang diucapin sambil nangis itu banyak artinya. Bisa tangis perpisahan, karena kamu sudah buang dia jadi orang asing. Tapi bisa juga tangisan haru — orang yang harus pergi sementara buat impiannya, tapi tahu laki-laki yang dia cintai bakal setia nunggu dia pulang." id b39_011

    ageng "{i}(mengetuk konter jati, menekankan tiap kata){/i} Suara tangis yang sama bisa lahir dari benci, dari kecewa, atau justru dari cinta yang terlalu besar buat diucapin pakai kata biasa." id b39_012
    ageng "Kaset merahmu cuma kasih tahu dia nangis. Kamulah — lewat keputusan pengecutmu hari ini — yang lagi nentuin tangis itu bakal jadi tangis penyesalan, atau tangis rindu." id b39_012_p2

    show kai cemas at pos_left
    "Kai tertegun seperti baru dihantam godam. Selama ini dia cuma mendengar frekuensi — tidak pernah mencoba memahami jiwa di balik suara itu. Dia sudah menyerah kalah bahkan sebelum memahami arti melodi yang dia dengar." id b39_013

    ## Adegan 39-2 — Kilas balik sisipan ◆ m20 (beberapa minggu sebelumnya, sebelum jarak itu ada)
    stop music fadeout 1.0
    scene bg_kelas with fade
    play music bgm_senja loop fadein 1.5
    play sound sfx_desis_pita
    show kai biasa at pos_left with dissolve
    show yara ceria at pos_right with dissolve

    "Yara sedang menyusun mix terakhir portofolionya. Di layar dan di meja: file-file suara yang mereka kumpulkan berbulan-bulan. Satu tempat kosong tersisa di tengah mix — bagian yang akan diputar paling keras, sendirian." id b39_014

    yara "Satu lagi. Bagian tengahnya kosong. Harus ada satu suara yang berdiri sendiri di sini. {i}(menoleh){/i} Menurut kamu yang mana?" id b39_015

    ## GERBANG MINOR m20 (opsi A HANYA tampil bila item_file_panci dimiliki dari m10=A)
    menu:
        "Suara apa yang di-solo-kan di tengah mix Yara?"

        "Suara panci mendidih dari kantin." if item_file_panci:
            $ record_minor_choice("m20", "A")
            play sound sfx_panci
            yara "{i}(tertawa){/i} Panci ibu kantin? …Kamu tahu, justru itu yang paling jujur. Air yang nggak sabar mau jadi uap. {i}(mengklik){/i} Masuk. Dia yang solo." id b39_016a
            stop sound fadeout 0.6

        "Suara hujan di talang.":
            $ record_minor_choice("m20", "B")
            play sound sfx_hujan_deras
            yara "Hujan talang… {i}(mendengarkan sebentar){/i} Iya. Ini Malang banget. Nggak ada kota lain yang hujannya bunyi kayak gini. Masuk." id b39_016b
            stop sound fadeout 0.6

        "Desis pita kosong.":
            $ record_minor_choice("m20", "C")
            play sound sfx_desis_pita
            yara "Desis? {i}(terdiam; lalu tersenyum kecil){/i} …Berani juga. Sunyi yang bukan kosong. Oke. Aku suka. Masuk." id b39_016c

    "Suara itu tersimpan di tengah mix — dan akan terdengar paling jelas nanti, saat demo portofolio itu diputar." id b39_017

    stop music fadeout 1.5
    return
