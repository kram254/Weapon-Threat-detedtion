# OpenThreatDetection Setup Guide

## Installation Steps

1. **Boot from ISO:**

   - Insert the `OpenThreatDetection.iso` into the server.
2. **Configure Cameras:**

   - Place `cameras.json` in `/etc/openthreatdetection/`.
3. **Run the System:**

   ```bash
   cd /path/to/OpenThreatDetection
   source venv/bin/activate
   python main.py --config config.yaml
   ```
