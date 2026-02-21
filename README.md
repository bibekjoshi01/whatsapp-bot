# WhatsApp Bot + Automation API

This repo now has two separated apps:
- Node.js WhatsApp bot (chat interaction)
- FastAPI automation service (browser/API triggers)

## Folder structure
```text
.
├── src/                       # Node bot source (TypeScript)
├── automation_api/
│   ├── app/
│   │   ├── api/routes/        # FastAPI routes
│   │   ├── core/              # env/config helpers
│   │   ├── schemas/           # request/response models
│   │   └── services/          # automation services (Meroshare, etc.)
│   ├── .env.example
│   ├── requirements.txt
│   └── run.py
├── package.json               # Node bot package
├── tsconfig.json
└── .env.example               # Node bot env template
```

## Node bot (separate runtime)
### Setup
```bash
npm install
cp .env.example .env
```

### Run
```bash
npm start
```

### PM2
```bash
npm install -g pm2
npm run build
pm2 start ecosystem.config.json
pm2 logs whatsapp-bot
pm2 save
pm2 startup
```

## FastAPI automation (separate runtime)
`FastAPI` is preferable over Flask here because your use case is API triggers and FastAPI provides typed validation and cleaner API contracts by default.

### Setup
```bash
cd automation_api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
cp .env.example .env
```

### Run
```bash
cd automation_api
python run.py
```

### Trigger Meroshare login
```bash
curl -X POST http://localhost:8000/trigger/login \
  -H "Content-Type: application/json" \
  -d '{"save_session": true, "state_path": "state.json"}'
```

### Health check
```bash
curl http://localhost:8000/health
```
