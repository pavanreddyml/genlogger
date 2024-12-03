# GLogger: The Logger That Speaks Your Language

Say hello to or **GenLogger** – the logger that makes your debugging a vibe. We’ve officially retired the tired old "DEBUG," "INFO," and "ERROR" for something with a little more personality: **YAP**, **DEETS**, **SKETCH**, **SUS**, and when things go totally sideways, **COOKED**. 

This isn’t just a logger; it’s a generational bridge for your codebase. Gen Z will call it lit, Millennials will embrace it ironically (but actually love it), and Boomers… well, they’ll ask for the docs (they wont be here long anyways). So why settle for boring logs when you can debug with *style*? Spice up your workflow and let your logs do the talking!

For now, we only support the coolest generation of all time – **Gen Z**. But don't worry, we'll be adding support for Millennials, Boomers, and other generations soon because we're all about inclusivity, even though y'all ain't as cool as us, you're still cool.


# Usage

To get started, simply integrate **GLogger** into your existing code:

```python
import logging
from genlogger import GenLogging, GenZ
GenLogging(generation=GenZ)
```

This modifies the `logging` module in place and works seamlessly with your current setup. **Important:** Make sure you import `glogger` *after* importing the `logging` module. If you import it before and your system gets **COOKED**, well… that’s on you. We’re Gen Z; we don’t write tests. 😉

# Contributing

Read `CONTRIBUTING.md`. Dont expect everything in `README.md`. Also figure it out, documentation is not a **GenZ** thing.

# Example Logs
```
2024-12-03 12:41:14,649 - SYSTEM IS COOKED - Victoria Daniels queried something at 1986-12-26 19:29:17
2024-12-03 12:41:14,649 - JUST YAPPING - William Lewis deleted something at 1988-12-15 19:36:26
2024-12-03 12:41:14,649 - JUST YAPPING - Heidi Smith retrieved something at 1980-01-31 04:13:07
2024-12-03 12:41:14,649 - THAT'S SKETCH - Alyssa Day queried something at 1996-05-17 12:07:21
2024-12-03 12:41:14,649 - SOMETHING IS SUS - Lisa Rodriguez created something at 2013-09-26 02:56:25
2024-12-03 12:41:14,649 - JUST YAPPING - Dominic Yoder queried something at 2010-01-23 02:13:55
2024-12-03 12:41:14,649 - THAT'S SKETCH - Paul Mcconnell created something at 1997-09-29 22:33:00
2024-12-03 12:41:14,649 - SOMETHING IS SUS - Savannah Schroeder retrieved something at 2007-06-22 22:12:29
2024-12-03 12:41:14,649 - THAT'S SKETCH - Dennis Cook updated something at 2024-10-31 11:30:04
2024-12-03 12:41:14,649 - SOMETHING IS SUS - Ronald Goodwin created something at 1975-11-02 22:35:27
```
