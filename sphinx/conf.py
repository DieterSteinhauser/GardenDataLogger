# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import subprocess


if os.path.abspath('..') not in sys.path:
    sys.path.insert(0, os.path.abspath('..'))  # '..' moves up one folder, much like 'cd ..'

print(sys.path)  # prints the sys.path for debugging

# -- Project information -----------------------------------------------------

project = 'Autonomous Drone Station'
copyright = '2023, Drone Maestros, Agribugs, UF IoT4Ag'
author = 'Dieter Steinhauser'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosectionlabel', 'sphinx.ext.napoleon',
              'sphinx.ext.coverage', 'sphinx.ext.extlinks']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_mock_imports = ["machine"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinx_material'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def is_doxygen_installed():
    try:
        # Run the command to check if Doxygen is installed
        subprocess.run(['doxygen', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

if is_doxygen_installed():
    extensions.append('breathe')
    extensions.append('sphinx.ext.graphviz')

    # Breathe Configuration
    breathe_projects = {
        'control_station': r'doxygen\xml'
    }
    breathe_default_project = 'control_station'

    breathe_default_members = ('members', 'undoc-members', 'private-members')

    breathe_projects_source = {
        "myprojectsource" : (
            "../control_station_gui/control_station/source/", ["ComDevice.cpp","MainComponent.cpp","Main.cpp", "cSerialPortListMonitor.cpp","SerialPortMenu.cpp"]
        )
    }


#  extra options for the read the docs theme.

# html_theme_options = {
#     'analytics_id': 'G-XXXXXXXXXX',  # Provided by Google in your dashboard
#     'analytics_anonymize_ip': False,
#     'logo_only': False,
#     'display_version': True,
#     'prev_next_buttons_location': 'bottom',
#     'style_external_links': False,
#     'vcs_pageview_mode': '',
#     'style_nav_header_background': 'seaborn',
#     # Toc options
#     'collapse_navigation': True,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
#     'includehidden': True,
#     'titles_only': False
# }
