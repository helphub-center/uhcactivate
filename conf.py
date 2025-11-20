# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any custom paths here if modules are outside the root directory
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Set Up VIZIO Account'
copyright = '2025, VIZIO'
author = 'VIZIO Support Team'

# Full version
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any required Sphinx extensions here
extensions = []

# Enable raw HTML in RST files
raw_enabled = True

# Templates directory
templates_path = ['_templates']

# Files and directories to ignore when building
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Title setup
html_title = "How to Set Up a VIZIO Account – Complete Guide"
html_short_title = "VIZIO Setup Guide"

# Favicon (place the file in _static or project root)
html_favicon = 'favicon.ico'

# Hide page source link
tml_show_sourcelink = False

# Allow unsafe raw HTML in RST
html_allow_unsafe = True

# Theme options
html_theme_options = {
    'show_powered_by': False,
}

# Static asset directory
# html_static_path = ['_static']  # Uncomment if using static files
