wellcome_massage = "Wellcome AizenChizuru Games"
bear_position = 2
 
# Header
print("|*************************************|")
print(f"|---- {wellcome_massage} ----|".upper())
print("|*************************************|")

# Content
nama_user = input("Masukan Nama Kamu: ")

print(f'''
      Halo {nama_user}, Coba Perhatikan Goa Dibawah Ini"
      |_| |_| |_| |_| |_| 
'''.upper())

pilihan_user = int(input("Menurut Kamu Mana Beruang Itu Bersembunyi ? [1 / 2 / 3 / 4 / 5] : "))

print(f"Pilihan Kamu Adalah {pilihan_user}".upper())

if bear_position == bear_position:
    print("selamat kamu menemukannya".upper())
else:
    print("kamu kalah tidak menemukan beruang".upper())