# Spotify Stats Viewer

A Python program to view your Spotify stats for different artists and songs using the Spotify Web API.

## Features

- View top tracks
- View top artists
- Easy-to-use command line interface

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/spotify-stats-viewer.git
    cd spotify-stats-viewer
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Get Spotify API credentials**:
    - Sign up on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
    - Create a new application to get your client ID and client secret.
    - Set the Redirect URI in the Spotify Developer Dashboard.

5. **Create a `.env` file** in the project root directory and add your Spotify API credentials:
    ```plaintext
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    REDIRECT_URI=your_redirect_uri
    ```

## Usage

1. **Run the program**:
    ```sh
    python main.py
    ```

2. **Follow the on-screen instructions** to authenticate and view your stats.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**: `git checkout -b feature/your-feature`
3. **Make your changes**.
4. **Commit your changes**: `git commit -m 'Add some feature'`
5. **Push to the branch**: `git push origin feature/your-feature`
6. **Submit a pull request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Spotipy](https://spotipy.readthedocs.io/) - A lightweight Python library for the Spotify Web API.

