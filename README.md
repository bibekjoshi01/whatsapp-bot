# WhatsApp Bot + Automation API

A small monorepo containing two complementary apps:

- A Node.js WhatsApp bot (TypeScript) for handling chat interactions and automations.
- A FastAPI-based automation service that runs browser-driven tasks (Meroshare integration, session management, etc.).

## Key Features

- Conversational WhatsApp bot with configurable intents and memory.
- Automation API to programmatically drive browser tasks and persist sessions.
- Clear separation of runtimes so services can be deployed independently.

## Repository layout

```
.
├── src/                  # Node bot source (TypeScript)
├── automation_api/       # FastAPI automation service
├── package.json
├── tsconfig.json
├── requirements.txt
└── .env.example
```

## Quick Start

You can run the Node bot and the FastAPI automation service independently. Below are minimal steps to get both running locally.

### Node bot (Quick)

1. Install dependencies:

```bash
npm install
```

2. Create environment file and start:

```bash
cp .env.example .env
npm start
```

Optional (PM2 deployment):

```bash
npm run build
npm install -g pm2
pm2 start ecosystem.config.json
pm2 logs whatsapp-bot
pm2 save
pm2 startup
```

### FastAPI automation (Quick)

1. Create & activate a virtualenv, install deps:

```bash
cd automation_api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
cp .env.example .env
```

2. Run the service:

```bash
python run.py
```

Health check:

```bash
curl http://localhost:8000/health
```

Trigger example (Meroshare login):

```bash
curl -X POST http://localhost:8000/trigger/login \
  -H "Content-Type: application/json" \
  -d '{"save_session": true, "state_path": "state.json"}'
```

## Environment

- Copy the appropriate `.env.example` to `.env` in each service before running.

## Development notes

- Node sources live in `src/` and are written in TypeScript. Use `npm run build` to compile.
- The automation API lives in `automation_api/` and exposes typed endpoints under `api/routes/`.

## Contributing

Contributions are welcome. Open an issue or submit a PR with a clear description of your change.

## License

This project does not include a license file. Add one if you plan to publish or share the code widely.

