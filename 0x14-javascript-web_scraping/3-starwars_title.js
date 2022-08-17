#!/usr/bin/node
const request = require('request');

request.get('https://swapi-api.hbtn.io/api/films/:id' + process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
