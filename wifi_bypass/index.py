import subprocess

# Získání seznamu všech Wi-Fi profilů
wifi_profiles = subprocess.check_output(['nmcli', 'c', 'show']).decode('utf-8').split('\n')

# Vytvoření slovníku pro ukládání jmen Wi-Fi sítí a hesel
wifi_passwords = {}

# Procházení všech profilů
for profile in wifi_profiles:
    if "802-11-wireless.ssid" in profile:
        profile_name = profile.strip().split(":")[1].strip()
        try:
            password_info = subprocess.check_output(['sudo', 'cat', '/etc/NetworkManager/system-connections/' + profile_name], stderr=subprocess.PIPE).decode('utf-8')
            password = None
            for line in password_info.split('\n'):
                if "psk=" in line:
                    password = line.split("psk=")[1]
            wifi_passwords[profile_name] = password.strip() if password else "No password"
        except Exception as e:
            wifi_passwords[profile_name] = "Error retrieving password"

# Výsledky
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")
for profile_name, password in wifi_passwords.items():
    print("{:<30}| {:<}".format(profile_name, password))

