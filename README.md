# Nutri-Hydra Calc Pro 💧🍎

A comprehensive, multilingual tool designed to calculate daily water intake and nutritional requirements (Proteins, Fats, Carbohydrates, and Fiber) based on personal biometrics and physical activity levels.

## 🌟 Features

- **Multi-Platform:** Available in HTML/JS (Web), C++ (CLI), and Python (GUI).
- **Internationalization:** Full support for 5 languages: English, Italian, German, French, and Spanish.
- **Dual Unit System:** Seamlessly toggle between **Metric** (kg/cm/L) and **Imperial** (lb/in/gal) units.
- **Visual Analytics:** Interactive pie charts (Web/Python) and progress bars (C++) to visualize macronutrient distribution.
- **Smart Logic:** Adjusts recommendations based on age, gender, weight, and sport frequency/intensity.
- **Dark Mode:** Optimized for eye comfort with modern dark themes.

---

## 🛠 Installation & Usage

### 1. Web Version (HTML/JS)
The easiest way to use the app. No installation required.

- **Requirements:** Any modern web browser (Chrome, Firefox, Safari, Edge).
- **Setup:**
  1. Download the `index.html` file.
  2. Open the file directly in your browser.
  3. *Note: An active internet connection is required to load the Chart.js library via CDN.*

---

### 2. Python Version (GUI)
A modern desktop application featuring a "CustomTkinter" interface and Matplotlib integration.

- **Requirements:** Python 3.8+
- **Dependencies:**
  ```bash
  pip install customtkinter matplotlib
  Setup:

Navigate to the Python directory.

Run the script:
  '''Bash'''
  python nutri_hydra.py
3. C++ Version (CLI)
A high-performance command-line tool with a custom translation engine and progress-bar visualization.

Requirements: A C++ compiler supporting C++11 or higher (GCC, Clang, or MSVC).

Compilation:

Bash
# Example using G++
g++ -o nutri_calc main.cpp
Usage:

Run the compiled executable:

Bash
./nutri_calc
Follow the on-screen prompts to select your language and input data.

📊 Nutritional Logic
Water Intake: Calculated using weight-based algorithms (30-35ml/kg) plus dynamic sport offsets.

Proteins: Optimized at 1.2g/kg for sedentary users and 1.6g/kg for active users.

Fats: Standardized at 0.9g/kg following Mediterranean Diet guidelines.

Carbohydrates: Balanced to provide the remaining energy requirements based on activity.

Created with ❤️ for a healthier lifestyle.
