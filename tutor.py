from rich.console import Console
import time

console = Console()

# Fungsi banner
def banner():
    console.print("[bold red]#######                            [/bold red]")
    console.print("[bold red]   #    #    # #####  ####  #####  [/bold red]")
    console.print("[bold red]   #    #    #   #   #    # #    # [/bold red]")
    console.print("[bold red]   #    #    #   #   #    # #    # [/bold red]")
    console.print("[white]   #    #    #   #   #    # #####  [/white]")
    console.print("[white]   #    #    #   #   #    # #   #  [/white]")
    console.print("[white]   #     ####    #    ####  #    # [/white]\n")
    console.print("[white]Tools Dibuat Oleh [bold red](Asep Riezky)[/bold red]\n")

# Fungsi untuk menampilkan menu
def menu():
    console.print("[bold green]Menu:[/bold green]")
    console.print("[bold green]1. Tutorial ganteng[/bold green]")
    console.print("[bold green]2. Tutorial kaya raya[/bold green] ")
    console.print("[bold green]3. Tutorial punya cewek[/bold green] ")
    console.print("[bold green]4. Tutorial membahagiakan orang tua[/bold green] ")
    console.print("[bold green]5. Tutorial sukses dunia akhirat[/bold green] ")
    console.print("[bold green]6. Tutorial chat dibalas[/bold green] ")
    console.print("[bold green]7. Exit[/bold green] ")

# Fungsi untuk menampilkan penjelasan tiap menu
def explain(choice):
    if choice == '1':
        console.print("[bold white]Nih Caranya: Pertama Lu kudu punya duit karna duit itu modal utama.     abis tu beli sabun atau skincare buat perawatan muka,     kalau emang belum juga ganteng coba oplas aja sekalian biar ganteng kek cowo korea![/bold white]")
    elif choice == '2':
        console.print("[bold white]Tutorial kaya raya: Cara mengelola keuangan dan investasi dengan cerdas![/bold white]")
    elif choice == '3':
        console.print("[bold white]Nih caranya:Kalau lu ngga ganteng lu ngga usah pengin punya cewe kecuali lu kaya dan punya harta wkwkw lagian pacaran tuh ngga boleh!! ![/bold white]")
    elif choice == '4':
        console.print("[bold white]Tutorial membahagiakan orang tua: Perlakukan orang tua dengan cinta dan perhatian yang tulus.[/bold white]")
    elif choice == '5':
        console.print("[bold white]Tutorial sukses dunia akhirat: Seimbangkan antara kehidupan dunia dan persiapan akhirat![/bold white]")
    elif choice == '6':
        console.print("[bold white] Nih Caranya: minimal lu ganteng dulu biar chat lu dibales secara fast respon.kalau lu jelek mah siapapun pasti males bales chat lu,tapi kalau lu orangnya sopan dan baik hati mungkin bisa dibales secara fast respon hehe![/bold white]")

# Panggil banner sekali di awal
banner()

# Loop menu
while True:
    menu()
    choice = input("Pilih menu (1-7): ")

    if choice == '7':
        break
    elif choice in ['1', '2', '3', '4', '5', '6']:
        # Tampilkan penjelasan sesuai pilihan
        explain(choice)
        
        # Tambahkan delay agar pengguna bisa membaca penjelasan
        time.sleep(5)
        
        # Tanyakan apakah ingin kembali ke menu
        input("\n[bold green]Tekan Enter untuk kembali ke menu...[/bold green]")
        
        # Clear layar sebelum kembali ke menu, tetapi banner tetap ada
        console.clear()
        banner()  # Tampilkan ulang banner
    else:
        console.print("[bold red]Pilihan tidak valid, silakan coba lagi.[/bold red]")
