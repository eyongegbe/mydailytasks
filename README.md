# Daily Tasks Web Application

The Daily Tasks web application is a Django-based application that allows users to manage their daily tasks. Users can create tasks, mark them as completed, view their current and completed tasks, and edit or delete tasks.

## Installation

To run the Daily Tasks web application, follow the steps below:

1. Clone the repository:
   ```bash
   git clone <https://github.com/eyongegbe/mydailytasks.git>
   ```
   
2. Navigate to the project directory:
   ```bash
   cd mydailytasks
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - For macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Set up the database:
   ```bash
   python manage.py migrate
   ```

7. Create a superuser (admin) account (optional):
   ```bash
   python manage.py createsuperuser
   ```

## Usage

To run the Daily Tasks web application, execute the following command:

```bash
python manage.py runserver
```

Once the server is running, open your web browser and navigate to `http://localhost:8000` to access the application.

## Features

- **User Registration**: Users can sign up for a new account to access the application.
- **User Authentication**: Users can log in and log out of their accounts.
- **Task Management**: Users can create new tasks, mark tasks as completed, view their current, edit tasks, and delete tasks.

## Technologies Used

- Django
- HTML/CSS
- JavaScript

## Contributing

Contributions to the Daily Tasks web application are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit your code.
4. Push the changes to your fork.
5. Submit a pull request describing your changes.

## License

The Daily Tasks web application is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

