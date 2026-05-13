
# BACA INI YA SAYANG KU:
# Script ini boleh dikembangkan, dimodifikasi, dan dipelajari untuk kebutuhan pembelajaran maupun pengembangan lebih lanjut. 
# Namun, jangan menghapus credit pembuat asli dari source code ini.

# Original Author:
# Byexe

# Rasulullah ﷺ bersabda:
"""“Barang siapa mengambil hak seorang Muslim dengan sumpahnya, maka Allah mewajibkan neraka baginya dan mengharamkan surga baginya.”
(HR. Muslim No. 137)"""

# Walaupun hanya sebuah source code, tetap ada hak dan usaha milik pembuat aslinya. 
# Jangan mengambil, menghapus, atau mengklaim hak orang lain tanpa izin.

import os
import platform
import requests
import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

a = "\033[1;30m"
m = "\033[1;31m"
h = "\033[1;32m"
k = "\033[1;33m"
c = "\033[1;36m"
p = "\033[1;37m"
r = "\033[0m"

def channel_wa():
    os.system("xdg-open 'https://whatsapp.com/channel/0029Vb8Czm0B4hdQ5pc3tv0m'")
    time.sleep(2)

def cek_myip():
    try:
        respon = requests.get("https://api.ipify.org?format=json")
        data   = respon.json()

        print(f"""
    {h}[{m}+{h}]{k} My IP       {h}:{k} {data.get("ip", "-")}
        """)

    except Exception as e:
        print(f"\n    {h}[{m}!{h}]{k} Error{m} :{a} {e}")

def cek_usn():
    username = input(f"\n    {h}[{m}>{h}]{k} Enter Username {h}:{k} ").strip()

    situs = {
        "GitHub"       : f"https://github.com/{username}",
        "GitLab"       : f"https://gitlab.com/{username}",
        "Twitter/X"    : f"https://twitter.com/{username}",
        "Instagram"    : f"https://instagram.com/{username}",
        "TikTok"       : f"https://tiktok.com/@{username}",
        "Facebook"     : f"https://facebook.com/{username}",
        "Reddit"       : f"https://reddit.com/user/{username}",
        "Pinterest"    : f"https://pinterest.com/{username}",
        "Tumblr"       : f"https://tumblr.com/{username}",
        "Twitch"       : f"https://twitch.tv/{username}",
        "YouTube"      : f"https://youtube.com/@{username}",
        "LinkedIn"     : f"https://linkedin.com/in/{username}",
        "Telegram"     : f"https://t.me/{username}",
        "Steam"        : f"https://steamcommunity.com/id/{username}",
        "Keybase"      : f"https://keybase.io/{username}",
        "Pastebin"     : f"https://pastebin.com/u/{username}",
        "Replit"       : f"https://replit.com/@{username}",
        "HackerNews"   : f"https://news.ycombinator.com/user?id={username}",
        "ProductHunt"  : f"https://producthunt.com/@{username}",
        "Gravatar"     : f"https://gravatar.com/{username}",
    }

    print(f"\n    {k}Searching username {h}\"{username}\"{k} on {len(situs)} sites...\n")

    ditemukan = 0
    tidak     = 0

    for nama, url in situs.items():
        try:
            respon = requests.get(url, timeout=5, allow_redirects=True)
            if respon.status_code == 200:
                print(f"    {h}[{m}+{h}]{k} {nama:<15} : {url}")
                ditemukan += 1
            else:
                print(f"    {a}[-]{r} {nama:<15} : Not Found")
                tidak += 1
        except Exception:
            print(f"    {a}[!]{r} {nama:<15} : Timeout / Error")
            tidak += 1

    print(f"""
    {a}________________________

    {h}[{m}+{h}]{k} Found       : {ditemukan}
    {h}[{m}+{h}]{k} Not Found   : {tidak}
    {h}[{m}+{h}]{k} Total       : {len(situs)}
    """)

