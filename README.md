# Volantes Cursors

## Original Repo: https://github.com/varlesh/volantes-cursors

### Why the fork?

The original repo did only support old xcursor themes, which fail to scale cleanly (for example in 'Shake cursor'). Therefore this repo drastically improved the quality by using `kcursorgen` to use svg themes.
There are only changes to the build system, icons are still the same.

All credits belong to @varlesh, if you someday read this: I would be happy to merge this into your original repo!

### Install build version

Not available for now. Check out the original repo (not svg fixes though).

### Manual Install

1. Install dependencies:
   - git
   - tar
   - python
   - kcursorgen

2. Run the following commands as normal user:

   ```bash
   git clone https://github.com/LDprg/volantes-cursors.git
   cd volantes-cursors
   python gen.py
   ```

3. Install theme from file (tar.gz in the build folder)
