https://katalog-item.herokuapp.com/todolist/

## Kegunaan  {% csrf_token %}
Cross-Site Request Forgery Attack merupakan sebuah serangan lama yang dilakukan dengan cara membuat user mengirimkan request ke sebuah website tanpa diketahui oleh user aslinya. Cara untuk mencegahnya adalah dengan membuatkan sebuah token (CSRF token) yang bersifat unik ke tiap user sehingga sulit ditebak. Maka dari itu disertakan {% csrf_token %} pada tag form agar bisa dipastikan bahwa yang akan memasukkan data ke web adalah user yang asli.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 
Ya, kita tidak harus membuat elemen <form> dengan {{form.as_table}}, kita bisa membuatnya secara manual dengan membuat input seperti :
```ruby
<input type="text" name="title" placeholder="Title" class = "form-control">
```
Jika kita membuat langsung dengan {{form.as_table}}, maka kolom input akan langsung di-generate secara otomatis


## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pada button Create Task telah dibuat URL-nya menuju fungsi create_task pada views.py. Pada fungsi tersebut telah dibuat implementasinya, yaitu dengan cara membuat object Task yang parameternya sesuai dengan data yang diinput oleh user. Setelah object dibuat, akan dihubungkan ke html melalui show_todolist yang akan menampilkan object sesuai dengan user yang membuatnya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat app baru yang bernama 'todolist'
2. Membuat routing ke todolist di project_jango
3. Membuat model dan atributnya lalu migrate
4. Melengkapi fungsi-fungsi di views.py untuk menampilkan data model, melakukan registrasi, login, dan logout
5. Menambahkan routings di todolist untuk mengakses halaman-halaman register, login, dan logout
6. Membuat file forms.py untuk membantu mengimplementasikan fungsi create_task di views.py
7. Melengkapi file html : todolist.html, register.html, login.html, create_task.html
8. Melakukan deployment ke heroku

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Internal CSS : Menggunakan <style> tag pada head section di HTML. Internal CSS cocok untuk digunakan saat kita ingin menata satu halaman web saja sehingga bisa menjadi kurang efisien saat kita ingin menata banyak halaman.

External CSS : Menggunakan .css file yang dapat mengubah keseluruhan tampilan website dalam satu waktu. Untuk menghubungkan file css ini dengan file html, kita harus menambahkan referensi external filenya. Kekurangan external CSS adalah halaman website tidak akan dirender sampai file CSS sepenuhnya di-load.

Inline CSS : Digunakan untuk menata elemen-elemen spesifik di file HTML. Kita dapat menambahkan atribut style pada tiap tag elemen HTML. Namun, akan menjadi tidak efisien jika kita memiliki banyak elemen yang harus ditata.

##  Jelaskan tag HTML5 yang kamu ketahui.
1. <a> : untuk mendefinisikan sebuah hyperlink
2. <form> : untuk membuat sebuah form untuk user input
3. <img> : menampilkan sebuah gambar
4. <p> : menampilkan tulisan pendek 
5. <ul> : menampilkan sebuah unordered list

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Universal selector : memilih seluruh elemen, menggunakan *
2. Element selector : memilih elemen berdasarkan tagnya
3. Id selector : membuat sebuah atribut id pada elemen HTML yang ingin ditata, lalu memanggil id tersebut dengan #

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama, saya membuat sebuah static folder yang berisi file style.css untuk membuat external CSS. Kemudian, saya mulai menambahkan header untuk menggunakan bootstrap. Lalu saya melanjutkan design dengan menambahkan style dan CSS.
