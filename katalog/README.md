https://katalog-item.herokuapp.com/katalog/

## Request Client ke Web Aplikasi
![alt text](./image/"bagan")

Pertama, urls.py akan mencari response yang cocok dari request client. Ketika ditemukan response yang tepat, view akan mengambil data dari models.py dan me-render sebuah template. Models merupakan sebuah tempat untuk menampung data-data yang ingin ditampilkan dan template merupakan hasil luaran yang akan ditampilkan pada web. 

## Mengapa Menggunakan Virtual Environment?
Virtual environment merupakan sebuah alat untuk memisahkan proyek yang berbeda dengan menyediakan suatu environment untuk sebuah proyek spesifik. Virtual environment memungkinkan modul yang digunakan pada sebuah program tidak dapat diakses oleh program lainnya. 

Virtual environment dapat menghindari kita dari konflik versi. Ketika ada program yang dibuat khusus untuk versi Django tertentu dan tidak ada pemisahan antar proyek melalui virtual environment, konflik dengan proyek lain yang menggunakan versi Django yang berbeda sangat mudah terjadi.

Pembuatan aplikasi web tanpa virtual environment masih memungkinkan, tetapi tidak disarankan. Tanpa pemisahan yang disediakan oleh virtual environment, akan sulit untuk menjaga aplikasi dari adanya konflik dan proses pemeliharaan aplikasi akan semakin rumit.

## Cara Mengimplementasi Aplikasi
**views.py**
Function yang dibuat pada views.py ini digunakan untuk mendapatkan web response dengan membuat web request. Pada file ini, saya membuat fungsi show_katalog dengan parameter request dan mengembalikan fungsi render untuk menampilkan template katalog.html dengan data yang diambil dari CatalogItem dan value dari context.

```ruby
def show_katalog(request) :
    data_item = CatalogItem.objects.all()
    context = {
        'list_item' :data_item,
        'nama' : 'Aulia Najwa Salsabila',
        'npm' : '2106751524'
    }
    return render(request, "katalog.html", context)
```
**Template**
Pada file ini saya menambahkan loop untuk menampilkan data barang pada tabel yang akan ditampilkan. Pada loop ini juga dipanggil atribut dari file models.py.
```ruby
{% for barang in list_item %}
    <tr>
        <th>{{barang.item_name}}</th>
        <th>{{barang.item_price}}</th>
        <th>{{barang.item_stock}}</th>
        <th>{{barang.rating}}</th>
        <th>{{barang.description}}</th>
        <th>{{barang.item_url}}</th>
    </tr>
    {% endfor %}
```
**Routing**
Menambahkan potongan kode ini pada file urls.py pada folder katalog :
```ruby
urlpatterns = [
    path('', show_katalog, name='show_katalog')
]
```
Kode di atas akan memanggil fungsi show_katalog yang ada di views agar halaman HTML dapat ditampilkan

Menambahkan potongan kode ini pada file urls.py pada folder project_django :
```ruby
path('katalog/', include('katalog.urls'))
```
Kode di atas ditambahkan agar ketika kita membuka web aplikasi menuju halaman yang sesuai, yaitu halaman aplikasi katalog

**Deployment**
Pada tahap ini, saya melakukan git push perubahan ke github. Lalu, saya membuat sebuah aplikasi yang akan di-deploy melalui Heroku. Kemudian saya membuat pengaturan secrets pada repository sebelum melakukan deploy.