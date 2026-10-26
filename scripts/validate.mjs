import { places,days,routes,S } from '../data/itinerary.js';
import { readFileSync,existsSync,readdirSync } from 'node:fs';
import { resolve,dirname } from 'node:path';
let failures=[];
const fail=(m)=>failures.push(m);
for(const [i,p] of places.entries()){
 if(!Array.from({length:16},(_,i)=>i+1).includes(p.day))fail(`Row ${i}: invalid day`);
 if(!['verified','partial','unverified'].includes(p.status))fail(`Row ${i}: invalid status`);
 if(!p.name||!p.type||!p.detail)fail(`Row ${i}: missing identifying info`);
 if(!p.source?.startsWith('https://'))fail(`Row ${i}: missing HTTPS official source`);
 if(p.extra && !p.extra.startsWith('https://'))fail(`Row ${i}: invalid extra source`);
 if(p.status==='unverified'&&(p.where||p.hours))fail(`Row ${i}: unverified fields must be blank`);
 if(p.sourceKind==='context'&&p.status!=='unverified')fail(`Row ${i}: context link cannot verify row`);
}
const ids=new Set();
for(const day of days){if(ids.has(day.n))fail(`Duplicate day ${day.n}`);ids.add(day.n);if(!day.steps?.length)fail(`No steps day ${day.n}`);for(const step of day.steps)if(!step[2]?.startsWith('https://'))fail(`Unsourced step day ${day.n}`)}
if(days.length!==16)fail('Expected all 16 supplied itinerary days');
for(let n=1;n<=16;n++)if(!ids.has(n))fail(`Missing day ${n}`);
for(const [i,r] of routes.entries())if(!r.source?.startsWith('https://'))fail(`Route ${i}: missing official link`);
const files=['index.html',...['days','places','transport','review','food-guide','cafes-guide','markets-guide','shopping-guide','sights-guide','stays-guide'].map(n=>`pages/${n}.html`)];
for(const f of files){if(!existsSync(f)){fail(`Missing ${f}`);continue};const text=readFileSync(f,'utf8');for(const m of text.matchAll(/(?:href|src)="([^"#]+)"/g)){const url=m[1];if(url.startsWith('http')||url.startsWith('data:'))continue;const target=resolve(dirname(f),url.split('#')[0]);if(!existsSync(target))fail(`${f}: broken asset ${url}`)}}
// Legacy Pages publishes the entire repository root, not build/. Refuse to publish
// additional HTML tables bypassing this validator; old routes must redirect.
const aliases={accommodation:'stays-guide.html',all:'places.html',attractions:'sights-guide.html',busan:'days.html#day-9',cafes:'cafes-guide.html',flagged:'review.html',food:'food-guide.html',markets:'markets-guide.html',nightlife:'food-guide.html',shopping:'shopping-guide.html',transportation:'transport.html',activities:'sights-guide.html','day-by-day':'days.html'};
for(const name of readdirSync('pages').filter(n=>n.endsWith('.html'))){
 const f=`pages/${name}`;if(files.includes(f))continue;
 const target=aliases[name.slice(0,-5)],text=readFileSync(f,'utf8');
 if(!target||!text.includes(`url=${target}`)||!text.includes(`href=\"${target}\"`)||/<table\b/i.test(text))fail(`${f}: unexpected published page or invalid redirect`);
 if(target&&!existsSync(`pages/${target.split('#')[0]}`))fail(`${f}: missing redirect target ${target}`);
}
for(const [key,url] of Object.entries(S))if(!url.startsWith('https://'))fail(`Source ${key} not HTTPS`);
if(failures.length){console.error(failures.join('\n'));process.exit(1)}
console.log(`OK: ${days.length} days, ${places.length} place entries, ${routes.length} routes, ${files.length} HTML pages; all rows and steps have official links.`);
