<<<<<<< HEAD
# Air Canvas (Beginner Friendly)

Draw in the air using your webcam. Two ways:
1) **Basic**: track a colored object (like a blue cap) to draw.
2) **Advanced (optional)**: use **MediaPipe** to track your index fingertip.

---

## 1) Install Python & VS Code
- Install Python 3.9+ from https://python.org (tick "Add Python to PATH" on Windows).
- Install VS Code from https://code.visualstudio.com

## 2) Get the code
Download this repo as a zip and extract, or `git clone` if you upload it to GitHub.

## 3) Create a virtual environment (recommended)
**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
**macOS/Linux (bash/zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4) Install dependencies
```bash
pip install -r requirements.txt
```

## 5) Pick ONE path to start

### Path A — Basic (colored object)
1. Stick a **bright blue** tape/marker cap to your fingertip (or use any color and tune it).
2. Run the **color tuner** to find HSV values that isolate your object:
   ```bash
   python color_tuner.py
   ```
   - Move sliders until your object appears **solid white** in the *Mask* window.
   - Note the **Lower/Upper HSV** numbers printed in the terminal.
3. Put those values into `air_canvas_basic.py` (look for the line with `lower_hsv` / `upper_hsv`).
4. Run the canvas:
   ```bash
   python air_canvas_basic.py
   ```

**Controls (Basic):**
- `1/2/3` — change pen color
- `[` / `]` — thinner / thicker line
- `c` — clear the canvas
- `s` — save a PNG to `shots/`
- `q` — quit

### Path B — Advanced (MediaPipe hand tracking)
> No colored object needed. Tracks your **index fingertip**.

Run:
```bash
python air_canvas_mediapipe.py
```

**Controls (Advanced):**
- `d` — toggle drawing ON/OFF
- `h` — toggle show hand landmarks
- `1/2/3` — change pen color
- `[` / `]` — thinner / thicker line
- `c` — clear the canvas
- `s` — save a PNG to `shots/`
- `q` — quit

---

## Troubleshooting
- **Black/blank camera window**: close other apps using the camera; try `VideoCapture(1)` instead of `0`.
- **No `cv2.imshow` window**: avoid running in WSL; run directly in Windows/macOS/Linux.
- **`pip` not found**: use `python -m pip install ...` or `py -m pip install ...` (Windows).
- **Mask is noisy** (Basic): improve lighting, move sliders in `color_tuner.py`, try a different color (neon/bright works well).
- **Laggy video**: close heavy apps, reduce frame size.

---

## How it works (super short)
- Read webcam frames with OpenCV.
- Find either your colored object (Basic) or your fingertip (Advanced).
- Store the fingertip points and draw lines on a transparent canvas.
- Overlay the canvas on the live video.

---

## Show it on LinkedIn (template)
> 🚀 Built an **Air Canvas** with Python + OpenCV (and MediaPipe)!  
> I can draw in the air using my fingertip—no touchscreen needed.  
> **What I learned:** HSV color masking, contour detection, hand landmarks, and real-time video processing.  
> **Tech:** Python, OpenCV, MediaPipe  
> 🎥 Demo attached | 💻 Code in comments

Tip: Record with **OBS** or **Xbox Game Bar** (Win: `Win + G`), trim, and post.

Good luck & have fun!
=======
# air-canvas-ritu
>>>>>>> 19ac56c1076a4e2ec2c3610909aedb095258571b
