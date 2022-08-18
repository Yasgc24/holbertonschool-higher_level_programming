#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  }
  let count = 0;
  for (const result of JSON.parse(body).results) {
    for (const urlwed of result.characters) {
      if (urlwed.includes(18)) {
        count++;
      }
    }
  }
  console.log(count);
});
