Link Aplikasi Heroku : https://pudding-tugas2-pbp.herokuapp.com/

> Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

>Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
virtual environment digunakan supaya development project yang menggunakan virtual environment tidak mempengaruhi konfigurasi seperti software-software dan library yang digunakan oleh komputer secara global. Aplikasi tetap dapat dibuat tanpa menggunakan virtual environment tetapi dapat menyebabkan konflik terhadap software-software dan library lain yang diinstallasi pada komputer lokal sehingga tidak disarankan.

>Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. Mengimpor model CatalogItem dari katalog.models.py lalu membuat fungsi show_catalog pada katalog.views.py yang menyajikan object dari CatalogItem dalam data_catalogue beserta name dan student_id dimana akan dirender kepada katalog.html

2. Membuat katalog.urls.py dimana dari library django.urls diimpor path dan juga mengimpor katalog.views.py dimana dibuat variabel urlpatterns untuk menyajikan katalog.views.py pada url ''

3. Pada katalog.html memasukkan data dengan syntax yang telah diberikan django untuk memasukkan data dengan memberi tanda {{variable}} (seperti {{nama}}, {{student_id}}, dst) pada berkas html yang dimana variabel diambil dari variabel context dari fungsi show_catalog pada katalog.views.py