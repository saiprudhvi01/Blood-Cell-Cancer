# Render Deployment Configuration

## Services Needed

### Web Service
- **Name**: blood-cancer-detection
- **Environment**: Python 3.11.7
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python start.py`
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
PYTHONUNBUFFERED=1
TF_CPP_MIN_LOG_LEVEL=2
```

## Deployment Steps

1. Connect GitHub repository to Render
2. Create Web Service with Python 3.11.7 environment
3. Set environment variables
4. Deploy - Render will automatically detect the Procfile
5. Test the deployed application

## Important Notes

- Uses Python 3.11.7 for maximum compatibility
- TensorFlow 2.13.x with CPU-only support
- Includes fallback handling for TensorFlow import issues
- Uses custom start.py script for better error handling
- All dependencies use version ranges for flexibility
- Pillow 10.x for Python 3.11 compatibility

## Troubleshooting

If TensorFlow fails to install:
1. Check the build logs
2. The start.py script includes fallback installation
3. TensorFlow CPU-only version is used for Render compatibility

If Pillow fails to install:
1. Python 3.11.7 is used for better Pillow compatibility
2. Pillow 10.x supports Python 3.11
3. Version ranges allow for compatible updates
