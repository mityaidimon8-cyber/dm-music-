import os
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Demo catalog. Replace this with results from a permitted VK Music integration.
DEMO_TRACKS = [
    {"id": "demo-1", "title": "Ночной город", "artist": "Demo Artist", "duration": 192, "album": "Демо-альбом", "cover": "", "streamUrl": "", "source": "demo"},
    {"id": "demo-2", "title": "На повторе", "artist": "Demo Artist & Friends", "duration": 211, "album": "Синглы", "cover": "", "streamUrl": "", "source": "demo"},
    {"id": "demo-3", "title": "После полуночи", "artist": "Demo Artist", "duration": 174, "album": "Демо-альбом", "cover": "", "streamUrl": "", "source": "demo"},
]

def search_vk_tracks(query: str):
    """TODO: Connect a VK audio provider that you are authorized to use.

    Return normalized track objects with id, title, artist, duration, cover, and
    streamUrl (only when the provider is permitted to expose a playable URL).
    Do not scrape private endpoints or attempt to bypass access controls.
    """
    q = query.casefold().strip()
    if not q:
        return DEMO_TRACKS
    return [t for t in DEMO_TRACKS if q in t["title"].casefold() or q in t["artist"].casefold()]

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/search")
def api_search():
    query = request.args.get("q", "")[:200]
    return jsonify({"tracks": search_vk_tracks(query), "mode": "demo", "message": "Демо-каталог. Подключите разрешённый источник VK Music в app.py."})

@app.get("/api/health")
def health():
    return jsonify({"ok": True, "mode": "demo"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=os.getenv("FLASK_DEBUG") == "1")
