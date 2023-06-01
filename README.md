# PranksterShot

This Python script is a playful project created to catch unsuspecting colleagues when they try to poke around your unlocked laptop. When run, it patiently waits for any mouse or keyboard activity and, when detected, it springs into action by quickly capturing webcam shots. It's a fun and harmless way to remind everyone about the importance of computer security.

## Getting Started

These instructions will guide you to run this script on your local machine. The script has been tested on Ubuntu Linux with the MATE desktop environment.

### Prerequisites

You'll need Python3 installed and pip, the Python package installer. This script also requires the `cv2` and `pynput` packages. A `requirements.txt` file is provided to install these packages.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your_username/PranksterShot.git
```

2. Go into the project directory:
```bash
cd PranksterShot
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

4. Make the script executable:
```bash
chmod 755 prankstershot.py
```

5. Move the script to /usr/local/bin to be able to run it with a single command:
```bash
sudo mv prankstershot.py /usr/local/bin/prankstershot
```

### Usage
To run the script, simply open a terminal and type:

```bash
prankstershot
```

After initiating the script, you will have a brief window of 5 seconds to minimize the terminal and make your desktop look less suspicious before walking away from your laptop. Remember to set a password on your screensaver; without it, the prank won't make as much sense.

The script will then wait for any keyboard or mouse activity. When such activity is detected, it will start taking pictures with the webcam and save them to the designated folder. The script will stop after capturing a predetermined number of pictures and will lock the screen, requiring a password to unlock.

## Caution
Remember, this is intended for fun and should be used responsibly. Always respect people's privacy.