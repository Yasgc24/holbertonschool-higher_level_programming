#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/:id' + process.argv[2];

request.get(URL, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
