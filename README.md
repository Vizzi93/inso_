# PrivatInsolvenz-Manager

Digitale Begleitung des deutschen Verbraucherinsolvenzverfahrens (§§ 304 ff. InsO).

> **Hinweis:** Diese Software ersetzt keine Rechtsberatung. Alle Entscheidungen sind mit einer qualifizierten Beratungsstelle abzustimmen.

## Phasen

| Phase | Bezeichnung | Status |
|-------|-------------|--------|
| 0 | Vorprüfung & Onboarding | 🚧 In Entwicklung |
| 1 | Außergerichtlicher Einigungsversuch | ⏳ Geplant |
| 2 | Gerichtlicher Schuldenbereinigungsplan | ⏳ Geplant |
| 3 | Eröffnung Insolvenzverfahren | ⏳ Geplant |
| 4 | Wohlverhaltensperiode | ⏳ Geplant |
| 5 | Restschuldbefreiung | ⏳ Geplant |

## Tech Stack

- **Backend:** Python 3.12, FastAPI, SQLAlchemy, Celery
- **Frontend:** React 18, TypeScript, Vite
- **Datenbank:** PostgreSQL 16 + pgcrypto
- **Infrastruktur:** Docker Compose, Nginx, Hetzner Cloud (DE)

## Lokale Entwicklung

```bash
# 1. Repo klonen
git clone https://github.com/Vizzi93/inso_.git
cd inso_

# 2. Secrets anlegen
cp backend/.env.example backend/.env
# .env nach Bedarf befüllen

# 3. Starten
docker compose up --build
```

API erreichbar unter: http://localhost:8000  
API-Docs (Swagger): http://localhost:8000/docs

## DSGVO

Alle personenbezogenen Daten werden ausschließlich auf deutschen Servern verarbeitet.
Siehe `docs/dsgvo-konzept.md` für das vollständige Verarbeitungsverzeichnis (Art. 30 DSGVO).

## Lizenz

Privat – alle Rechte vorbehalten.
