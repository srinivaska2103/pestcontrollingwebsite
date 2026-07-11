const fs = require('fs');
const path = require('path');

const directory = 'd:/Srinivas/pestcontrolwebsite';
const files = fs.readdirSync(directory);
const htmlFiles = files.filter(f => f.endsWith('.html')).map(f => path.join(directory, f));

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Replace space-x classes in flex containers with gap classes
    content = content.split('space-x-3 xl:space-x-6').join('gap-3 xl:gap-6');
    content = content.split('space-x-2 xl:space-x-4').join('gap-2 xl:gap-4');
    content = content.split('class="flex space-x-4"').join('class="flex gap-4"');
    content = content.split('justify-center space-x-4').join('justify-center gap-4');
    
    fs.writeFileSync(file, content, 'utf8');
});
