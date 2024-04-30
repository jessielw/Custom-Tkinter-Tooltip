from setuptools import setup, find_packages

tool_version = '1.4'
short_description = "Basic Hover Tooltip for Tkinter based off of Tkinter's built in tooltip"
long_description = "This package enables a customizable tooltip when you hover the mouse over a defined widget. " \
                   "It's built off of the Tkinter's built in Hovertip class. However it has most of the " \
                   "functionality of the label widget. You can set font, colors, relief, border, wrap length, " \
                   "anchor, border, textvariable, and width."

# Setting up
setup(
    name="Custom-Tooltip",
    version=tool_version,
    author="jlw4049 (Jessie Wilson)",
    author_email="<jessielw4049@gmail.com>",
    description=short_description,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    url='https://github.com/jlw4049/Custom-Tkinter-Tooltip',
    keywords=['python', 'tkinter', 'hovertip', 'tooltip', 'infotip', 'bubble'],
    classifiers=["Programming Language :: Python :: 3.6", 'Development Status :: 6 - Mature'])
