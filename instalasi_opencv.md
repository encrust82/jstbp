# Instalasi OpenCV (Linux)

OpenCV adalah pustaka sumber terbuka yang dikembangkan untuk keperluan *computer vision*. OpenCV dikembangkan oleh Intel Corp dan bersifat *cross-platform*. OpenCV mendukung bahasa C, C++, Python, Java, dan Matlab. Untuk sekarang kita menggunakan bahasa Python untuk pembelajarannya.

Sebelum instalasi, pastikan komputer kamu sudah terpasang Python.

Untuk Python2:
```shell
pip install opencv-python
```
Untuk Python3:
```shell
pip3 install opencv-python
```

Jika proses telah selesai, untuk memastikan OpenCV sudah terinstall jalankan. Terminal tidak mengeluarkan output berarti proses pemasangan berhasil.

```shell
python -c "import cv2"
```
# Program Python Sederhana
Sekarang kita ujicoba OpenCV dengan menggunakan bahasa pemrograman Python. Sekarang kamu siapkan satu buah berkas gambar dan buat berkas berekstensi *.py*, sekarang kita buat berkas bernama ujicoba.py.

```python
import cv2

imgLoad = cv2.imread("gambar1.jpg")		# Membaca berkas gambar1.jpg lalu simpan ke variabel imgLoad
cv2.imshow("Citra", imgLoad)			# Menampilkan gambar yang telah dibaca

cv2.waitKey(0)			# Menghentikan menampilkan gambar hingga pengguna menekan tombol
cv2.destroyAllWindows()
```
Pastikan sebelum menjalankan program, berkas dengan nama *gambar1.jpg* sudah disiapkan dan diletakan di direktori yang sama dengan berkas pythonnya.

Untuk menjalankan program, buka terminal kamu (pastikan di direktori yang sama dengan ujicoba.py) lalu jalankan perintah berikut.
```shell
python ujicoba.py
```
Hasilnya akan seperti gambar di bawah ini.
![](/src/hasil_ujicoba.png)
