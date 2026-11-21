label bab_17:
    $ chapter_autosave("bab_17", "Bab 17 — Ketukan Besi dan Aroma Kuah Hitam", "Ch. 17 — Iron Rhythms and Dark Broth")

    scene bg_warung_rawon with dissolve
    play music bgm_senja loop fadein 1.2
    play sound sfx_hujan_deras loop fadein 0.8

    "Sore itu perburuan suara membawa mereka ke perlintasan kereta tua yang membelah pemukiman padat. Gerimis yang menggantung sejak siang mulai berubah jadi hujan beneran." id b17_001

    if get_major_choice(4) == "A":

        show kai biasa at pos_left with dissolve
        show yara fokus at pos_right with dissolve

        "Kai berdiri di samping Yara, mendekap tas kamera tahan air, sementara perekam kedua ada di tangannya — tugas resminya sejak dia bilang \"mulai besok, aku ikut\"." id b17_002a

        yara "{i}(berbisik, mengatur perekamnya){/i} Jangan berisik dulu. Dengerin. Kereta yang lewat jalur ini mesinnya diesel tua. Ketukan rodanya di sambungan rel itu berat, nggak rata… Itu salah satu suara favoritku." id b17_003a

        kai "Kamu sampai hafal mesinnya?" id b17_004a

        show yara ceria at pos_right
        yara "Telinga kedua nggak boleh banyak tanya. {i}(tersenyum, menggeser perekam di tangan Kai){/i} Pegangnya miring dikit ke arah rel. Nah. Gitu." id b17_005a

        show kai senyum at pos_left
        kai_hati "Telinga kedua. Julukan baru. Kemarin-kemarin aku cuma \"Laki-laki Penunggu Mati\", sekarang naik pangkat dikit." id b17_006a

    elif get_major_choice(4) == "B":

        show yara fokus at pos_center with dissolve

        "Untuk yang satu ini, Yara tidak mengajak Kai. Dia merekam sendiri di pinggir rel — dan seperti biasa, dia tidak pernah mengajak dua kali." id b17_002b

        yara_hati "Diesel tua. Ketukannya berat, nggak rata. Sendirian pun tetap kedengaran bagus. {i}(jeda){/i} …Cuma biasanya ada yang megangin tas." id b17_003b

    else:

        show yara fokus at pos_center with dissolve

        "Yara merekam sendiri sore itu. Mikrofon mengarah ke rel yang mulai basah, dan dia menunggu dengan sabar seperti pemburu yang tahu mangsanya pasti lewat." id b17_002c

        yara_hati "Rekam dulu. Hasilnya biar dia dengar belakangan." id b17_003c

    play sound sfx_kereta_lewat
    "Klakson melengking membelah suara hujan. Tanah bergetar pelan. Lokomotif tua merah-biru yang kusam melintas lambat, menarik gerbong-gerbong barang yang berderit nyaring. Ketukan besi lawan besi itu pekat sekali: berbaur dengan deru diesel yang parau dan hujan yang menghantam atap seng warung." id b17_007

    if get_major_choice(4) == "A":
        show yara ceria at pos_right
        yara "{i}(menurunkan mikrofon, wajahnya puas){/i} Dapat. Bersih banget. {i}(menepuk bahu Kai){/i} Kerja bagus, Telinga Kedua." id b17_008a

        kai "Aku cuma megangin, Yar." id b17_009a

        yara "Megangin itu kerjaan paling susah. Salah miring dikit, suaranya bocor semua." id b17_010a

    elif get_major_choice(4) == "B":
        show yara biasa at pos_right with dissolve
        show kai cemas at pos_left with dissolve
        "Kereta menjauh, suaranya meredup di balik kabut hujan. Yara menurunkan mikrofonnya, puas. Baru setelah itu Kai muncul dari arah warung, separuh basah, membawa dua payung lipat." id b17_008b

        kai "…Telat, ya, aku?" id b17_009b

        show yara ceria at pos_right
        yara "Keretanya barusan lewat. {i}(mengangkat perekamnya){/i} Tapi suaranya dapat. Duduk aja — aku juga baru mau pesan makan." id b17_010b

    if get_major_choice(4) != "C":

        play sound sfx_hujan_deras loop fadein 0.6
        show kai biasa at pos_left
        show yara ceria at pos_right

        "Dari dalam warung, aroma gurih menggoda sejak tadi: kuah kental dimasak dengan kluwek dan rempah tajam. Perut Kai bunyi duluan sebelum dia sempat pesan." id b17_011

        yara "Nah, ini dia bagian terbaik dari berburu suara pas hujan." id b17_012

        show npc_pemilik_warung at pos_center with dissolve
        pemilik_warung "Rawonnya dua, Nduk? Sambalnya dipisah?" id b17_013

        menu:
            "Makan di mana?"

            "Makan rawon di warung rel.":
                $ record_minor_choice("m12", "A")
                yara "Di sini aja, Cak. Sekalian nunggu hujan reda." id b17_014a
                pemilik_warung "Siap. {i}(menambah sambal ke mangkuk mereka lebih banyak dari takaran biasa){/i} Saya tambahi sambalnya, hujan-hujan begini harus yang anget. Kereta terakhir lewat setengah sembilan, masih lama kalau mau nunggu di sini." id b17_015a
                $ show_item("item_rawon")
                "Dua mangkuk rawon mengepul di meja kayu, ditemani mendol tempe dan kerupuk udang. Kai menuang sedikit sambal, mengaduk kuah hitamnya pelan, membiarkan uapnya menghangatkan wajah." id b17_016a
                yara "{i}(menyuap){/i} Enak?" id b17_017a
                show kai senyum at pos_left
                kai "{i}(mengangguk, jujur){/i} Enak banget. Hangatnya sampai ke dada." id b17_018a
                yara "{i}(tersenyum tipis){/i} Suara hujan, ketukan kereta, sama semangkuk rawon panas. Komposisi paling sempurna yang bisa diciptain hari ini." id b17_019a
                "Mereka makan dalam diam di pinggir rel, ditemani rintik hujan di genangan sela-sela batu kerikil jalur kereta." id b17_020a

            "Bungkus, makan di toko.":
                $ record_minor_choice("m12", "B")
                kai "Dibungkus dua, Cak. Satu buat saya, satu buat… ada yang belum makan di toko." id b17_014b
                show yara penasaran at pos_right
                yara "{i}(mengangkat alis){/i} Kamu mau makan di toko Pak Ageng? Ya sudah. Aku di sini aja — masih ada satu kereta barang lagi yang mau kutunggu." id b17_015b
                stop sound fadeout 0.5
                play sound sfx_lonceng_pintu
                scene bg_toko_dalam with dissolve
                play music bgm_toko loop fadein 1.2
                show kai senyum at pos_left with dissolve
                show ageng senyum at pos_right with dissolve
                ageng "{i}(melihat bungkusan di tangan Kai){/i} Loh. Kamu bawa apa itu, Nak?" id b17_016b
                $ show_item("item_rawon")
                kai "Rawon, Pak. Yang di warung dekat rel itu. Masih anget. Makan bareng, Pak — kebanyakan kalau buat saya sendiri." id b17_017b
                ageng "{i}(tertawa kecil, mengambil mangkuk dari rak kecil){/i} Anak ini. Ke mana-mana ingat perut orang tua. Ya sudah, sini. Kita makan." id b17_018b
                "Rawon bungkus, dimakan di antara rak-rak kaset, ditemani bunyi hujan di luar gang. Rasanya tetap sama enaknya." id b17_019b

        kai_hati "Aneh ya. Duduk makan begini saja… aku nggak kepikiran sama sekali besok bakal kayak apa. Nggak butuh kaset buat tahu hari ini baik atau buruk. Hari ini memang baik. Titik." id b17_021

    else:

        scene bg_warung_rawon with fade
        show kai biasa at pos_left with dissolve
        show yara biasa at pos_right with dissolve

        "Kai tidak ikut merekam kereta itu. Dia hanya mendengar hasil jadinya — sore berikutnya, di warung yang sama, dari speaker kecil perekam Yara." id b17_022c

        play sound sfx_kereta_lewat
        kai "…Itu semua kemarin? Pas hujan?" id b17_023c

        yara "Iya. Sayang kamu nggak di sana. Aslinya lebih… {i}(mengangkat bahu){/i} ya, namanya juga rekaman. Yang asli cuma bisa didengar sekali, pas kejadiannya." id b17_024c

        show kai sedih at pos_left
        kai_hati "Suaranya bagus. Tapi ada jaraknya. Kayak dengar hidup orang lain dari balik pintu." id b17_025c

    stop sound fadeout 0.6
    return

