import secrets
from tonsdk.contract.wallet import Wallets, WalletVersionEnum
from tqdm import tqdm
from colorama import Fore, Style, init

# Inisialisasi colorama untuk memastikan warna bekerja pada semua OS
init(autoreset=True)

# ASCII art dengan warna pelangi
ASCII_ART = r"""
 _______                          
|     __|.--.--.---.-.-----.---.-.
|__     ||  |  |  _  |-- __|  _  |
|_______||___  |___._|_____|___._|
         |_____|
"""

# Warna pelangi untuk ASCII art
RAINBOW_COLORS = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN
]

# Fungsi untuk menampilkan ASCII art dengan warna pelangi
def print_rainbow_ascii_art():
    for i, line in enumerate(ASCII_ART.splitlines()):
        color = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
        print(color + line)

# Tampilkan ASCII art dengan warna pelangi
print_rainbow_ascii_art()

# Fungsi untuk menghasilkan dompet TON
def create_wallet():
    # Membuat dompet baru menggunakan Wallets.create()
    mnemonics, pub_k, priv_k, wallet = Wallets.create(WalletVersionEnum.v4r2, workchain=0)
    
    # Mendapatkan alamat dompet dari wallet
    address = wallet.address.to_string(True, True, False)
    
    return address, priv_k.hex(), mnemonics

# Meminta pengguna memasukkan jumlah wallet yang ingin dibuat
try:
    jumlah_wallet = int(input("Masukkan jumlah wallet yang ingin dibuat: "))
except ValueError:
    print("Input tidak valid, harus berupa angka!")
    exit()

# Membuat dan menyimpan wallet ke dalam wallets.txt dengan progress bar
with open('wallets.txt', 'w') as f:
    with tqdm(total=jumlah_wallet, desc="Membuat Wallet", ncols=100, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as pbar:
        for i in range(1, jumlah_wallet + 1):
            address, private_key, mnemonics = create_wallet()
            # Menyimpan alamat, kunci privat, dan mnemonik ke file
            f.write(f"{i}. Address: {address}\n")
            f.write(f"   Private Key: {private_key}\n")
            f.write(f"   Mnemonic: {' '.join(mnemonics)}\n\n")
            pbar.update(1)  # Update progress bar setiap kali wallet selesai dibuat

print("\n✨ Wallet berhasil disimpan ke wallets.txt")
