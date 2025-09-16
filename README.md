## Link deployment (PWS)
https://levina-aurellia-footballstation.pbp.cs.ui.ac.id

## Deskripsi Football Station
Aplikasi ini adalah tugas PBP (Football Shop) dengan nama aplikasinya yaitu 'Football Station'. Aplikasi ini dibuat menggunakan Django (MVT) dan memenuhi requirement tugas 2 mata kuliah PBP yang antara lain seperti model `Product` memiliki atribut `name`, `price`, `description`, `thumbnail`, `category`, `is_featured` dengan sedikit tambahan atribut sebagai variasi.

---
## Jawab Pertanyaan Tugas 2
<details>
<summary>📘 Tugas 2</summary>

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step  
[Jawaban]  
Pertama, saya membuat project Django baru dengan perintah django-admin startproject footballstation . di terminal folder football-station, dengan begitu terbentuklah kerangka dasar proyek beserta file manage.py. Setelah itu, saya menambahkan sebuah app bernama main menggunakan python manage.py startapp main, lalu mendaftarkannya ke dalam INSTALLED_APPS di settings.py. Di dalam app main, saya mendesain sebuah model Product yang berisi beberapa field utama seperti name, price, description, thumbnail, category, dan is_featured. Saya juga menambahkan field tambahan stock serta brand dengan choices. Agar perubahan model tersimpan ke database, saya menjalankan python manage.py makemigrations dan python manage.py migrate.  
Selanjutnya, saya membuat fungsi view show_main di views.py yang akan me-render file template main.html. Template ini saya isi dengan informasi sederhana seperti nama aplikasi, nama, dan kelas saya. Routing dilakukan dengan menambahkan path ke urls.py yang ada di dalam main, lalu menghubungkannya dengan urls.py sehingga bisa diakses lewat browser. Setelah itu, saya melakukan testing lokal dengan menjalankan python manage.py runserver. Saat semuanya sudah berjalan baik, saya menyiapkan deployment ke PWS. Untuk itu saya membuat file requirements.txt dengan pip freeze > requirements.txt, memastikan gunicorn sudah termasuk di dalamnya, lalu menambahkan ALLOWED_HOSTS. Saya juga mengubah schema menjadi tugas_individu. Terakhir, saya melakukan git add . lalu git commit, kemudian menjalankan git push pws master dengan credentials PWS yang diberikan. Setelah proses build selesai dan statusnya berubah menjadi Running, aplikasi saya sudah berhasil diakses melalui link PWS.  
  

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.  
[Jawaban]  
Berikut adalah bagan yang telah dibuat:   
![Alur Request-Response Django](gambar/bagan_no2.png)   
Ringkasan penjelasan tambahan:  
- urls.py untuk menentukan URL mana akan ditangani oleh view mana.
- views.py, berisi fungsi/class yang menangani request, mengambil data dari models, lalu menyiapkan context untuk template.
- models.py untuk mengatur struktur data di database, termasuk query untuk mengambil atau menyimpan data.
- Template HTML,  berisi template tag untuk menampilkan data yang dikirim dari view.
  

3. Jelaskan peran settings.py dalam proyek Django!  
[Jawaban]  
settings.py merupakan pusat konfigurasi proyek Django. Semua pengaturan penting terkait database, template, middleware, security, semuanya dikelola di settings.py ini. Perannya mulai dari BASE_DIR yaitu menyimpan data path dasar proyek. Kemudian, SECRET_KEY untuk keamanan seperti enkripsi token, DEBUG untuk menentukan apakah Django menampilkan pesan error atau tidak. Kemudian, ALLOWED_HOSTS untuk mendaftarkan domain/IP yang boleh mengakses aplikasi. INSTALLED_APPS berisi daftar aplikasi Django custom apps yang aktif, seperti di sini saya menambahkan 'main' ke dalam INSTALLED_APPS. Kemudian, MIDDLEWARE berperan untuk menentukan proses req atau response yang dijalankan Django.   
Dari penjelasan di atas tentang peran masing-masing komponen yang ada pada settings.py, menunjukkan bahwa settings.py tidak hanya berfungsi sebagai kumpulan konfigurasi teknis, tetapi juga sebagai penghubung antarbagian framework Django. Mulai dari keamanan (SECRET_KEY, DEBUG, ALLOWED_HOSTS), aplikasi yang digunakan (INSTALLED_APPS), hingga alur request-response (MIDDLEWARE), semuanya pengaturannya dari file ini. Oleh karena itu, settings.py merupakan pusat yang memastikan setiap komponen dalam proyek Django berjalan sesuai aturan dan kebutuhan yang telah ditentukan.  


