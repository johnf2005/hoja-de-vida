# Hoja de Vida Virtual - Deploy Instructions

## Render Deployment Configuration

### Critical: Manual Steps Required in Render Dashboard

**BEFORE deploying, you MUST set these Environment Variables in Render:**

1. Go to your service `hoja-de-vida` on render.com
2. Click `Environment` in the sidebar
3. Add these variables:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | `g!elTrW(mLW6Z)Pa08T+BCh#fuBFsf&b(PAbS=u15LN2wggwE)` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `hoja-de-vida-kmlp.onrender.com` |
| `DATABASE_URL` | Your PostgreSQL connection string |

4. **IMPORTANT**: Clear the Build and Start Commands in Settings → Build & Deploy
   - Build Command: (leave empty)
   - Start Command: (leave empty)

This allows Render to read the `Procfile` configuration.

### Configuration Files

- **Procfile**: Specifies how to start the application with Gunicorn
- **render.yaml**: Alternative configuration (currently using Procfile as primary)
- **requirements.txt**: Python dependencies
- **runtime.txt**: Python version (3.13.4)

### Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
cd mi_proyecto
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run development server
python manage.py runserver
```

### Production Deployment

After pushing to GitHub:

1. Verify environment variables are set in Render Dashboard
2. Clear Build/Start Commands in Settings
3. Go to Deploys → Redeploy

The application should deploy successfully using the `Procfile` configuration.

---

**Last Updated**: February 1, 2026
