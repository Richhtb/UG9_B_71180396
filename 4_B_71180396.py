print("="*5,"GEBYAR DISKON","="*5)
print("="*5,"MASUKKAN JUMLAH BARANG YANG DIPESAN","="*5)
kipasAngin = int(input("KIPAS ANGIN DISKON 10%   Rp 25.000,00    :"))
sepeda= int(input("SEPEDA DISKON 55%        Rp 6.000,00     :"))
helmRossi= int(input("HELM ROSSI DISKON 77%    Rp 8.000,00     :"))
print("="*5,"TOTAL","="*5)
totalKipas = 25_000 * (10/100) * kipasAngin
totalSepeda = 6_000 *(55/100) * sepeda
totalHelm = 8_000 * (77/100) * helmRossi
totalDiskon = totalKipas + totalSepeda + totalHelm
print(f'TOTAL KIPAS ANGIN       : Rp {totalKipas}')
print(f'TOTAL SEPEDA SUPER      : Rp {round(totalSepeda,2)}')
print(f'TOTAL HELM ROSSI        : Rp {totalHelm}')
print(f'Jumlah total biaya yang harus dibayar adalah Rp {totalDiskon}')