# Volantes Cursors

### Install build version

https://www.pling.com/p/1356095/

### Manual Install

1. Install dependencies:
   - git
   - tar
   - kcursorgen
   - xcursorgen
   - hyprcursor-util (only for hyprcusors)

2. Run the following commands as normal user:

   ```bash
   git clone https://github.com/varlesh/volantes-cursors.git
   cd volantes-cursors
   python gen.py
   sudo python install.py # System wide install
   ```

   For hyprcusors use following instead:

   ```bash
   git clone https://github.com/varlesh/volantes-cursors.git
   cd volantes-cursors
   python gen.py --hyprcursor
   python install_local.py # Local user install
   ```

3. Choose a theme in the Settings or in the Tweaks tool.
