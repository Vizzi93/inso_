# DSGVO-Konzept (Art. 30 DSGVO – Verzeichnis der Verarbeitungstätigkeiten)

> Stand: 2026 | Verantwortlicher: [NAME EINTRAGEN] | Datenschutzbeauftragter: [FALLS PFLICHT]

---

## 1. Verarbeitete Datenkategorien

| Kategorie | Beispiele | Rechtsgrundlage |
|-----------|-----------|-----------------|
| Stammdaten | Name, Adresse, Geburtsdatum | Art. 6 Abs. 1 lit. b DSGVO (Vertragserfüllung) |
| Finanzdaten | Schulden, Einkommen, Vermögen | Art. 6 Abs. 1 lit. b DSGVO |
| Gläubigerdaten | Name, Forderungshöhe, Kontakt | Art. 6 Abs. 1 lit. b DSGVO |
| Verfahrensdaten | Phasenstatus, Fristen, Beschlüsse | Art. 6 Abs. 1 lit. c DSGVO (rechtliche Pflicht) |
| Kommunikation | E-Mails, Schreiben | Art. 6 Abs. 1 lit. b DSGVO |

## 2. Speicherung & Verschlüsselung

- **Ort:** Hetzner Cloud, Rechenzentrum Deutschland (Nürnberg/Falkenstein)
- **Datenbank:** PostgreSQL mit Feldebeneverschlüsselung (pgcrypto, AES-256)
- **Dokumente:** MinIO, AES-256 Verschlüsselung at-rest
- **Transport:** TLS 1.3 ausschließlich

## 3. Aufbewahrungsfristen

| Datenart | Frist | Grundlage |
|----------|-------|-----------|
| Aktive Verfahrensdaten | Während Verfahren + 1 Jahr | Betrieblich |
| Abgeschlossene Verfahren | 10 Jahre | § 147 AO |
| Audit-Logs | 10 Jahre | § 147 AO |
| E-Mail-Logs | 6 Monate | Betrieblich |

## 4. Betroffenenrechte (Art. 15–22 DSGVO)

- **Auskunft (Art. 15):** Datenexport-Funktion geplant
- **Löschung (Art. 17):** Eingeschränkt durch Aufbewahrungspflichten (§ 147 AO)
- **Einschränkung (Art. 18):** Daten werden eingefroren (kein Zugriff, keine Löschung)
- **Portabilität (Art. 20):** JSON/CSV-Export geplant

## 5. Auftragsverarbeiter

| Anbieter | Leistung | AV-Vertrag |
|----------|----------|------------|
| Hetzner Online GmbH | Hosting | Vorhanden |
| [E-Mail-Provider] | SMTP | Eintragen |

## 6. Technische & Organisatorische Maßnahmen (TOMs)

- [ ] Zugangskontrolle: MFA für alle Admin-Zugänge
- [ ] Zugriffskontrolle: RBAC (Schuldner sieht nur eigene Daten)
- [ ] Trennungskontrolle: Row-Level Security in PostgreSQL
- [ ] Verschlüsselung at-rest: AES-256 (DB + Dokumentenspeicher)
- [ ] Verschlüsselung in transit: TLS 1.3
- [ ] Audit-Log: Unveränderliches Event-Log aller Datenänderungen
- [ ] Backup: Täglich, verschlüsselt, offsite
- [ ] Penetrationstest: [Termin eintragen]
