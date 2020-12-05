# AWS SAM

![AWS SAM](sam-logo.png)

## Features

- Local test
- Deployment types (All-at-once, Canary, Linear)
- Polyglot (Python 3.8, Node.js 12)
- CI/CD *(todo)*
- Layers *(todo)*

## Commands

- **Init app**
  ```bash
  sam init
  ```
- **Build**

  build all functions

  ```bash
  sam build --use-container
  ```

  build specific function

  ```bash
  sam build --use-container HelloWorldFunction
  ```

- **Run Lambda locally**
  ```bash
  sam local invoke HelloWorldFunction
  ```
  use event data from file
  ```bash
  sam local invoke HelloWorldFunction -e events/event.json
  ```
  use event data from command
  ```bash
  echo '{ "message": "Hey, are you there?" }' | sam local invoke HelloWorldFunction -e -
  ```
- **Start API Gateway server**
  ```bash
  sam local start-api
  curl http://localhost:3000/
  ```
- **Deploy**
  ```bash
  sam deploy \
  --region eu-west-1 \
  --capabilities CAPABILITY_IAM \
  --s3-bucket sonufrienko-deployments \
  --s3-prefix demo-api \
  --stack-name demo-api
  ```
- **Unit tests**
  ```bash
  pip install pytest pytest-mock --user
  python -m pytest tests/ -v
  ```
- **Fetch logs from CloudWatch**
  ```bash
  sam logs -n HelloWorldFunction --stack-name demo-api --tail
  ```
- **Validate SAM template**
  ```bash
  sam validate
  ```
- **Delete app**
  ```bash
  aws cloudformation delete-stack --stack-name demo-api
  ```