label bab_18:
    $ chapter_autosave("bab_18", "Bab 18 — Pita Merah dan Rekaman Tanpa Ramalan", "Ch. 18 — Red Tape and Unforetold Recordings")

    scene bg_warung_rawon with dissolve
    play music bgm_senja loop fadein 1.2
    show kai biasa at pos_left with dissolve
    show yara biasa at pos_right with dissolve

    if get_major_choice(4) in ("A", "B"):
        "Hujan berubah jadi rintik yang malas. Di bawah tempias atap seng, Yara membersihkan embun dari badan perekamnya pakai kain mikrofiber, telaten sekali." id b18_001ab
    else:
        "Rekaman kereta selesai diputar. Yara mematikan perekamnya, lalu membersihkan embun yang menempel di badannya pakai kain mikrofiber, telaten sekali." id b18_001c

    "Kai memperhatikan tangan Yara — lalu tatapannya turun ke tas kanvas gadis itu yang sedikit terbuka. Di sela kabel dan baterai cadangan, ada sesuatu yang sangat dia kenal. Wadah plastik mika transparan, dengan aksen merah menyala di sepanjang sisinya." id b18_002

    show kai cemas at pos_left
    kai_hati "Itu… kotak kaset Type IV. Metal. Pita hitam pekat, partikel logam. Sama persis kayak yang di lemari kaca Pak Ageng. Yang harganya bukan uang." id b18_003

    $ show_item("item_kaset_merah")
    kai "Yar. {i}(menunjuk ragu pakai dagu){/i} Kotak kaset merah di tasmu itu… Kamu juga pelanggan toko Gema Masa?" id b18_004

    show yara ceria at pos_right
    "Yara mendongak. Dia menatap Kai, lalu tasnya sendiri. Bukannya kaget, dia malah tersenyum tipis — senyum yang penuh arti. Dia merogoh tasnya, mengeluarkan kaset merah berlabel kosong itu, memutar-mutarnya di sela jari." id b18_005

    yara "Jadi kamu juga sering ke sana? {i}(tertawa kecil){/i} Pantas. Hari pertama kita ketemu di perpustakaan, mukamu pucat kayak orang lagi nunggu malaikat maut jemput." id b18_006

    kai "{i}(menggaruk tengkuk, wajahnya merona){/i} A-aku panik waktu itu. Aku dengar rekaman keheningan satu menit buat hari Jumat. Aku kira… aku kira aku bakal mati." id b18_007

    yara "Dasar. Pak Ageng itu memang suka biarin orang tersesat sama asumsi mereka sendiri." id b18_008

    $ hide_item()

    kai "Tapi, Yar… kaset merah itu harganya bukan uang. Pak Ageng minta ingatan paling bahagia sebagai bayaran. Kamu beneran—" id b18_009

    show yara fokus at pos_right
    yara "{i}(menggenggam kaset merah itu erat){/i} Aku memang nyerahin salah satu kenanganku buat kaset ini, Kai. Tapi aku nggak pakai buat ngeramal masa depan." id b18_010

    kai "Terus buat apa?" id b18_011

    show yara biasa at pos_right
    yara "Buat ngerekam. {i}(menjelaskan sambil mengetuk kaset itu pelan){/i} Pak Ageng punya stok kaset kosong Type IV Metal kualitas paling bagus, yang belum pernah dia isi frekuensi masa depan. Aku beli karena pita metal itu dynamic range-nya paling luas, noise-nya paling rendah. Dia bisa nangkep suara dunia apa adanya. Jujur. Nggak pakai distorsi." id b18_012

    "Yara menyandarkan punggung ke tiang kayu warung, menatap rel yang berkilau basah." id b18_013

    yara "Orang-orang datang ke toko Pak Ageng karena takut sama besok. Mereka pengin jaminan. Pengin tahu duluan biar bisa siap-siap. {i}(jeda){/i} Tapi buatku, ngeramal masa depan itu cara paling cepat ngerusak indahnya hari ini. Kalau kamu udah tahu akhir ceritanya… buat apa jalanin prosesnya?" id b18_014

    show kai biasa at pos_left
    kai_hati "Kepalaku kayak ketabrak pelan-pelan. Selama ini aku lari ngejar bayangan besok biar ngerasa aman. Dia… dia berdiri di tempatnya. Merekam hari ini." id b18_015

    show yara fokus at pos_right
    yara "{i}(menatap Kai langsung){/i} Aku nukar kenanganku bukan buat ngintip besok, Kai. Biar aku punya media paling bagus buat nyimpan momen-momen yang lagi kejadian sekarang. Ngerekam masa kini itu jauh lebih penting daripada ngeramal masa depan yang belum tentu ada." id b18_016

    show yara ceria at pos_right
    "Yara membuka daftar rekaman di perekamnya, seperti teringat sesuatu." id b18_017

    yara "Oh iya. Dengerin ini bentar. Kamu masih ingat kamu pernah bilang suara yang paling kamu benci itu apa?" id b18_018

    if get_minor_choice("m11") == "A":
        play sound sfx_kelas
        yara "Bel masuk yang sama. Tapi kurekam dari lapangan, pas sore, pas sekolah udah sepi. Kedengarannya beda, kan? Nggak kayak perintah. Kayak… pengingat pulang." id b18_019a
        show kai senyum at pos_left
        kai "{i}(terdiam sebentar){/i} …Iya. Yang ini nggak bikin dada sesak." id b18_020a
        stop sound fadeout 0.6

    elif get_minor_choice("m11") == "B":
        play sound sfx_desis_pita
        yara "Itu anak kelas sebelah, bisik-bisik nyemangatin temannya sebelum presentasi. Bisikan itu nggak selalu soal ngomongin orang, Kai. Kadang cuma karena suaranya terlalu berharga buat diteriakin." id b18_019b
        show kai senyum at pos_left
        kai "{i}(tersenyum kecil, mau tidak mau){/i} …Kamu rekam semua hal kayak gitu?" id b18_020b

    else:
        play sound sfx_desis_pita
        yara "Ini diam. Kurekam di ruang kelas kosong habis jam terakhir. Dengerin baik-baik — diam itu sebenarnya nggak kosong. Dia cuma ngomongnya pelan." id b18_019c
        show kai biasa at pos_left
        kai "{i}(memasang headphone lebih rapat, lama){/i} …Ada suaranya. Kecil banget. Tapi ada." id b18_020c

    show yara biasa at pos_right
    yara "{i}(mengangguk){/i} Semua suara yang kamu benci itu cuma belum kamu dengar dari jarak yang bener." id b18_021

    if item_file_panci:
        "Kai menatap perekamnya sendiri — lebih tepatnya, HP-nya. Di dalamnya ada satu file yang dia rekam di kantin: suara panci mendidih, rekaman pertamanya." id b18_022

        kai_hati "File panci itu. Rekamannya kasar, banyak bocornya. Tapi itu pertama kalinya aku ngerekam sesuatu bukan karena takut… cuma karena suaranya bagus." id b18_023

        menu:
            "Apa yang Kai lakukan dengan file suara panci itu?"

            "Beri file itu ke Yara.":
                $ record_minor_choice("m13", "A")
                kai "Yar. Ini… file panci yang di kantin waktu itu. Rekamanku jelek sih. Tapi kalau kamu mau, ambil aja." id b18_024a
                play sound sfx_panci
                show yara ceria at pos_right
                yara "{i}(menerima, mendengarkan sekilas, lalu mengangguk mantap){/i} Noise-nya banyak. Tapi detaknya dapet. {i}(mengetik sesuatu di daftar portofolionya){/i} Masuk arsip. Ini rekaman pertamamu, Kai. Yang kayak gini nggak bisa diulang." id b18_025a
                stop sound fadeout 0.6

            "Simpan untuk diri sendiri.":
                $ record_minor_choice("m13", "B")
                kai_hati "Nggak. Yang ini buat aku dulu. Bukti kecil bahwa aku pernah ngerekam sesuatu cuma karena aku mau, bukan karena aku takut." id b18_024b
                show yara ceria at pos_right
                yara "{i}(melirik, tidak bertanya){/i} Nyimpan sesuatu, ya? {i}(tersenyum){/i} Bagus. Nggak semua rekaman harus dibagi." id b18_025b

            "Hapus, rekamannya jelek.":
                $ record_minor_choice("m13", "C")
                kai "{i}(menghapus file itu){/i} Udah. Jelek. Banyak bocornya." id b18_024c
                show yara biasa at pos_right
                yara "{i}(mengangkat bahu){/i} Sayang sih. Tapi itu file-mu. Yang ngerekam yang berhak mutusin." id b18_025c

    "Di bawah langit Malang yang berangsur gelap, di samping rel yang sunyi sehabis dilewati diesel tua, Kai memandangi kaset merah di tangan Yara — dan untuk pertama kalinya, benda itu tidak terlihat menakutkan." id b18_026

    stop music fadeout 1.2
    return

