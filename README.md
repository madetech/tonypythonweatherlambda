# tonypythonweatherlambda

## Deployment instructions
1. Zip up lambda function
```
zip my-deployment-package.zip lambda_function.py
```
2. Push lambda zip to AWS
```
aws-vault exec madesso -- aws lambda update-function-code --function-name getLondonWeather --zip-file fileb://my-deployment-package.zip
```


