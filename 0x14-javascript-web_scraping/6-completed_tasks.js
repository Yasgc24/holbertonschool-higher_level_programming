#!/usr/bin/node
const { error } = require('console');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    console.error('error:', error);
    const completed = {};
    JSON.parse(body).forEach((tasks) => {
      if (tasks.completed && completed[tasks.userId] === undefined) {
        completed[tasks.userId] = 1;
      } else if (tasks.completed) {
        completed[tasks.userId] += 1;
      }
    });
  }
});
