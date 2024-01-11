#!/usr/bin/node
const request = require('request');
if (process.argv[2]) {
  function makeRequest (url) {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      }
      );
    }
    );
  }

  const url = 'https://swapi-api.alx-tools.com/api/films/';
  makeRequest(url + process.argv[2])
    .then((response) => {
      const values = JSON.parse(response);
      console.log(values.title);
    })
    .catch((error) => {
      console.error(error);
    });
}
