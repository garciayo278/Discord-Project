# Discord-Like Project with Django

## Description

This project is a Discord-like web application built using the Django framework. It aims to provide a platform for real-time communication, allowing users to create and join channels, send messages, and interact with other users in a chat-like interface.

## Features

- **User Authentication:** Secure login and registration system.
- **Channels:** Users can create, join, and manage channels for group discussions.
- **Real-Time Messaging:** Users can send and receive messages in real time.
- **User Profiles:** Customizable user profiles with avatars and personal information.

## Technologies Used

- Django: Backend framework for handling server-side logic, database interactions, and routing.
- Channels: Django library for handling WebSockets and real-time features.
- Redis: In-memory data store used as a message broker for real-time messaging.
- HTML/CSS/JavaScript: Frontend technologies for building the user interface.

## Live Site

The project is deployed and can be accessed at [Carrier Navigator](https://carriernavigator.com).

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
git clone https://github.com/yourusername/discord-like-project.git
2. Navigate to the project directory:
cd discord-like-project
3. Install dependencies:
pip install -r requirements.txt
4. Migrate the database:
python manage.py migrate
5. Run the server:
python manage.py runserver

## Usage

Once the server is running, you can access the application at `http://localhost:8000`. Register for an account or log in to start using the chat features.

## Contributing

This project is open for contributions. If you have any ideas or suggestions, feel free to fork the repository and submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
