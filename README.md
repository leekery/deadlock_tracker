## INFO

This project is designed to compare numbers extracted from specific regions of game (Deadlock). It uses OCR (Optical Character Recognition) to recognize text from images and provides a visual overlay if the percentage difference between the numbers exceeds a certain threshold (10%).

### Showcase in-game UI:

![image](https://github.com/user-attachments/assets/983a89af-4831-4835-8245-d0487580c395)


### Key Features:
- **Region Selection**: Select multiple regions from the screen to capture and compare numbers.
- **OCR Integration**: Uses Tesseract OCR to recognize text from the selected regions.
- **Visual Overlay**: Displays a visual overlay if the percentage difference between the numbers exceeds 10%.

## How to Use

### Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Install Tesseract OCR**:
    - Download and install Tesseract OCR from [this link](https://github.com/UB-Mannheim/tesseract/wiki).

### Running the Project

1. **Navigate to the project directory**:
    ```sh
    cd src
    ```

2. **Run the main application**:
    ```sh
    python main.py
    ```
