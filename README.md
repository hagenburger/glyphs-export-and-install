# Export and install fonts from Glyphs.app

Installing fonts on MacOS sometimes is tricky, as fonts stay cached in the old
version, even when installing a new one.

This script solves caching issues.

1. Exports all active instances of a font
2. Deletes (uninstalls) older versions of each instance
3. Renames the exported fonts to `OriginalName-20180212-2234.otf` (including the
   current time to avoid caching issues)
4. Installs the new version into `~/Library/Fonts`

Before running this script the first time, use Glyph.app’s export function at
least once. The configuration is kept.


## Installation

```
git clone git@github.com:hagenburger/glyphs-export-and-install.git
cd glyphs-export-and-install
ln -s "`pwd`/Export-and-install.py" ~/Library/Application\ Support/Glyphs/Scripts
```

Restart Glyphs.app.

<img width="797" alt="Screenshot of the installed script in the menu" src="https://user-images.githubusercontent.com/103399/36138983-09b0cdc8-109c-11e8-914e-df7686172225.png">



## Update

In case updates are available:

```
cd glyphs-export-and-install
git pull
```


## Copyright

Copyright 2018++ [Nico Hagenburger](http://www.hagenburger.net).
See [MIT-LICENSE.md](MIT-LICENSE.md) for details.
Get in touch with [@hagenburger](https://twitter.com/hagenburger) on Twitter or
[open an issue](https://github.com/hagenburger/glyphs-export-and-install/issues/new).
