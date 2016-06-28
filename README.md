# silly-little-class-checker
Find the classes in your CSS file that aren't in your HTML file.

## Use
Drop an index.html and screen.css file into this directory, then

```
python3 find-classes.py
```

Info is sent to stdout and data/outputs.txt.

## Notes, to-do's, etc
Current status: way rough. Basically me learning how to use regex, python, etc. But! It does/can provide some helpful information for manually cleaning out unused classes from CSS files.

Because I am not a full-time regex ninja and I haven't spent much time on this, there's lots of false positives (picking up decimal numbers as classes, for example). I'll probably upgrade that a bit when I next need to actually use this.

Also worth noting, this won't treat utility classes (e.g., .hidden, .animate) as special. So!

I'd also like to expand this to deal with multiple .html files, maybe look through a sass directory, etc.
