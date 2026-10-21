// Publish only the canonical, audited site. Earlier merged snapshots stay in Git history.
import { mkdirSync, copyFileSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
const files=['index.html','assets/app.js','assets/style.css','data/itinerary.js',
 ...['days','places','transport','review','food-guide','cafes-guide','markets-guide','shopping-guide','sights-guide','stays-guide'].map(n=>`pages/${n}.html`)];
rmSync('build',{recursive:true,force:true});
for(const file of files){const dest=join('build',file);mkdirSync(dirname(dest),{recursive:true});copyFileSync(file,dest)}
console.log(`Built ${files.length} audited static files in build/`);
