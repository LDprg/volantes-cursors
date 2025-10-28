# Volantes Cursors

### Install build version

https://www.pling.com/p/1356095/

### Manual Install

1. Install dependencies:
   - git
   - tar
   - kcursorgen
   - hyprcursor-util (only for hyprcusors)

2. Run the following commands as normal user:

   ```bash
   git clone https://github.com/varlesh/volantes-cursors.git
   cd volantes-cursors
   python gen.py
   sudo python install.py
   ```

   For hyprcusors use following instead:

   ```bash
   git clone https://github.com/varlesh/volantes-cursors.git
   cd volantes-cursors
   python gen.py --hyprcursor
   sudo python install.py
   ```

3. Choose a theme in the Settings or in the Tweaks tool.
