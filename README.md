# DevHub: Developer Portfolio Visualizer

A Flask-based web application that provides developers with a visually appealing way to showcase their activity and contributions across various platforms.

Current Platforms Supported:
* GitHub

Planned Integrations (Future Releases):
* Stack Overflow
* X (social media)

**Features (Planned):**

- **Interactive Visualizations:** See your contributions and coding journey represented through charts and graphs.
- **Customizable Filters:** Focus your analysis on specific platforms, repositories, and timeframes.
- **GitHub Authentication:** Connect your accounts securely with platform-specific OAuth for private data access.
- **Activity Metrics:** Track key metrics like commits, contributions, and platform-specific data.
**Live Demo (Link will be updated upon deployment):**

[https://your-deployed-app-url.herokuapp.com](https://your-deployed-app-url.herokuapp.com)

**Project Blog Post:**

[Your Blog Post URL]([Your Blog Post URL])

## Author(s):

- **Natasha Daije** 
    - LinkedIn: [https://www.linkedin.com/in/natasha-mbugua/](https://www.linkedin.com/in/natasha-mbugua/)


## Installation

1. **Clone the Repository:**
    ```bash
    git clone [invalid URL removed]
    ```
2. **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**
    ```bash
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up Environment Variables:**
    - Create a `.env` file in the project root and add your GitHub OAuth credentials and MongoDB URI:
        ```
        GITHUB_CLIENT_ID=your_github_client_id
        GITHUB_CLIENT_SECRET=your_github_client_secret
        SQLALCHEMY_DATABASE_URI=your_sqlalchemy_uri
        ```

## Usage

1.  **Start the Development Server:**
    ```bash
    python api/v1/app.py
    ```

2.  **Access the Application:**
    -   Open your browser and visit `http://127.0.0.1:5000/index`.
    -   (For development with HTTPS, you can use ngrok or a similar tool).

3.  **Log in:** Click on the "Sign Up" button and follow the instructions. Once logged In, you can click in 'Connect with GitHub' and follow authorization prompts

4.  **Explore and Visualize Your Activity:**  (Detailed instructions on using the app's features will be added later)


## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to help improve the project.

## Related Projects

- **[Other similar projects you find relevant]** 

## License

This project is licensed under the [MIT License](LICENSE).