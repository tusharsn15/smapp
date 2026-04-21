# SnapGram - Quick Start Guide

## Installation & Setup (Windows)

### Step 1: Navigate to Project
```cmd
cd "C:\Users\Lenovo\OneDrive\Desktop\2 sem\C\SocialMediaApp"
```

### Step 2: Create Virtual Environment
```cmd
python -m venv venv
```

### Step 3: Activate Virtual Environment
```cmd
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your command prompt.

### Step 4: Install Dependencies
```cmd
pip install -r requirements.txt
```

### Step 5: Run the Application
```cmd
python run.py
```

### Step 6: Access the App
Open your browser and go to: **http://127.0.0.1:5000**

## First Time Setup

1. **Register a new account**
   - Click "Register" on the landing page
   - Enter username, email, and password
   - Create your account

2. **Create a post**
   - Click "New Post" on home
   - Add caption and image URL
   - Use #hashtags for discoverability
   - Click "Post"

3. **Create a story**
   - Click "New Story" on home
   - Add image URL and caption
   - Stories expire in 24 hours

4. **Find and follow users**
   - Go to Explore
   - Click on user profiles
   - Click "Follow" to start following
   - See their posts in your feed

## Features Overview

| Feature | Description |
|---------|------------|
| **Posts** | Share photos with captions & hashtags |
| **Stories** | Share content that disappears in 24 hours |
| **Messages** | Direct chat with other users |
| **Comments** | Comment on posts from others |
| **Likes** | Like posts and engage with content |
| **Follow** | Build your community |
| **Explore** | Discover new content |
| **Search** | Find posts by #hashtags |
| **Notifications** | Get updates on likes, comments, follows |
| **Profiles** | Customize your profile and settings |

## Project Structure

```
SocialMediaApp/
├── app/
│   ├── models/          # Database models (User, Post, Story, etc.)
│   ├── routes/          # Application endpoints/routes
│   ├── static/          # CSS and JavaScript files
│   └── templates/       # HTML templates for each page
├── config.py            # Configuration settings
├── run.py              # Start the application here
├── requirements.txt    # Python dependencies
└── .env               # Environment variables
```

## Troubleshooting

### Port Already in Use
If port 5000 is in use, modify `run.py`:
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```
Then access: http://127.0.0.1:5001

### Module Not Found Error
Ensure virtual environment is activated:
```cmd
venv\Scripts\activate
```

### Database Issues
Delete `app.db` and restart the app to reset database:
```cmd
del app.db
python run.py
```

## Development Tips

1. **Hot Reload**: Changes to templates reload automatically
2. **Debug Mode**: Set `DEBUG=True` in config for detailed error messages
3. **Database**: SQLite file is `app.db` in project root
4. **Uploads**: User files go to `app/static/uploads/`

## Next Steps

- Customize the app with your own branding
- Add more features (filters, effects, live chat)
- Deploy to hosting (Heroku, Railway, etc.)
- Set up proper email system for notifications
- Add image/video upload functionality

## Support

For issues:
1. Check terminal for error messages
2. Ensure all dependencies are installed: `pip install -r requirements.txt`
3. Try deactivating and reactivating the virtual environment
4. Clear browser cache (Ctrl+Shift+Delete)

---

Happy coding! Enjoy building with SnapGram! 🚀
