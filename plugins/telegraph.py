# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for Telegraph commands """

import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from pyAyiin import ayiin, cmdHelp
from pyAyiin.decorator import ayiinCmd
from pyAyiin.utils import eod, eor

from . import cmd


telegraph = Telegraph()
r = telegraph.create_account(short_name="telegraph")
auth_url = r["auth_url"]


@ayiinCmd(pattern="tg (m|t)$")
async def telegraphs(graph):
    """For telegraph command, upload media & text to telegraph site."""
    xxnx = await eor(graph, "**Memproses...**")
    if not graph.text[0].isalpha() and graph.text[0] not in (
            "/", "#", "@", "!"):
        if graph.fwd_from:
            return
        if not os.path.isdir(ayiin.TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(ayiin.TEMP_DOWNLOAD_DIRECTORY)
        if graph.reply_to_msg_id:
            start = datetime.now()
            r_message = await graph.get_reply_message()
            input_str = graph.pattern_match.group(1)
            if input_str == "m":
                downloaded_file_name = await graph.client.download_media(
                    r_message, ayiin.TEMP_DOWNLOAD_DIRECTORY
                )
                end = datetime.now()
                ms = (end - start).seconds
                await xxnx.edit(f"**Di Download Ke** `{downloaded_file_name}` **di** `{ms}` **detik.**"
                )
                if downloaded_file_name.endswith(".webp"):
                    resize_image(downloaded_file_name)
                try:
                    media_urls = upload_file(downloaded_file_name)
                except exceptions.TelegraphException as exc:
                    await xxnx.edit(f"ERROR: {str(exc)}")
                    os.remove(downloaded_file_name)
                else:
                    os.remove(downloaded_file_name)
                    await xxnx.edit(
                        f"**Berhasil diupload ke** [telegra.ph](https://telegra.ph{media_urls[0]})",
                        link_preview=True,
                    )
            elif input_str == "t":
                user_object = await graph.client.get_entity(r_message.sender_id)
                title_of_page = user_object.first_name  # + " " + user_object.last_name
                # apparently, all Users do not have last_name field
                page_content = r_message.message
                if r_message.media:
                    if page_content != "":
                        title_of_page = page_content
                    downloaded_file_name = await graph.client.download_media(
                        r_message, ayiin.TEMP_DOWNLOAD_DIRECTORY
                    )
                    m_list = None
                    with open(downloaded_file_name, "rb") as fd:
                        m_list = fd.readlines()
                    for m in m_list:
                        page_content += m.decode("UTF-8") + "\n"
                    os.remove(downloaded_file_name)
                page_content = page_content.replace("\n", "<br>")
                response = telegraph.create_page(
                    title_of_page, html_content=page_content
                )
                await xxnx.edit(
                    f"**Berhasil diupload ke** [telegra.ph](https://telegra.ph{response['path']})",
                    link_preview=True,
                )
        else:
            await eod(
                xxnx,
                "**Mohon Balas Ke Pesan, Untuk Mendapatkan Link Telegraph Permanen.**"
            )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


cmdHelp.update(
    {
        "telegraph": f"**Plugin : **`telegraph`\
        \n\n  »  **Perintah :** `{cmd}tg` m\
        \n  »  **Kegunaan : **Mengunggah m(Media) Ke Telegraph.\
        \n\n  »  **Perintah :** `{cmd}tg` t\
        \n  »  **Kegunaan : **Mengunggah t(Teks) Ke Telegraph.\
    "
    }
)
