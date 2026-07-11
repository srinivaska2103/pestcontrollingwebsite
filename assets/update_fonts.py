import sys, re

with open('d:/Srinivas/pestcontrolwebsite/aboutus.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<!-- 7\. Safety & Quality Standards -->.*?)(</section>)', re.DOTALL)
match = pattern.search(content)

if match:
    section = match.group(1)
    
    # change h4 font-bold to font-semibold
    section = section.replace('font-bold text-gray-900', 'font-semibold text-gray-900')
    
    # change p text to font-semibold
    section = section.replace('class="text-gray-600 dark:text-gray-400"', 'class="text-gray-600 dark:text-gray-400 font-semibold"')
    
    new_content = content[:match.start()] + section + match.group(2) + content[match.end():]
    
    with open('d:/Srinivas/pestcontrolwebsite/aboutus.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Updated Safety & Quality Standards section')
else:
    print('Section not found')