label bab_19:
    $ chapter_autosave("bab_19", "Bab 19 — Debu yang Mengendap di Atas Rak", "Ch. 19 — Dust Settling on the Shelves")

    scene bg_kamar_kai with dissolve
    show kai biasa at pos_center with dissolve

    "Ada perubahan kecil di kamar Kai yang baru dia sadari hari itu. Meja belajarnya tidak lagi penuh coretan kalender berlingkaran merah dan catatan skenario buruk buat besok." id b19_001
    "Sekarang di sudut meja ada daftar lokasi perburuan suara dari Yara, beberapa baterai AA cadangan, dan satu jepit rambut hitam yang tertinggal waktu mereka merapikan kabel rekaman tempo hari." id b19_001_p2

    "Laci mejanya — tempat dia dulu menyimpan kaset-kaset ramalan — mulai berdebu." id b19_002

    show kai senyum at pos_center
    kai_hati "Udah berapa lama ya aku nggak ke gang itu? Dua minggu? Tiga? {i}(tersenyum kecil){/i} Tiap bangun pagi, yang kepikiran bukan lagi \"hari ini bakal ada apa\". Tapi \"hari ini kami ngerekam apa\"." id b19_003

    "Gerimis tipis membasahi Malang sore itu. Kai mengambil jaketnya. Bukan karena cemas. Bukan karena butuh jaminan besok. Dia cuma… kangen toko itu." id b19_004

    play sound sfx_lonceng_pintu
    scene bg_toko_dalam with dissolve
    play music bgm_toko loop fadein 1.5
    play sound sfx_derit_kursi_goyang loop fadein 0.8
    show kai senyum at pos_left with dissolve
    show ageng senyum at pos_right with dissolve

    "Lonceng pintu berdenting lembut. Aroma teh hangat dan kertas tua menyambut seperti biasa. Pak Ageng duduk di balik konter, kacamata baca bertengger di ujung hidung, membersihkan pemutar kaset dengan cotton bud." id b19_005

    ageng "{i}(mendongak, tersenyum lebar sampai kerut di sudut matanya dalam){/i} Ah. Sang penjelajah waktu yang hilang. {i}(terkekeh){/i} Bapak kira kamu sudah pindah kota, Kai." id b19_006

    kai "{i}(tertawa kecil — kali ini tanpa canggung sama sekali){/i} Maaf, Pak. Saya… akhir-akhir ini agak sibuk." id b19_007

    ageng "{i}(menggeser cangkir teh melati hangat ke hadapan Kai){/i} Sibuk menjalani hari ini, hm? {i}(tatapannya turun sekilas ke kantong jaket Kai, tempat ujung kabel mikrofon menyembul){/i}" id b19_008

    kai "{i}(mengangguk, menyesap teh){/i} Iya, Pak. Rasanya aneh. Dulu, kalau nggak tahu besok ada apa, saya nggak bisa tidur. Sekarang… saya bahkan nggak ingat kapan terakhir kali saya khawatir soal besok." id b19_009

    show ageng biasa at pos_right
    ageng "Itu karena kamu sudah menemukan sauhmu, Nak. Orang yang terus lihat ke depan itu biasanya karena nggak punya tempat berpijak di masa kini. Begitu kamu nemu sesuatu — atau seseorang — yang bikin masa kinimu berharga, besok nggak lagi terasa kayak ancaman." id b19_010

    stop sound fadeout 0.6
    "Kai melirik rak di samping konter. Debu halus mengendap di atas barisan kotak kaset — toko ini ikut menua dengan tenang. Pak Ageng mengikuti arah pandangannya." id b19_011

    menu:
        "Apa yang Kai lakukan?"

        "Bantu Pak Ageng membersihkan rak.":
            $ record_minor_choice("m14", "A")
            kai "Pak, raknya saya bantu bersihkan ya. Debunya udah tebel ini." id b19_012a
            show ageng senyum at pos_right
            ageng "{i}(tertawa kecil){/i} Monggo. Kemocengnya di belakang konter." id b19_013a
            "Kai membersihkan rak baris demi baris. Di baris paling bawah, di belakang tumpukan kaset biasa, ada satu kaset tanpa label. Cangkangnya sudah menguning. Kai mengangkatnya pelan." id b19_014a
            show kai biasa at pos_left
            kai "Pak, ini kaset apa? Nggak ada labelnya." id b19_015a
            show ageng iba at pos_right
            ageng "{i}(terdiam sebentar; suaranya melembut){/i} Itu… hujan. Hujan tahun sembilan puluh empat. {i}(jeda){/i} Nanti. Nanti Bapak ceritakan." id b19_016a
            kai_hati "Sembilan puluh empat. Tangannya Pak Ageng barusan… gemetar dikit? Baru kali ini aku lihat." id b19_017a

        "Lihat-lihat saja.":
            $ record_minor_choice("m14", "B")
            "Kai menyusuri rak dengan matanya saja, membaca label-label tulisan tangan yang sebagian sudah pudar. Dia tidak menyentuh apa pun. Ada hal-hal di toko ini yang terasa bukan buat diutak-atik." id b19_012b
            show ageng biasa at pos_right
            ageng "Rak itu isinya tahun-tahun orang, Nak. Debunya juga bagian dari isinya." id b19_013b

        "Tawar kaset rusak di pojok rak.":
            $ record_minor_choice("m14", "C")
            kai "Pak, yang di pojok itu… kaset rusak, ya? Pitanya udah kusut separuh. Kalau nggak kepakai, boleh saya beli murah?" id b19_012c
            show ageng senyum at pos_right
            ageng "{i}(mengintip, lalu mengibaskan tangan){/i} Ambil saja. Gratis. Pita kusut itu sudah nggak bisa nyimpan apa-apa — cocok buat kamu sekarang. Kamu kan sudah nggak nyimpan-nyimpan ketakutan lagi." id b19_013c
            $ renpy.notify(ui_tr("notify_item_kaset_rusak"))

    show ageng biasa at pos_right
    ageng "{i}(menunjuk lemari kaca di sampingnya, tempat kaset-kaset ramalan Type I berjejer rapi){/i} Jadi… kurasa hari ini kamu nggak datang buat beli jaminan hari esok?" id b19_018

    "Kai menatap barisan kaset itu. Perasaannya asing — tapi lega." id b19_019

    show kai senyum at pos_left
    kai "{i}(menggeleng mantap){/i} Nggak, Pak. Saya rasa… saya sudah nggak butuh itu lagi." id b19_020

    show ageng senyum at pos_right
    ageng "{i}(mengangguk-angguk puas){/i} Hm. Bagus. Bagus sekali, Nak." id b19_021

    return