def cek_ip():
    ip = input(f"\n    {h}[{m}>{h}]{k} Enter IP Address {h}:{k} ").strip()

    try:
        fields = "status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
        respon = requests.get(f"http://ip-api.com/json/{ip}?fields={fields}")
        data   = respon.json()

        if data["status"] == "fail":
            print(f"\n    {m}[!]{k} {data.get('message', 'IP tidak valid.')}")
            return

        proxy   = "Yes" if data.get("proxy")   else "No"
        mobile  = "Yes" if data.get("mobile")  else "No"
        hosting = "Yes" if data.get("hosting") else "No"

        print(f"""
    {h}[{m}+{h}]{k} IP         {h} : {k}{data.get("query", "-")}
    {h}[{m}+{h}]{k} Reverse DNS {h}: {k}{data.get("reverse", "-")}
    {h}[{m}+{h}]{k} ASN        {h} : {k}{data.get("as", "-")}
    {h}[{m}+{h}]{k} ASN Name   {h} :{k} {data.get("asname", "-")}
    {h}[{m}+{h}]{k} ISP        {h} :{k} {data.get("isp", "-")}
    {h}[{m}+{h}]{k} ORG        {h} :{k} {data.get("org", "-")}
    {h}[{m}+{h}]{k} Continent  {h} : {k}{data.get("continent", "-")} ({data.get("continentCode", "-")})
    {h}[{m}+{h}]{k} Country     {h}: {k}{data.get("country", "-")} ({data.get("countryCode", "-")})
    {h}[{m}+{h}]{k} Region      {h}:{k} {data.get("regionName", "-")} ({data.get("region", "-")})
    {h}[{m}+{h}]{k} City        {h}:{k} {data.get("city", "-")}
    {h}[{m}+{h}]{k} District   {h} :{k} {data.get("district", "-") or "-"}
    {h}[{m}+{h}]{k} ZIP        {h} :{k} {data.get("zip", "-")}
    {h}[{m}+{h}]{k} Latitude  {h}  : {k}{data.get("lat", "-")}
    {h}[{m}+{h}]{k} Longitude{h}   : {k}{data.get("lon", "-")}
    {h}[{m}+{h}]{k} Timezone   {h} : {k}{data.get("timezone", "-")}
    {h}[{m}+{h}]{k} UTC Offset  {h}: {k}{data.get("offset", "-")}
    {h}[{m}+{h}]{k} Currency    {h}: {k}{data.get("currency", "-")}
    {h}[{m}+{h}]{k} Proxy/VPN  {h} : {k}{proxy}
    {h}[{m}+{h}]{k} Mobile     {h} : {k}{mobile}
    {h}[{m}+{h}]{k} Hosting   {h}  : {k}{hosting}
        """)

    except Exception as e:
        print(f"\n    {h}[{m}!{h}]{k} Error{m} :{a} {e}")

def cek_tlp():
    nomor = input(f"\n    {h}[{m}>{h}]{k} Enter International Format Phone Number {h}:{k} ").strip()

    try:
        parsed = phonenumbers.parse(nomor)

        valid        = phonenumbers.is_valid_number(parsed)
        wilayah      = geocoder.description_for_number(parsed, "id")
        operator     = carrier.name_for_number(parsed, "id")
        zona_waktu   = timezone.time_zones_for_number(parsed)
        format_intl  = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        format_lokal = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)

        print(f"""
    {h}[{m}+{h}]{k} Number      {h}: {k}{format_intl}
    {h}[{m}+{h}]{k} Local       {h}: {k}{format_lokal}
    {h}[{m}+{h}]{k} Status      {h}: {k}{"Valid" if valid else "Tidak Valid"}
    {h}[{m}+{h}]{k} Region      {h}: {k}{wilayah if wilayah else "Tidak Diketahui"}
    {h}[{m}+{h}]{k} Operator    {h}: {k}{operator if operator else "Tidak Diketahui"}
    {h}[{m}+{h}]{k} Timezone    {h}:{k} {", ".join(zona_waktu)}
        """)

    except phonenumbers.NumberParseException as e:
        print(f"\n    {h}[{m}!{h}]{k} Failed to Parse Number {m}:{a} {e}")

def main():
    try:
        respon = requests.get("http://worldtimeapi.org/api/timezone/Asia/Jakarta", timeout=3)
        data = respon.json()
        tahun, bulan, hari = data["datetime"][:10].split("-")
    except:
        from datetime import datetime
        now = datetime.now()
        hari, bulan, tahun = now.strftime("%d"), now.strftime("%m"), now.strftime("%Y")
    menu = {
        '1': cek_tlp,
        '2': cek_ip,
        '3': cek_usn,
        '4': cek_myip,
        '5': channel_wa,
    }

    while True:
        os.system("clear")
        print(f"""{m}
________         .__        __ __________.__        
\_____  \   _____|__| _____/  |\______   \  |  __ __  ______
 /   |   \ /  ___/  |/    \   __\     ___/  | |  |  \/  ___/
/    |    \\\___ \|  |   |  \  | |    |   |  |_|  |  /\___ \ 
\_______  /____  >__|___|  /__| |____|   |____/____//____  >
        \/     \/        \/                              \/ 

    {h} 🜲 {m}:{k} Byexe
    {h} ☸ {m}:{k} https://byexe.vercel.app
    {h} ☘︎ {m}:{k} 1.0.0
    {h} ⏱︎ {m}:{k} {hari}{m}-{k}{bulan}{m}-{k}{tahun}
{a}________________
    
    {h}[{m}1{h}]{k} Check Phone Number Information
    {h}[{m}2{h}]{k} Check IP Address Information
    {h}[{m}3{h}]{k} Check Username Information
    {h}[{m}4{h}]{k} Check My IP Address
    {h}[{m}5{h}]{k} Follow Byexe WhatsApp Channel
    {h}[{m}0{h}]{k} Exit
""")
        pilihan = input(f"    {h}[{m}>{h}]{k} Enter Choice {h}:{k} ").strip()

        if pilihan == '0':
            os.system("clear")
            break
        elif pilihan in menu:
            menu[pilihan]()
            input(f"  {k}Use of This Feature is Completed{m} |{h} ENTER")
        else:
            input(f"\n  {k}Your Choice Is Invalid {m}|{h} ENTER")

if __name__ == "__main__":
    main()