4. Bagaimana cara kerja migrasi database di Django?  
[Jawaban]  
Adanya migrasi database pada Django bertujuan untuk menyimpan instruksi segala hal modifikasi skema basis data. Setiap kali terdapat perubahan, menambahkan, atau memodifikasi perlu dipastikan bahwa basis data tersimpan dan sinkron dengan model yang ada pada proyek Django. Maka dari itu, Django menggunakan migrasi inilah untuk tiap kali menerapkan perubahan ke basis data dengan dua perintah, yaitu makemigrations dan migrasi. Berikut cara kerjanya:  
    - Pertama, Django akan memeriksa perubahan pada model dengan membandingkannya terhadap histori migrasi sebelumnya. Setelah itu, Django membuat file migrasi di direktori app/migrations/ berupa file Python yang berisi instruksi perubahan skema database. Nantinya berkas-berkas migrasi akan diberi nomor otomatis sebagai penanda perubahan yang dibuat pada skema basis data.
    - Kedua, setelah file migrasi terbentuk, perintah python manage.py migrate dijalankan untuk menerapkan instruksi tersebut ke database. Django memastikan migrasi dijalankan sesuai urutan yang benar dan menyimpan catatan migrasi yang sudah diterapkan di tabel khusus bernama django_migrations.
    -  Dengan menjalankan perintah tersebut, Django akan melakukan pembaruan pada skema database sehingga selaras dengan modifikasi yang tercatat dalam berkas migrasi.  

  
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?  
[Jawaban]  
Berdasarkan referensi yang telah saya baca, Django cocok dijadikan pemulaan belajar pengembangan perangkat lunak karena erat kaitannya dengan Python yang banyak orang sudah familiar dengan bahasa pemrograman tersebut, sehingga waktu pengembangan bisa lebih efektif. Selain itu, dokumentasinya lengkap sehingga pemula (seperti saya) mudah mengikuti panduan yang ada. Django juga menggunakan pendekatan 'batteries included' yang artinya menyediakan berbagai fitur penting bawaan seperti ORM sehingga kita tidak perlu membangun semuanya dari nol. Di sisi lain, Django juga memiliki sistem keamanan terintegrasi dan selalu diperbarui, misalnya perlindungan dari XSS, CSRF, dan SQL Injection, tanpa perlu bergantung pada library pihak ketiga yang rentan bug, membuat Django cukup aman dan terpercaya. Framework ini juga fleksibel karena bisa digunakan untuk proyek kecil maupun besar, bahkan hingga level perusahaan seperti Spotify dan Quora, serta mendukung lintas platform dan berbagai basis data. Django juga mengikuti prinsip pemrograman DRY (Don't Repeat Yourself) dan KISS (Keep It Simple and Short) sehingga kode yang dihasilkan lebih rapi, mudah dibaca, dan minim bug. Ditambah lagi, Django memiliki dukungan REST API yang memudahkan pengembang dalam membuat layanan pertukaran data tanpa harus berurusan langsung dengan detail teknis query database. Yang tidak kalah penting, Django juga punya komunitas global yang sangat besar, aktif, dan suportif, sehingga jika ada kesulitan akan mudah menemukan solusi terbaik dari para pengembang berpengalaman. Dengan semua alasan tersebut itulah yang saya rasa mengapa Django dijadikan sebagai framework yang ideal untuk pemula dalam memahami konsep dasar pengembangan perangkat lunak.
  
  
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?  
[Jawaban]  
Menurut saya, arahan yang diberikan asdos pada tutorial 1 sangat membantu saya memahami alur pembuatan proyek Django, mulai dari routing hingga bagian-bagian lainnya. Tanpa penjelasan yang asdos sampaikan, baik melalui Discord maupun web tutorial, mungkin saya akan kesulitan menyelesaikan tugas 2 ini. Oleh karena itu, saya rasa tidak ada saran khusus untuk asdos, hanya harapan saya mungkin agar pada sesi lab berikut-berikutnya tetap seperti ini yaitu memberikan penjelasan yang jelas dan lengkap. Terima kasih banyak, kakak asdos!
  
   
Referensi:  
1. https://www.geeksforgeeks.org/python/django-basic-app-model-makemigrations-and-migrate/
2. https://blog.jetbrains.com/pycharm/2023/11/django-vs-flask-which-is-the-best-python-web-framework/
3. https://opensource.com/article/18/8/django-framework
4. https://www.geeksforgeeks.org/blogs/why-django-framework-is-best-for-web-development/
5. https://www.djangoproject.com/start/overview/
</details>

---
## Jawab Pertanyaan Tugas 3
<details>
<summary>📘 Tugas 3</summary>

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?  
[Jawaban]  
Pada dasarnya data delivery merupakan cara kita mengirimkan data dari satu bagian sistem ke bagian lain. Formatnya bisa macam-macam, misal HTML, XML, atau JSON. Kalau HTML biasanya dipakai untuk menampilkan data langsung ke pengguna lewat browser, sedangkan XML dan JSON lebih sering dipakai untuk pertukaran data antar aplikasi. 
  
    Maka dari itu, kita perlu data delivery karena dalam pengembangan platform modern, data tidak hanya dipakai oleh satu tampilan saja, melainkan dipakai juga dalam:
- data perlu data untuk ditampilkan ke user
- aplikasi mobile mengambil data yang sama lewat API
- layanan pihak ketiga/ integrasi (c/. dashboard analitik) perlu pula mengakses data itu
- testing dan automasi lebih mudah dilakukan kalau ada akses ke data mentahnya.  
    Dengan adanya data delivery (terutama format XML atau JSON), backend bisa menyediakan data yang terpisah dari tampilan, sehingga lebih fleksibel, bisa dipakai berulang bagi frontend, dan membuat sistem lebih modular.  
   
   
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?  
[Jawaban]  
XML maupun JSON bisa dipakai untuk menyimpan dan bertukar data. XML memiliki kelebihan untuk kebutuhan dokumen yang kompleks karena mendukung metadata, namespace, dan transformasi seperti XSLT. Namun, cara aksesnya lah yang bisa dibilang lebih ribet, perlu parsing dengan XML DOM lalu looping elemen satu per satu. Sedangkan JSON lebih sederhana. Data disusun dengan format objek/array sehingga mudah dibaca, ditulis, dan diproses. Bahkan di JavaScript saat menerima JSON bisa langsung melakukan JSON.parse() dan data bisa langsung dipakai.  
    
    Jadi, kalau diberi pilihan mana yang lebih baik, saya menjawabnya tergantung. XML lebih baik untuk dokumen yang kompleks dengan kebutuhan metadata, JSON lebih baik untuk API modern terutama web dan mobile, karena lebih ringan, mudah, dan cepat.
  
    Dan JSON lebih popular karena kebanyakan aplikasi sekarang butuh API yang cepat, efisien, dan mudah diintegrasikan dengan JavaScript atau bahasa pemrograman lain.
   
   
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut.   
[Jawaban]  
Method is_valid() pada form Django dipakai untuk melakukan validasi data yang dikirimkan lewat form. Ketika kita membuat instance form dan mengisinya dengan data (biasanya dari request.POST), kita perlu memanggil form.is_valid() supaya Django bisa mengecek apakah data tersebut memenuhi semua aturan validasi yang berlaku.   
   
    Proses validasi ini bukan hanya sekadar ngecek tipe data dasar (misalnya angka atau teks), tapi lebih dalam lagi:  
- Django akan membersihkan data melalui mekanisme `full_clean()`, sehingga setiap field punya data yang sudah sesuai format.
- Django juga menjalankan validator bawaan maupun custom (misalnya cek panjang minimal password).
- Kalau form tersebut berbasis ModelForm, Django ikut memanggil `validate_unique()` untuk memastikan field yang diberi atribut `unique=True` tidak duplikat di database.
- Semua error yang ditemukan tidak langsung menghentikan proses, tapi dikumpulkan di `form.errors`.
   
    Hanya setelah semua tahap validasi ini lolos, form.is_valid() akan mengembalikan True. Kalau ada yang gagal, ia mengembalikan False dan kita bisa kasih feedback yang sesuai di template.   
    
    Alasan mengapa kita butuh is_valid() adalah karena Django sudah menyediakan satu mekanisme validasi yang lengkap, reusable, dan aman. Kalau kita mencoba bikin validasi sendiri langsung di view, biasanya hasilnya lebih ribet, gampang ada bug, dan sulit dipakai ulang. Dengan is_valid(), kita bisa yakin data yang masuk sudah dicek dari banyak sisi (tipe data, format, constraint unik, dsb.) sebelum diproses lebih lanjut seperti disimpan ke database.   

    
   
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?  
[Jawaban]  
csrf_token dipakai untuk melindungi aplikasi web dari serangan Cross-Site Request Forgery (CSRF). Serangan CSRF terjadi ketika penyerang mencoba menggunakan sesi login pengguna yang masih aktif. Misalnya, pengguna sedang login ke aplikasi bank online, lalu penyerang mengirimkan link atau form tersembunyi yang jika diklik akan mengirim request transfer dana. Karena browser pengguna otomatis menyertakan cookie sesi (yang valid), request itu bisa dieksekusi seolah-olah datang dari pengguna asli.

   Agar hal ini tidak terjadi, Django menyertakan token CSRF, yaitu string unik yang dihasilkan untuk setiap sesi pengguna. Token ini harus ikut dikirimkan bersama setiap request yang sifatnya mengubah data (POST, PUT, DELETE). Django kemudian akan mencocokkan token tersebut dengan yang tersimpan di server.
- Jika token cocok → request dianggap valid.
- Jika token tidak ada atau berbeda → request langsung ditolak (403 Forbidden).

   Kalau kita tidak menambahkan csrf_token di dalam form, maka Django tidak bisa memverifikasi apakah request benar-benar dibuat oleh user yang sah atau hasil manipulasi pihak luar. Dapat berakibat seperti Form bisa dipalsukan oleh penyerang dan “diselundupkan” lewat link atau script berbahaya, bahkan penyerang bisa memanfaatkan sesi login aktif untuk melakukan aksi berbahaya (misalnya ubah password, kirim pesan spam, transfer dana, dsb.) tanpa sepengetahuan user.
   
  Jadi, csrf_token itu semacam pelindung yang memastikan kalau request memang berasal dari user yang sedang membuka form di aplikasi kita, bukan dari sumber luar yang berbahaya.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  
[Jawaban]  
Pertama, saya membuat direktori baru bernama templates di root folder proyek dan menambahkan file base.html sesuai dengan kode yang ada di tutorial 2. Setelah itu, saya menambahkan direktori templates tersebut ke dalam variabel TEMPLATES yang terdapat di settings.py pada direktori proyek football_station.
   
    Kemudian, saya mengubah berkas main.html yang ada di main/templates dengan kode yang disesuaikan dari tutorial 2. Saya juga membuat file baru bernama forms.py di direktori main, isinya sesuai dengan definisi form yang sudah ditentukan. Setelah itu, di views.py pada direktori main, saya menambahkan fungsi untuk tombol add_product dan juga fungsi untuk tombol detail_product.
    
    Selanjutnya, di urls.py pada direktori main, saya mengimpor fungsi-fungsi yang sudah dibuat tadi dan menambahkan path URL baru ke dalam variabel urlpatterns. Setelah itu, saya mengubah isi main.html serta membuat file add_product.html dan detail_product.html di main/templates untuk menampilkan form penambahan produk dan detail data dari setiap objek model.
    
    Berikutnya, saya menambahkan konfigurasi CSRF_TRUSTED_ORIGINS di settings.py pada direktori root proyek. Lalu, di views.py saya membuat empat fungsi tambahan untuk kebutuhan data delivery. Setelah fungsi tersebut selesai dibuat, saya mengimpornya ke dalam urls.py di direktori main dan menambahkan path baru ke dalam urlpatterns.
    
    Terakhir, karena saya menambahkan field UUID pada models.py, saya melakukan makemigrations terlebih dahulu, kemudian menjalankan runserver untuk memastikan proyek berjalan lancar. Setelah semuanya selesai, saya melakukan push proyek ke GitHub serta mengunggahnya ke PWS.
    
6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?   
[Jawaban]  
Menurut saya, tutorial 2 berjalan aman dan terkendali, kak Asdos juga sangat membantu dalam menjelaskan materi serta membimbing langkah-langkah pengerjaan, terima kasih kak.
   
Referensi:  
1. https://www.geeksforgeeks.org/html/difference-between-json-and-xml/
2. https://docs.djangoproject.com/en/5.2/ref/forms/api/
3. https://stackoverflow.com/questions/73173747/django-form-is-valid-what-does-it-check
4. https://www.geeksforgeeks.org/python/csrf-token-in-django/
    
## Screenshoot Postman
XML:   
![SS XML](gambar/ss_xml.jpg)    
   
JSON:   
![SS JSON](gambar/ss_json.jpg)   
    
XML by ID:   
![SS XML BY ID](gambar/ss_xml_by_id.jpg)    
    
JSON by ID:   
![SS JSON BY ID](gambar/ss_json_by_id.jpg)    
</details>
---
