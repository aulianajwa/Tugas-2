## Perbedaan Asynchronous Programming dengan Synchronous 
Pemrograman sinkronus bekerja dengan cara menyelesaikan satu tugas terlebih dahulu sebelum lanjut ke task selanjutnya. Kekurangan dari pemrograman sinkronus adalah waktu eksekusi yang lama karena ada proses menunggu. Di sisi lain, pemrograman asinkronus memungkinkan jalannya tugas secara bersamaan tanpa harus menunggu tugas sebelumnya selesai. 

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Alur dari event-driven programming bergantung kepada events yang terjadi. Event tersebut dapat terjadi karena adanya action yang dilakukan oleh user, contohnya mouse click. Contoh pada tugas ini adalah di bagian submit new task pada bagian modal. Pada bagian ini, terdapat function ajax yang akan dijalankan hanya saat button submit di-click.

## Jelaskan penerapan asynchronous programming pada AJAX.
Dengan menerapkan asynchronous programming pada AJAX, website tidak perlu mereload halaman saat ada perubahan data, baik itu mengirimkan data atau menerima data. Misalnya pada tugas ini, saat kita menggunakan function get dan post, data yang diubah akan dikirimkan ke server tanpa harus ada reload page.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat function show_json di views.py untuk menampilkan data json lalu buat routing di urls.py
2. Menambahkan navbar dan modal untuk membuat input create task
3. Membuat script jquery untuk melakukan get data dari json. Lalu loop tiap elemennya dan dimasukkan ke elemen cards.
4. Membuat function add task di views yang nantinya akan digunakan untuk melakukan post
5. Membuat function post yang akan diakses melalui event click pada button. Pada function ini, akan dibuat objek task baru dan dimasukkan ke cards


