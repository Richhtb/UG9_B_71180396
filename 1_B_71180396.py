nama=input("Nama:")
namaBelakang = nama.split()[-1]
namaDepan = nama.split()[0:-1]
namaDepan = " ".join(namaDepan)
tempaTanggalhr= input("Tempat tangal lahir:")
tempat = tempaTanggalhr.split()[0]
tanggaLhr=tempaTanggalhr.split()[1:]
tanggaLhr = " ".join(tanggaLhr)
print(f'halo! {namaBelakang}, {namaDepan}')
print(f'Anda lahir di {tempat} pada tanggal {tanggaLhr} ')


