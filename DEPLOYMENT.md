# Render Deployment Configuration

## Services Needed

### Web Service
- **Name**: blood-cancer-detection
- **Environment**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Health Check Path**: `/`

### PostgreSQL Database (Optional)
- **Name**: blood-cancer-db
- **Version**: PostgreSQL 14

## Environment Variables

Set these in your Render dashboard:

```
SECRET_KEY=your-secure-secret-key-here
FLASK_ENV=production
DATABASE_URL=postgresql://user:pass@host:port/dbname
```

## Deployment Steps

1. Connect GitHub repository to Render
2. Create Web Service with Python 3 environment
3. Set environment variables
4. Deploy - Render will automatically detect the Procfile
5. Test the deployed application

## Notes

- The app includes a `Procfile` for Render deployment
- Uses `gunicorn` as production server
- Configured for PostgreSQL in production
- Includes all necessary dependencies in requirements.txt
