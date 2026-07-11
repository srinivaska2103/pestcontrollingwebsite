import os
import glob
import re

directory = r'd:\Srinivas\pestcontrolwebsite'
html_files = glob.glob(os.path.join(directory, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Remove the theme-toggle from the top nav mobile section (if present)
    # The pattern is:
    # <button class="theme-toggle text-gray-500 p-2">
    #     <i class="fas fa-moon dark:hidden"></i>
    #     <i class="fas fa-sun hidden dark:block text-yellow-400"></i>
    # </button>
    pattern_remove = r'<button class=\"theme-toggle text-gray-500[^\"]* p-2\">\s*<i class=\"fas fa-moon dark:hidden\"></i>\s*<i class=\"fas fa-sun hidden dark:block text-yellow-400\"></i>\s*</button>'
    content = re.sub(pattern_remove, '', content)
    
    # Clean up empty gap container if it's now just the bars
    content = re.sub(r'<div class=\"lg:hidden flex items-center gap-4\">\s*<button id=\"mobileMenuBtn\"', r'<div class="lg:hidden flex items-center gap-4">\n                    <button id="mobileMenuBtn"', content)
    
    # 2. Add the theme toggle to the mobile menu right above dir-toggle or right after pt-4
    theme_toggle_btn = '''<button class="theme-toggle flex items-center justify-center w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-gray-700 dark:text-gray-300 mb-2">
                        <i class="fas fa-moon dark:hidden mr-2"></i>
                        <i class="fas fa-sun hidden dark:block text-yellow-400 mr-2"></i> Toggle Theme
                    </button>'''
    
    # Look for the insertion point
    if 'id="mobileMenu"' in content:
        if 'Toggle Theme' not in content: # to prevent double addition
            if 'pt-4 flex flex-col gap-3' in content:
                content = content.replace('<div class="pt-4 flex flex-col gap-3">', '<div class="pt-4 flex flex-col gap-3">\n                    ' + theme_toggle_btn)
            elif '<div class="px-4 pt-2 pb-6 space-y-1 shadow-lg">' in content:
                # Fallback if the pt-4 div is not present (e.g. services.html)
                content = content.replace('<div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-darkbg border-t border-gray-200 dark:border-gray-800 absolute w-full">', '<div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-darkbg border-t border-gray-200 dark:border-gray-800 absolute w-full">\n        <div class="px-4 pt-4">\n            ' + theme_toggle_btn + '\n        </div>')
            else:
                 # Last resort for files like services.html that have a simpler mobile menu
                 content = content.replace('<div id="mobileMenu"', '<div id="mobileMenu"')
                 # Need to manually inject it.
                 if '<a href="index.html"' in content and '<div id="mobileMenu"' in content:
                    content = content.replace('<div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-darkbg border-t border-gray-200 dark:border-gray-800 absolute w-full">', '<div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-darkbg border-t border-gray-200 dark:border-gray-800 absolute w-full">\n            <div class="px-4 pt-4 pb-2 border-b border-gray-100 dark:border-gray-700 mb-2">\n                ' + theme_toggle_btn + '\n            </div>')
            
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated:', filepath)