label bab_20:
    $ chapter_autosave("bab_20", "Bab 20 — Keserakahan yang Terputus", "Ch. 20 — Severed Greed")

    scene bg_toko_dalam with dissolve
    stop music fadeout 0.6
    play sound sfx_lonceng_pintu
    play music bgm_cemas loop fadein 1.2
    show kai cemas at pos_left with dissolve
    show kaya biasa at pos_center with vpunch
    show ageng serius at pos_right with dissolve

    "Ketenangan itu pecah. Pintu kayu terdorong kasar sampai loncengnya berdenting panik. Seorang pria paruh baya melangkah masuk: jas necis yang jelas mahal, parfum menyengat yang seketika mengusir wangi teh melati dan kertas tua dari ruangan." id b20_001
    "Napasnya memburu. Matanya merah — bukan kurang tidur, tapi ambisi yang tidak sabaran. Hanya saja suaranya, waktu dia bicara, justru pelan dan terkendali. Itu yang bikin merinding." id b20_001_p2

    show kaya senyum at pos_center
    kaya "Permisi. {i}(tersenyum tipis, tidak ramah){/i} Pemilik toko ini… Bapak, ya?" id b20_002

    ageng "{i}(meletakkan kacamata bacanya perlahan-lahan){/i} Saya pemiliknya. Ada yang bisa saya bantu, Tuan?" id b20_003

    "Pria itu membuka tas kulitnya dan meletakkan beberapa gepok uang pecahan seratus ribu ke atas konter jati. Bunyinya tebal dan berat. Jumlahnya fantastis — jauh melampaui harga ratusan kaset di toko ini." id b20_004

    kaya "Saya dengar apa yang dijual di toko ini. Dan saya tidak suka basa-basi. {i}(menatap rak-rak kaset){/i} Saya mau beli semua kaset untuk enam bulan ke depan. Pergerakan saham. Keputusan investasi. Grafik pasar — sebelum semua itu terjadi. {i}(tersenyum){/i} Saya mau membeli saham masa depan, Pak." id b20_005

    kai_hati "Enam bulan…? Aku pakai kaset ini buat ngadepin ulangan matematika sama rasa malu di kelas. Orang ini mau pakai buat… pasar saham?" id b20_006

    menu:
        "Kai ada di ruangan itu. Apa yang dia lakukan?"

        "Menyela, membela Pak Ageng.":
            $ record_major_choice(5, "A")
            show kai panik at pos_left
            kai "{i}(berdiri dari kursinya, suaranya bergetar tapi keluar juga){/i} P-Pak. Maaf. Toko ini nggak jual yang kayak gitu. Bapak salah tempat—" id b20_007a
            show kaya biasa at pos_center
            "Pria kaya itu menoleh. Untuk pertama kalinya dia benar-benar melihat Kai — dari seragam sekolahnya sampai ujung kabel mikrofon di kantong jaketnya. Tatapannya berhenti satu detik lebih lama dari yang nyaman." id b20_008a
            kaya "{i}(pelan, mengingat){/i} …Kamu yang sering ke sini, ya." id b20_009a
            kai_hati "Dia ngomongnya pelan. Tapi rasanya kayak namaku barusan ditulis di buku catatannya." id b20_010a
            ageng "{i}(tenang, memotong){/i} Anak ini tamu saya, Tuan. Urusan Tuan dengan saya." id b20_011a

        "Diam mendengarkan.":
            $ record_major_choice(5, "B")
            "Kai menahan napas di kursinya. Jari-jarinya mencengkeram tepi kursi kayu. Dia menatap tumpukan uang itu, lalu Pak Ageng, lalu uang itu lagi — dan tidak bilang apa-apa." id b20_007b

        "Dengarkan tawarannya sampai habis.":
            $ record_major_choice(5, "C")
            "Kai diam — tapi bukan karena lumpuh. Dia mendengarkan. Semua. Karena sebagian kecil di kepalanya, bagian yang dulu tiap sore membeli rasa aman di konter ini, ingin tahu: masa depan itu sebenarnya dihargai berapa oleh orang seperti ini?" id b20_007c

    ageng "{i}(menatap tumpukan uang itu dengan pandangan sedingin es; tidak ada setitik pun binar tertarik){/i} Toko ini tidak melayani pembelian masa depan untuk ditukar dengan angka-angka di atas kertas, Tuan. Gema Masa ada untuk membantu jiwa-jiwa yang tersesat mencari ketenangan. Bukan untuk memuaskan keserakahan." id b20_012

    show kaya biasa at pos_center
    kaya "{i}(senyumnya hilang; suaranya masih pelan, tapi sekarang menekan){/i} Pak. Semua hal di dunia ini ada harganya. Bapak sebut saja. {i}(mengeluarkan buku cek dari tas kulitnya){/i} Kalau uang ini kurang, saya bisa tulis cek dengan nominal berapa pun yang Bapak mau. Berapa pun." id b20_013

    if get_major_choice(5) == "C":
        kai_hati "Dia nyebut angka barusan. Angka yang… kalau aku yang dengar setahun lalu, mungkin aku— nggak. Dengerin aja. Dengerin sampai habis, biar tahu rasanya ditawari." id b20_014c

    ageng "Toko ini menolak melayani Anda. {i}(berdiri tegak dari kursi goyangnya){/i} Silakan ambil kembali uang Anda, dan keluar dari sini." id b20_015

    "Di situlah kesopanan pria itu retak." id b20_016

    show kaya marah at pos_center with vpunch
    kaya "Jangan berlagak suci, Tua Bangka! {i}(wajahnya memerah padam){/i} Semua orang punya harga! Kamu juga—" id b20_017

    ageng "{i}(tidak meninggikan suara sama sekali){/i} Silakan pergi, Tuan." id b20_018

    "Pria kaya itu mendesis geram. Matanya menangkap satu kaset yang tergeletak di dekat tangan Pak Ageng. Tanpa peringatan, dia menyambarnya." id b20_019

    kaya "Kalau kamu tidak mau menjualnya, aku ambil sendiri!" id b20_020

    play sound sfx_pita_kusut
    show kai panik at pos_left with vpunch
    kai "{i}(menutup telinga){/i} Pak—?! Kasetnya—!" id b20_021

    "Pita magnetik cokelat gelap di dalam kaset itu menegang, bergetar hebat — lalu putus jadi dua di tengah jalan. Ujungnya tergulung kusut ke dalam. Mati. Dengingnya berhenti seketika, dan toko kembali senyap. Pria kaya itu tersentak, menjatuhkan kaset rusak itu ke meja dengan wajah pucat." id b20_022

    ageng "{i}(sangat tenang, dan justru karena itu menusuk){/i} Masa depan tidak bisa dibeli dengan keserakahan. Pita itu putus karena dia menolak merekam jiwa yang kotor. {i}(jeda){/i} Sekarang, silakan pergi. Sebelum toko ini benar-benar menutup pintunya untuk Anda selamanya." id b20_023

    hide kaya with dissolve
    play sound sfx_lonceng_pintu
    "Dengan tangan gemetar dan napas terengah, pria itu menyambar kembali gepok-gepok uangnya dan berlari keluar, menembus gerimis yang mulai menderas di gang buntu." id b20_024

    stop music fadeout 1.0
    play music bgm_toko loop fadein 1.5
    play sound sfx_hujan_deras loop fadein 0.8
    show kai sedih at pos_left
    show ageng biasa at pos_right

    "Di dalam toko, keheningan turun lagi seperti debu yang mengendap. Kai menatap kaset dengan pita putus di atas meja itu lama sekali." id b20_025

    kai_hati "Aku dulu juga ke sini buat nguasain besok. Bedanya cuma… aku takut, dia serakah. Dan pita ini nggak peduli bedanya di mana — dia putus buat kami berdua kalau dipaksa." id b20_026

    ageng "{i}(duduk kembali, menghela napas pelan, menuang teh untuk dirinya sendiri){/i} Tehmu sudah dingin, Nak. Bapak tuang yang baru, ya." id b20_027

    stop sound fadeout 0.6

    if get_major_choice(5) == "C":

        stop music fadeout 1.0
        scene bg_kamar_kai_malam with fade
        show kai cemas at pos_center with dissolve

        "Malam itu, angka-angka dari toko tadi tidak mau pergi dari kepala Kai. Dia membuka laci mejanya — kaset-kaset ramalan lamanya masih di sana — dan, tanpa sadar, mulai menghitung. Kaset ini dulu berapa. Yang itu berapa. Semua kaset di rak Pak Ageng, kalau dijual ke orang seperti tadi, jadi berapa." id b20_028c

        show kai biasa at pos_center
        kai_hati "{i}(menutup laci pelan-pelan){/i} …Nggak. Udahan. Angka itu bukan urusanku lagi. {i}(jeda){/i} Tapi anehnya, sekarang aku tahu persis kenapa Pak Ageng nggak pernah mau nyebut harga buat yang satu itu." id b20_029c

    return
