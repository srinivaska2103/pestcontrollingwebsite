const fs = require('fs');
const path = require('path');

const directory = 'd:/Srinivas/pestcontrolwebsite';
const files = fs.readdirSync(directory);
const htmlFiles = files.filter(f => f.endsWith('.html')).map(f => path.join(directory, f));

htmlFiles.forEach(filepath => {
    let content = fs.readFileSync(filepath, 'utf8');
    const originalContent = content;
    
    // 1. Remove the theme-toggle from the top nav mobile section (if present)
    const patternRemove = /<button class="theme-toggle text-gray-500[^"]* p-2">\s*<i class="fas fa-moon dark:hidden"><\/i>\s*<i class="fas fa-sun hidden dark:block text-yellow-400"><\/i>\s*<\/button>/g;
    content = content.replace(patternRemove, '');
    
    // Clean up empty gap container if it's now just the bars
    content = content.replace(/<div class="lg:hidden flex items-center gap-4">\s*<button id="mobileMenuBtn"/g, '<div class="lg:hidden flex items-center gap-4">\n                    <button id="mobileMenuBtn"');
    
    // 2. Add the theme toggle to the mobile menu right above dir-toggle or right after pt-4
    const themeToggleBtn = `<button class="theme-toggle flex items-center justify-center w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-gray-700 dark:text-gray-300 mb-2">
                        <i class="fas fa-moon dark:hidden mr-2"></i>
                        <i class="fas fa-sun hidden dark:block text-yellow-400 mr-2"></i> Toggle Theme
                    </button>`;
    
    // Look for the insertion point
    if (content.includes('id="mobileMenu"')) {
        if (!content.includes('Toggle Theme')) { // to prevent double addition
            if (content.includes('pt-4 flex flex-col gap-3')) {
                content = content.replace('<div class="pt-4 flex flex-col gap-3">', '<div class="pt-4 flex flex-col gap-3">\n                    ' + themeToggleBtn);
            } else if (content.includes('<div class="px-4 pt-2 pb-6 space-y-1 shadow-lg">')) {
                // Fallback if the pt-4 div is not present (e.g. services.html)
                content = content.replace('<div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-darkbg border-t border-gray-200 dark:border-gray-800 absolute w-full">', '<div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-darkbg border-t border-gray-200 dark:border-gray-800 absolute w-full">\n        <div class="px-4 pt-4">\n            ' + themeToggleBtn + '\n        </div>');
            } else {
                 // Last resort for files like services.html that have a simpler mobile menu
                 if (content.includes('<a href="index.html"') && content.includes('<div id="mobileMenu"')) {
                    content = content.replace('<div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-darkbg border-t border-gray-200 dark:border-gray-800 absolute w-full">', '<div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-darkbg border-t border-gray-200 dark:border-gray-800 absolute w-full">\n            <div class="px-4 pt-4 pb-2 border-b border-gray-100 dark:border-gray-700 mb-2">\n                ' + themeToggleBtn + '\n            </div>');
                 }
            }
        }
    }
            
    if (content !== originalContent) {
        fs.writeFileSync(filepath, content, 'utf8');
        console.log('Updated:', filepath);
    }
});
