import asyncio
from time import sleep

from pyAyiin import cmdHelp
from pyAyiin.decorator import ayiinCmd
from pyAyiin.utils import eor

from . import cmd


@ayiinCmd(pattern="bulan$")
async def _(event):
    event = await eor(event, "bulan.")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("bulan..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@ayiinCmd(pattern="sayang$")
async def _(event):
    e = await eor(event, "I LOVEE YOUUU 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG KAMU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELAMANYA 💕")
    await e.edit("💘💘💘💘")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("SAYANG KAMU💞")


@ayiinCmd(pattern=r"dino(?: |$)(.*)")
async def _(event):
    typew = await eor(event, "`DIN DINNN.....`")
    sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    sleep(1)
    await typew.edit("`🏃                        🦖`")
    await typew.edit("`🏃                       🦖`")
    await typew.edit("`🏃                      🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃   `LARII`          🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃WOARGH!   🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                    🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃  Huh-Huh           🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃          🦖`")
    await typew.edit("`🏃         🦖`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await typew.edit("`🏃       🦖`")
    await typew.edit("`🏃      🦖`")
    await typew.edit("`🏃     🦖`")
    await typew.edit("`🏃    🦖`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`🧎🦖`")
    sleep(2)
    await typew.edit("`-TAMAT-`")


@ayiinCmd(pattern="gabut$")
async def _(event):
    e = await eor(event, "`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
    await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
    await e.edit("`RAMBUUUT WARNAAA WARNII`")
    await e.edit("`BAGAI GULALI`")
    await e.edit("`IMUUUTTTTT LUCUUU`")
    await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
    await e.edit("`GW GABUUTTTT`")
    await e.edit("`EMMMM BACOTNYA`")
    await e.edit("`GABUTTTT WOI GABUT`")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("`CILUUUKKK BAAAAA`")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🚶                                 🐢")
    await e.edit("`AHHH MANTAP`")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("😂")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("`GABUT`")


@ayiinCmd(pattern=r"terkadang(?: |$)(.*)")
async def _(event):
    typew = await eor(event, "`Terkadang`")
    sleep(1)
    await typew.edit("`Mencintai Seseorang`")
    sleep(1)
    await typew.edit("`Hanya Akan Membuang Waktumu`")
    sleep(1)
    await typew.edit("`Ketika Waktumu Habis`")
    sleep(1)
    await typew.edit("`Tambah Aja 5000`")
    sleep(1)
    await typew.edit("`Bercanda`")


# Create by myself @localheart


@ayiinCmd(pattern=r"mf$")
async def _(event):
    await eor(event, "`mf g dl` **ミ(ノ;_ _)ノ=3** ")


@ayiinCmd(pattern=r"(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "cinta":
        await event.edit(input_str)
        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Target Cinta`",
            "`Mengirim Cintaku.. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 84%\n█████████████████████▒▒▒▒ `",
            "`Mengirim Cintaku.. 100%\n█████████CINTAKU███████████ `",
            "`Cintaku Sekarang Sepenuhnya Terkirim Padamu, Dan Sekarang Aku Sangat Mencintai Mu, I Love You 💞`",
        ]
        animation_interval = 2
        animation_ttl = range(11)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@ayiinCmd(pattern=r"gombal(?: |$)(.*)")
async def _(event):
    typew = eor(event, "`Hai, I LOVE YOU 💞`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH!`")
    sleep(1)
    await typew.edit("`I NEED YOU!`")
    sleep(1)
    await typew.edit("`I WANT TO BE YOUR BOYFRIEND!`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💕💗`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💗💞`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💝💗`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💟💖`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💘💓`")
    sleep(1)
    await typew.edit("`Tapi Bo'ong`")


# Create by myself @localheart


@ayiinCmd(pattern="helikopter(?: |$)(.*)")
async def _(event):
    await eor(
        event,
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Semuanya :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n",
    )


@ayiinCmd(pattern="tembak(?: |$)(.*)")
async def _(event):
    await eor(
        event,
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉\n" r"_/﹋\_" "\n**Mau Jadi Pacarku Gak?!**",
    )


@ayiinCmd(pattern="bundir(?: |$)(.*)")
async def _(event):
    await eor(
        event,
        "`Dadah Semuanya...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


@ayiinCmd(pattern="awk(?: |$)(.*)")
async def _(event):
    await eor(
        event,
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`",
    )


@ayiinCmd(pattern="ular(?: |$)(.*)")
async def _(event):
    await eor(
        event,
        "░░░░▓\n"
        "░░░▓▓\n"
        "░░█▓▓█\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓███\n"
        "░░░░██▓▓████\n"
        "░░░░░██▓▓█████\n"
        "░░░░░░██▓▓██████\n"
        "░░░░░░███▓▓███████\n"
        "░░░░░████▓▓████████\n"
        "░░░░█████▓▓█████████\n"
        "░░░█████░░░█████●███\n"
        "░░████░░░░░░░███████\n"
        "░░███░░░░░░░░░██████\n"
        "░░██░░░░░░░░░░░████\n"
        "░░░░░░░░░░░░░░░░███\n"
        "░░░░░░░░░░░░░░░░░░░\n",
    )


@ayiinCmd(pattern="y(?: |$)(.*)")
async def _(event):
    await eor(
        event,
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    )


@ayiinCmd(pattern="tank(?: |$)(.*)")
async def _(event):
    await eor(
        event,
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n",
    )


@ayiinCmd(pattern="babi(?: |$)(.*)")
async def _(event):
    await eor(
        event,
        "┈┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n",
    )


@ayiinCmd(pattern="ajg(?: |$)(.*)")
async def _(event):
    await eor(
        event,
        "╥━━━━━━━━╭━━╮━━┳\n"
        "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
        "╨━━┗┛┗┛━━┗┛┗┛━━┻\n",
    )


@ayiinCmd(pattern=r"bernyanyi(?: |$)(.*)")
async def _(event):
    typew = await eor(event, "**Ganteng Doang Gak Bernyanyi (ง˙o˙)ว**")
    sleep(2)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")


@ayiinCmd(pattern="santet(?: |$)(.*)")
async def _(event):
    typew = await eor(event, "`Mengaktifkan Perintah Santet Online....`")
    sleep(2)
    await typew.edit("`Mencari Nama Orang Ini...`")
    sleep(1)
    await typew.edit("`Santet Online Segera Dilakukan`")
    sleep(1)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   ▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    sleep(1)
    await typew.edit("`Target Berhasil Tersantet Online 🥴`")


cmdHelp.update(
    {
        "animasi": f"**Plugin :** `animasi`\
        \n\n  »  **Perintah : **`{cmd}gabut` | `{cmd}dino`\
        \n  »  **Kegunaan :** ntahlah gabut doang.\
        \n\n  »  **Perintah : **`{cmd}gombal`\
        \n  »  **Kegunaan :** buat bercanda.\
        \n\n  »  **Perintah : ** `{cmd}cinta`\
        \n  »  **Kegunaan :** mengirim cintamu ke seseorang.\
        \n\n  »  **Perintah : **`{cmd}sayang`\
        \n  »  **Kegunaan :** untuk jadi buaya.\
        \n\n  »  **Perintah : **`{cmd}terkadang`\
        \n  »  **Kegunaan :** Auk dah iseng doang.\
        \n\n  »  **Perintah : **`{cmd}helikopter` | `{cmd}tank` | `{cmd}tembak` | `{cmd}bundir`\
        \n  »  **Kegunaan :** liat sendiri.\
        \n\n  »  **Perintah : **`{cmd}y`\
        \n  »  **Kegunaan :** jempol\
        \n\n  »  **Perintah : **`{cmd}bulan` | `{cmd}hati` | `{cmd}bernyanyi`\
        \n  »  **Kegunaan :** liat aja.\
        \n\n  »  **Perintah : **`{cmd}awk`\
        \n  »  **Kegunaan :** ketawa lari.\
        \n\n  »  **Perintah : **`{cmd}lar` | `{cmd}abi` | `{cmd}ajg`\
        \n  »  **Kegunaan :** liat sendiri.\
        \n\n  »  **Perintah : **`{cmd}bunga` | `{cmd}buah`\
        \n  »  **Kegunaan :** animasi.\
        \n\n  »  **Perintah : **`{cmd}waktu`\
        \n  »  **Kegunaan :** animasi.\
        \n\n  »  **Perintah : **`{cmd}santet`\
        \n  »  **Kegunaan :** Santet Online Buat Bercanda.\
    "
    }
)
