# Weather Project

## Description

A simple weather application built with Django that fetches and displays weather data from the OpenWeatherMap API.

## Setup

1.  **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd weather_project
   ```

2.  **Create a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate   # On macOS and Linux
   ```

3.  **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4.  **Set up environment variables:**
   -   Create a `.env` file in the project root.
   -   Add your OpenWeatherMap API key:
       ```
       OPENWEATHERMAP_API_KEY=YOUR_API_KEY
       ```

5.  **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6.  **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7.  **Access the application:**
   -   Open your web browser and go to `http://localhost:8000/weather/`.

## Configuration

-   **OpenWeatherMap API Key:**
    -   Sign up for an account at [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
    -   Set the `OPENWEATHERMAP_API_KEY` environment variable in the `.env` file.

## Dependencies

-   Django
-   requests
-   python-dotenv

## Project Structure

```
weather_project/
├── db.sqlite3
├── manage.py
├── static/
│   └── style.css
├── weather_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── weatherapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── templates/
    │   └── weatherapp/
    │       └── index.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Contributing

-   Feel free to contribute to the project by submitting pull requests.

## License

-   This project is licensed under the [MIT License](LICENSE).