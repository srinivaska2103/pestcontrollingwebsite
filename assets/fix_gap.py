import glob

html_files = glob.glob('d:/Srinivas/pestcontrolwebsite/*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace space-x classes in flex containers with gap classes
    content = content.replace('space-x-3 xl:space-x-6', 'gap-3 xl:gap-6')
    content = content.replace('space-x-2 xl:space-x-4', 'gap-2 xl:gap-4')
    content = content.replace('class="flex space-x-4"', 'class="flex gap-4"')
    content = content.replace('justify-center space-x-4', 'justify-center gap-4')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
