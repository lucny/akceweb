# Akční web (Django)

Jednoduchá webová aplikace v Django pro správu kulturních akcí.

## Rychlý start

Pokud chceš aplikaci jen rychle spustit lokálně:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Pak otevři: http://127.0.0.1:8000/

Obsahuje:
- veřejnou úvodní stránku,
- seznam a detail akcí,
- jednoduché CRUD formuláře (vložit, upravit, smazat),
- ošetření přístupu podle přihlášení, oprávnění a autora záznamu.

## Technologie

- Python 3.12+
- Django 6.0.3
- SQLite (výchozí databáze)
- Bootstrap (statické soubory v aplikaci)

## Struktura projektu

- `akceweb/` – konfigurace projektu (settings, root URL, WSGI/ASGI)
- `akce/` – hlavní aplikace
  - `models.py` – model `Akce`
  - `views.py` – funkční i třídní view včetně CRUD
  - `forms.py` – `ModelForm` pro akce
  - `templates/` – šablony seznamu, detailu, formuláře a smazání
  - `urls.py` – routy aplikace
- `manage.py` – Django management vstup
- `requirements.txt` – Python závislosti

## Model `Akce`

Pole modelu:
- `nazev` (CharField)
- `datum` (DateField)
- `popis` (TextField)
- `kategorie` (výběr: divadlo, hudba, kino, výstava)
- `hodnoceni` (FloatField, validace 1.0–5.0)
- `autor` (ForeignKey na `User`)
- `upraveno` (DateTime, auto_now)

Řazení je nastaveno v `Meta.ordering` podle data sestupně.

## Instalace a spuštění

### 1) Klon a vstup do adresáře

```bash
git clone <repo-url>
cd akceweb
```

### 2) Vytvoření a aktivace virtuálního prostředí

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3) Instalace závislostí

```bash
pip install -r requirements.txt
```

### 4) Migrace databáze

```bash
python manage.py migrate
```

### 5) Vytvoření administrátora

```bash
python manage.py createsuperuser
```

### 6) Spuštění vývojového serveru

```bash
python manage.py runserver
```

Aplikace poběží na adrese:
- http://127.0.0.1:8000/
- root URL přesměrovává na `/akce/`

## URL přehled

Root URL:
- `/` → přesměrování na `/akce/`
- `/admin/` → Django admin

Aplikace `akce`:
- `/akce/` – úvodní stránka
- `/akce/list/` – seznam akcí
- `/akce/detail/<id>/` – detail akce
- `/akce/create/` – vložení nové akce
- `/akce/detail/<id>/update/` – úprava akce
- `/akce/detail/<id>/delete/` – smazání akce

## Oprávnění a práva uživatelů

Aplikace využívá Django autentizaci + model permissions.

### Přístupová pravidla

- Seznam akcí (`/akce/list/`) vyžaduje přihlášení.
- Detail akce vyžaduje permission `akce.view_akce`.
- Vložení nové akce vyžaduje permission `akce.add_akce`.
- Úprava akce vyžaduje:
  - permission `akce.change_akce` a zároveň
  - uživatel je autor akce **nebo** superuser.
- Smazání akce vyžaduje:
  - permission `akce.delete_akce` a zároveň
  - uživatel je autor akce **nebo** superuser.

Při vytvoření akce se pole `autor` nastaví automaticky na přihlášeného uživatele.

### Přihlášení

V navigaci jsou odkazy:
- `Přihlásit` (admin login)
- `Odhlásit`

Po přihlášení se zobrazí uživatelské jméno a akce dle oprávnění.

## Přidělení oprávnění uživatelům

Nejjednodušeji přes Django admin:
1. Přihlásit se na `/admin/`.
2. Otevřít uživatele nebo skupiny.
3. Přidat oprávnění:
   - `akce | akce | Can view akce`
   - `akce | akce | Can add akce`
   - `akce | akce | Can change akce`
   - `akce | akce | Can delete akce`

## Vývoj a kontrola projektu

Základní kontrola konfigurace:

```bash
python manage.py check
```

Spuštění testů:

```bash
python manage.py test
```

## Poznámky

- Projekt používá SQLite (`db.sqlite3`) pro jednoduchý lokální vývoj.
- Soubor `.gitignore` je nastaven tak, aby se necommitovalo virtuální prostředí, lokální DB, cache a IDE metadata.
- Pro produkční nasazení je nutné změnit `DEBUG`, `ALLOWED_HOSTS`, `SECRET_KEY` a nastavit bezpečné ukládání statických souborů.
