cd C:\Users\Doja\Desktop\Dojaflow\inso

# .env ALLOWED_ORIGINS korrigieren (in der .env diese Zeile setzen/ersetzen):
# ALLOWED_ORIGINS=["http://localhost:3000","http://localhost"]

git add backend/app/core/config.py
git commit -m "fix: allowed_origins als list[str] mit Default-Werten"
git push

# Neu starten
docker-compose down
docker-compose up -d

# Nach 15 Sekunden testen
Start-Sleep 15
Invoke-WebRequest http://localhost/api/health | Select-Object -ExpandProperty Content