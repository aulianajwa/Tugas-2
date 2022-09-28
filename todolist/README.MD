https://katalog-item.herokuapp.com/todolist/

## Kegunaan  {% csrf_token %}
Cross-Site Request Forgery Attack merupakan sebuah serangan lama yang dilakukan dengan cara membuat user mengirimkan request ke sebuah website tanpa diketahui oleh user aslinya. Cara untuk mencegahnya adalah dengan membuatkan sebuah token (CSRF token) yang bersifat unik ke tiap user sehingga sulit ditebak. Maka dari itu disertakan {% csrf_token %} pada tag <form> agar bisa dipastikan bahwa yang akan memasukkan data ke web adalah user yang asli.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 
Ya, kita tidak harus membuat elemen <form> dengan {{form.as_table}}, kita bisa membuatnya secara manual dengan membuat input seperti :
<input type="text" name="title" placeholder="Title" class = "form-control">
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
