# Headify

## Overview

![Python Logo](https://res.cloudinary.com/ddrntb739/image/upload/v1714560791/headify_qu82d8.png)

Headify is a custom Odoo module designed to modify the website header. It provides an image cover header with a hamburger menu, inspired by the [Bootstrap theme](https://preview.colorlib.com/theme/bootstrap/website-menu-20/index.html).

## Requirements

- PostgreSQL
- Odoo v17

## Installation

1. Clone this repository to your Odoo addons directory.
2. Restart your Odoo server.
3. Install the "Headify" module from the Odoo Apps menu.

## File Structure

```
.
├── headify
│   ├── __init__.py
│   ├── controllers
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── static ├──src
│   │   ├── css
│   │   │   ├── style.css
│   │   │   └── ...
│   │   ├── fonts
│   │   │   ├── fontawesome-webfont.woff2
│   │   │   └── ...
│   │   ├── images
│   │   │   ├── bg-1.jpg
│   │   │   └── ...
│   │   ├── js
│   │   │   ├── main.js
│   │   │   └── ...
│   │   ├── scss
│   │   │   ├── _variables.scss
│   │   │   └── ...
│   │   └── description
│   │       └── icon.png
│   ├── views
│   │   ├── css_loader.xml
│   │   └── header.xml
│   ├── __manifest__.py
│   └── README.md
└── ...
```

## Usage

Once installed, the "Headify" module will modify the website header to display the custom image cover header with a hamburger menu.

## Credits

- Bootstrap theme: [Colorlib](https://preview.colorlib.com/theme/bootstrap/website-menu-20/index.html)
