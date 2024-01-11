#!/usr/bin/node
const request = require('request');
if (process.argv[2]) {
  function makeRequest (url) {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(response);
        }
      }
      );
    }
    );
  }

  makeRequest(process.argv[2])
    .then((response) => {
      console.log('code: ' + response.statusCode);
    })
    .catch((error) => {
      console.error(error);
    });
}
