#!/bin/bash
# rollback.sh – Aktiviert das zuletzt funktionierende Docker-Image
set -e

cd /opt/insolvenz-manager

echo "[rollback] Starte Rollback..."

# Letztes bekannt-gutes Image aus docker-compose history
PREVIOUS_IMAGE=$(docker image ls ghcr.io/vizzi93/insolvenz-api --format "{{.Tag}}" | grep -v latest | sed -n '2p')

if [ -z "$PREVIOUS_IMAGE" ]; then
    echo "[rollback] FEHLER: Kein vorheriges Image gefunden!"
    exit 1
fi

echo "[rollback] Wechsle auf Image: ${PREVIOUS_IMAGE}"
export IMAGE_TAG="$PREVIOUS_IMAGE"

docker compose -f docker-compose.prod.yml up -d --no-deps api worker

echo "[rollback] Abgeschlossen. Bitte manuell prüfen!"
