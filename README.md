# SnapGram - Instagram + Snapchat Social Media App

A full-featured social media web application combining the best features of Instagram and Snapchat with additional modern features.

## Features

### Core Features
- **User Authentication**: Secure registration and login system
- **User Profiles**: Customizable profiles with bio, follower/following counts
- **Posts**: Create, delete, and share posts with images and captions
- **Stories**: Share disappearing stories (expire after 24 hours)
- **Direct Messaging**: Private chat between users
- **Comments**: Comment on posts from other users
- **Likes**: Like posts and see like counts
- **Notifications**: Real-time notifications for likes, comments, and follows

### Advanced Features
- **Follow/Unfollow**: Build your community
- **Hashtags**: Search posts by hashtags (#)
- **Feed**: Personalized feed showing posts from followed users
- **Explore**: Discover new content from all users
- **Private Accounts**: Option to make account private
- **Search**: Search for users and hashtags

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (Flask-SQLAlchemy)
- **Authentication**: Flask-Login
- **Frontend**: HTML, CSS, JavaScript
- **ORM**: SQLAlchemy

## Installation

1. **Clone/Navigate to the project**:
   ```bash
   cd SocialMediaApp
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5000`

## Project Structure

```
SocialMediaApp/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # User model with followers
│   │   ├── post.py          # Post, Like, Comment models
│   │   ├── story.py         # Story model (24h expiry)
│   │   ├── message.py       # Direct message model
│   │   └── notification.py  # Notification model
│   ├── routes/
│   │   ├── auth.py          # Login/Register endpoints
│   │   ├── main.py          # Home/Explore endpoints
│   │   ├── posts.py         # Post CRUD endpoints
│   │   ├── stories.py       # Story endpoints
│   │   ├── messages.py      # Messaging endpoints
│   │   └── profile.py       # Profile endpoints
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # Main stylesheet
│   │   ├── js/
│   │   │   └── main.js      # Frontend JavaScript
│   │   └── uploads/         # User-uploaded files
│   └── templates/
│       ├── base.html        # Base template
│       ├── index.html       # Landing page
│       ├── auth/            # Login/Register templates
│       ├── main/            # Home/Explore templates
│       ├── posts/           # Post templates
│       ├── stories/         # Story templates
│       ├── messages/        # Messaging templates
│       └── profile/         # Profile templates
├── config.py                # Configuration file
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── README.md               # This file
```

## Usage

### User Registration
1. Click "Register" on the landing page
2. Enter username, email, and password
3. Confirm your password and register
4. Log in with your credentials

### Creating Posts
1. Click "New Post" from the home page
2. Add your caption and optional image URL
3. Use #hashtags in your caption for discoverability
4. Click "Post" to share

### Sharing Stories
1. Click "New Story" from the home page
2. Add an image URL and optional caption
3. Post the story (expires in 24 hours)

### Direct Messaging
1. Go to Messages section
2. Click "New Message" to find users
3. Select a user and start chatting
4. Messages are saved in your conversation history

### Following Users
1. Visit a user's profile
2. Click "Follow" to start following them
3. See their posts in your feed
4. Click "Following" to unfollow

### Discovering Content
- **Explore**: Browse all posts from any user
- **Search**: Search for posts using hashtags (#hashtag) or user mentions
- **Notifications**: See who liked, commented, or followed you

## API Endpoints

### Authentication
- `GET/POST /auth/register` - User registration
- `GET/POST /auth/login` - User login
- `GET /auth/logout` - User logout

### Posts
- `GET/POST /posts/create` - Create post
- `POST /posts/<id>/like` - Like a post
- `POST /posts/<id>/comment` - Comment on post
- `POST /posts/<id>/delete` - Delete post
- `GET /posts/search` - Search posts

### Stories
- `GET/POST /stories/create` - Create story
- `GET /stories/<user_id>` - View user stories
- `GET /stories/all` - View all stories from followed users

### Messages
- `GET /messages/` - View inbox
- `GET /messages/conversation/<user_id>` - View conversation
- `POST /messages/send/<user_id>` - Send message

### Profile
- `GET /profile/<username>` - View profile
- `GET/POST /profile/edit` - Edit profile
- `POST /profile/<username>/follow` - Follow user
- `POST /profile/<username>/unfollow` - Unfollow user
- `GET /profile/notifications` - View notifications

## Database Models

### User
- username, email, password hash
- bio, profile picture, privacy setting
- relationships: posts, stories, messages, followers, following

### Post
- content, image URL, video URL
- author, timestamps
- relationships: comments, likes

### Comment
- content, author, post reference
- timestamp

### Like
- user, post reference
- timestamp

### Story
- image/video URL, caption
- author, expiry timestamp
- 24-hour auto-expiry

### Message
- sender, receiver, content
- read status, timestamp

### Notification
- user, type (like/comment/follow), content
- related user/post reference

## Future Enhancements

- [ ] Real-time notifications with WebSockets
- [ ] Video uploads and processing
- [ ] Advanced filters and effects
- [ ] Story polls and questions
- [ ] Live streaming
- [ ] Payment integration for features
- [ ] Email verification
- [ ] Two-factor authentication
- [ ] Post scheduling
- [ ] Analytics dashboard
- [ ] Mobile app (React Native)

## Security Considerations

- Passwords hashed with Werkzeug
- CSRF protection with Flask-WTF
- SQL injection prevention with SQLAlchemy ORM
- XSS protection in templates
- Input validation on all forms

## Configuration

Edit `.env` file for environment variables:
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

## License

MIT License - Feel free to use this project for learning and personal use.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Support

For issues and questions, please open an issue in the repository.

---

Made with ❤️ by SnapGram Team
