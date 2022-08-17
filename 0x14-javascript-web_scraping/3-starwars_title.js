#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/:id' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
