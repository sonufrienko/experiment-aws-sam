const fetch = require('node-fetch');

exports.handler = async (event) => {
  const response = await fetch('https://checkip.amazonaws.com/');
  const ip = await response.text();

  return {
    statusCode: 200,
    body: JSON.stringify({
      message: 'v2 hello world from Node.js function',
      location: ip.replace('\n', ''),
    }),
  };
};
