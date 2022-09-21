## Perbedaan JSON, XML, dan HTML
JSON (JavaScript Object Notation) merupakan sebua
## Mengapa Data Delivery Dibutuhkan?
Data delivery dibutuhkan untuk 

 
## Cara Mengimplementasikan Checklist Tugas 3
Seperti lab dan tugas sebelumnya, pertama saya membuat sebuah aplikasi baru bernama mywatchlist. Lalu saya membuat file initial_mywatchlist_data.json untuk menampung semua data yang akan ditampilkan.

Setelah itu, saya membuat models yang akan ditampilkan pada aplikasi ini, yaitu *watched, title, rating, release_date, review*. Kemudian, saya membuat sebuah file initial_mywatchlist_data.json untuk menampung data-data dari models tersebut. Setelahnya baru saya membuat sebuah file html yang akan menjadi struktur dari aplikasi ini. Kemudian saya juga menyelesaian views dan routing.

**Data Delivery** 
Tambahan terbaru untuk aplikasi ini adalah menyajikan data dalam format xml dan json. Untuk tahapan ini, pertama saya membuat fungsi-fungsi show_xml dan show_json di file views.py. Kemudian, saya menambahkan path pada urls.py agar kita bisa mengakses http://localhost:8000/mywatchlist/xml/ dan http://localhost:8000/mywatchlist/json/