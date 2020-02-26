import cv2

imgLoad = cv2.imread("gambar1.jpg")		# Membaca berkas gambar1.jpg lalu simpan ke variabel imgLoad
cv2.imshow("Citra", imgLoad)			# Menampilkan gambar yang telah dibaca

cv2.waitKey(0)							# Menghentikan menampilkan gambar hingga pengguna menekan tombol
cv2.destroyAllWindows()