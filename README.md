# WhatsApp Bot

A WhatsApp auto-reply bot built with `whatsapp-web.js`. It supports rule-based intent replies, simple conversation memory, and a plug-in point for AI responses.

## Requirements
- Node.js 18+
- A VPS or machine with a GUI or headless Chromium environment for WhatsApp Web

## Install
```bash
npm install
```

## Configure
Create `.env` using the template:
```bash
cp .env.example .env
```

Edit `.env` with your business details.

## Build and run locally
```bash
npm start
```

## Run with PM2 (VPS)
```bash
npm install -g pm2
npm run build
pm2 start ecosystem.config.json
pm2 logs whatsapp-bot
pm2 save
pm2 startup
```

## Owner Commands (from your own WhatsApp)
- `!bot on`
- `!bot off`
- `!bot status`

## Notes
- WhatsApp Web requires scanning a QR code the first time.
- Auth session is stored in `.wwebjs_auth` and cached in `.wwebjs_cache`.
- Conversation memory is in-memory only. For persistence, add Redis/SQLite.


<!-- suvani suvani <3 -->
Denish Dhakal
aakash suwal dskdsadasdasdasdada
Shekhar Rawal
Sakshi

- Udesh-Regmi
