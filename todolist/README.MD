
## Kegunaan  {% csrf_token %}
Cross-Site Request Forgery Attack merupakan sebuah serangan lama yang dilakukan dengan cara membuat user mengirimkan request ke sebuah website tanpa diketahui oleh user aslinya. Cara untuk mencegahnya adalah dengan membuatkan sebuah token (CSRF token) yang bersifat unik ke tiap user sehingga sulit ditebak. Maka dari itu disertakan {% csrf_token %} pada tag <form> agar bisa dipastikan bahwa yang akan memasukkan data ke web adalah user yang asli.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 




## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pada button Create Task telah dibuat URL-nya menuju fungsi create_task pada views.py. Pada fungsi tersebut telah dibuat implementasinya, yaitu dengan cara membuat object Task yang parameternya sesuai dengan data yang diinput oleh user. Setelah object dibuat, akan dihubungkan ke html melalui show_todolist yang akan menampilkan object sesuai dengan user yang membuatnya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
