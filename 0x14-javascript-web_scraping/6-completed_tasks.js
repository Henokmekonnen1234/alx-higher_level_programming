#!/usr/bin/node
const request = require('request');
if (process.argv[2]) {
  function Request (url) {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      }
      );
    }
    );
  }

  Request(process.argv[2])
    .then(response => {
      const task = {};
      response.forEach(data => {
        if (data.completed && !Object.keys(task).includes(String(data.userId))) {
          task[data.userId] = 0;
        }
        if (data.completed && Object.keys(task).includes(String(data.userId))) {
          task[data.userId] = task[data.userId] + 1;
        }
      }
      );
      console.log(task);
    }
    )
    .catch(error => console.error(error));
}
