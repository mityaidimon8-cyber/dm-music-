# VK Music Mini App for Telegram

Dark Telegram Mini App starter inspired by the supplied GB Music screenshot. It includes a responsive music UI, tabs (My music / Search / Playlists / Settings), a mini-player, favorites, playlists, and a Python Flask backend scaffold.

## Important about VK audio
This repository does **not** bypass VK access controls or scrape private audio endpoints. VK audio search/streaming access depends on VK's current API permissions, user authorization, and applicable terms. The UI runs in demo mode until a permitted VK audio provider is connected in `app.py`.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

## Telegram setup
1. Deploy this app to a public HTTPS host.
2. Create a bot with `@BotFather` and configure its Mini App URL.
3. Set `PUBLIC_BASE_URL` to your deployed URL if needed.
4. Validate Telegram `initData` on the server before trusting user identity. This starter UI does not yet authenticate Telegram users server-side.

## Connect a permitted VK audio provider
Implement the `search_vk_tracks(query)` and `get_stream_url(track_id)` functions in `app.py` using a currently authorized and permitted VK integration. Do not put VK access tokens in frontend JavaScript. Keep secrets in environment variables and never commit `.env`.
