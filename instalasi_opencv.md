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