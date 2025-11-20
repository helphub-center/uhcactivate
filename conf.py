# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# Add any custom paths here if modules are outside the root directory
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'UHC UCard Activation Guide'
copyright = '2025, UHC'
author = 'UHC Support Team'

# Full version
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Enable raw HTML in RST files
raw_enabled = True

# Templates directory
templates_path = ['_templates']

# Files and directories to ignore when building
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Title setup
html_title = "How to Activate Your UHC UCard – Complete Guide"
html_short_title = "UHC UCard Activation"

# Favicon (place favicon.ico in project root or _static)
html_favicon = 'favicon.ico'

# Hide page source link
html_show_sourcelink = False

# Theme options
html_theme_options = {
    'show_powered_by': False,
}

# Static asset directory (uncomment if needed)
# html_static_path = ['_static']
