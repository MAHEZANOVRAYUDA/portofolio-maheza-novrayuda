# DevOps — CI/CD, Testing, Monitoring

## 1. `build_files.sh` — perbarui untuk mencakup build frontend

Versi saat ini:
```bash
#!/usr/bin/env bash
set -e
pip install -r requirements.txt
python3 manage.py collectstatic --noinput
```

Versi baru (tambah build Tailwind + jalankan check):
```bash
#!/usr/bin/env bash
set -e

echo "==> Install Python dependencies"
pip install -r requirements.txt

echo "==> Install & build frontend assets"
npm install
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify

echo "==> Django system check"
python3 manage.py check --deploy

echo "==> Collect static files"
python3 manage.py collectstatic --noinput
```

## 2. GitHub Actions — CI untuk setiap push/PR

Buat `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        ports: ['5432:5432']
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - name: Run tests
        env:
          SECRET_KEY: dummy-secret-for-ci
          DATABASE_URL: postgres://postgres:postgres@localhost:5432/test_db
        run: python manage.py test

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install ruff
      - run: ruff check .
```

Ini menjamin: **setiap perubahan yang Antigravity buat otomatis dites** sebelum masuk ke `main`, mencegah portofolio "down" karena bug tidak sengaja.

## 3. Migrasi database — solusi untuk keterbatasan serverless

Karena Vercel tidak menjalankan `migrate` otomatis, tambahkan job migrasi terpisah:

**Opsi A (direkomendasikan): jalankan manual sekali per perubahan model**
```bash
# dari local, dengan DATABASE_URL production di .env
python manage.py migrate
```

**Opsi B (otomatis via GitHub Actions saat merge ke main):**
```yaml
  migrate:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -r requirements.txt
      - run: python manage.py migrate
        env:
          SECRET_KEY: ${{ secrets.SECRET_KEY }}
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
```
Simpan `SECRET_KEY` dan `DATABASE_URL` production sebagai **GitHub Secrets** (Settings → Secrets and variables → Actions), jangan pernah commit ke repo.

## 4. Monitoring & error tracking

Untuk portofolio personal, cukup pakai tier gratis:
- **Sentry** (free tier) — tambahkan `sentry-sdk` untuk menangkap error production otomatis, dapat notifikasi email kalau ada 500 error.
  ```python
  import sentry_sdk
  sentry_sdk.init(dsn=config('SENTRY_DSN', default=''), traces_sample_rate=0.1)
  ```
- **Vercel Analytics** (built-in, gratis untuk hobby plan) — untuk lihat traffic & Core Web Vitals langsung dari dashboard Vercel.
- **UptimeRobot** (free tier) — ping situs tiap 5 menit, kirim email/telegram kalau situs down. Bonus: bisa sekaligus jadi "keep-alive" untuk mitigasi cold start (lihat `05-system-design.md`).

## 5. Branching strategy sederhana

Untuk proyek 1 orang, tidak perlu Gitflow rumit:
```
main        → selalu deployable, auto-deploy ke production (Vercel)
feature/*   → branch kerja, PR ke main setelah CI hijau
```
Vercel otomatis membuat **Preview Deployment** untuk tiap PR — manfaatkan ini untuk review visual sebelum merge (link preview otomatis muncul di komentar PR GitHub).
