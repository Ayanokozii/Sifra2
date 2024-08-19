import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from Sifra import app
import yt_dlp  # Ensure yt-dlp is imported

# ------------------------------------------------------------------------------- #
#                           INSTAGRAM REELS LELO SAB                              #
# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["ig"], prefixes=["/", "!", "."]))
async def download_instareels(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a link to download the reel.")
        return

    reel_url = message.command[1]

    if not reel_url.startswith("https://www.instagram.com/reel/"):
        await message.reply_text("Please provide a valid Instagram reel link.")
        return

    try:
        # Use yt-dlp to extract the video URL
        ydl_opts = {'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(reel_url, download=False)
            video_url = info_dict.get("url")
            
            if video_url:
                await message.reply_video(video_url)
            else:
                await message.reply_text("Unable to extract the video URL from the provided link.")
    except Exception as e:
        print(f"Failed to download reel: {e}")
        await message.reply_text("Failed to download the reel. Please try again later.")

@app.on_message(filters.command(["reel"], prefixes=["/", "!", "."]))
async def instagram_reel(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply("Please provide a valid Instagram URL using the /reel command.")
        return

    url = message.command[1]
    
    try:
        response = requests.post(f"https://lexica-api.vercel.app/download/instagram?url={url}")
        data = response.json()

        if data.get('code') == 2:
            media_urls = data['content'].get('mediaUrls', [])
            if media_urls:
                video_url = media_urls[0].get('url')
                if video_url:
                    await message.reply_video(video_url)
                else:
                    await message.reply("No video found in the response. The account may be private.")
            else:
                await message.reply("No media found in the response. The account may be private.")
        else:
            await message.reply("The request was not successful.")
    except Exception as e:
        print(f"Failed to fetch reel: {e}")
        await message.reply("An error occurred while trying to fetch the reel. Please try again later.")
